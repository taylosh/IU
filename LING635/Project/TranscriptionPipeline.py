# -*- coding: utf-8 -*-
"""
Enhanced ASR Pipeline with VAD, Whisper, and Boundary Safety
"""
import os
import re
import logging
from pathlib import Path
import librosa
import numpy as np
from praatio import textgrid
from typing import List, Tuple, Optional, Dict
import subprocess
import json

# --------------------------
# Configuration Management
# --------------------------
DEFAULT_CONFIG = {
    "vad_aggressiveness": 3,
    "silence_thresh_db": -35.0,
    "min_silence_dur": 0.1,
    "tokenizer": "whisper",
    "alignment_method": "mfa",  # or "whisper"
    "language": "english",
    "max_workers": 4
}

def load_config(config_path: Optional[str] = None) -> Dict:
    """Load configuration from JSON or use defaults."""
    if config_path and Path(config_path).exists():
        with open(config_path) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG


# Add to dependencies: pydub and ffmpeg
# New function (modified from original):
def ensure_mono_audio(input_path: str, output_dir: str = "mono_processed") -> str:
    """Guarantees mono audio output, returns path to processed file."""
    from pydub import AudioSegment
    
    # Create output directory structure
    rel_path = Path(input_path).relative_to(Path.cwd())
    output_path = Path(output_dir) / rel_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Process audio
    audio = AudioSegment.from_wav(input_path)
    if audio.channels > 1:
        audio = audio.set_channels(1)
    
    audio.export(output_path, format="wav")
    return str(output_path)

# Modified main pipeline:
def process_file(wav_path: str, config: Dict) -> textgrid.Textgrid:
    # New first step:
    mono_path = ensure_mono_audio(wav_path, config.get("mono_output_dir", "mono_files"))
    
    # Rest of pipeline now uses mono_path instead of wav_path:
    segments = detect_speech_segments(mono_path, config=config)
    # ... (continue with existing workflow)
    

# --------------------------
# 1. Enhanced Speech Detection
# --------------------------
def detect_speech_segments(
    wav_path: str,
    method: str = "hybrid",
    config: Dict = DEFAULT_CONFIG
) -> List[Tuple[float, float]]:
    """Multi-method speech detection with boundary validation."""
    y, sr = librosa.load(wav_path, sr=None)
    max_duration = librosa.get_duration(y=y, sr=sr)
    
    if method == "hybrid":
        vad_segments = vad_detect(y, sr, config)
        amp_segments = amplitude_detect(y, sr, config)
        segments = merge_segments(vad_segments + amp_segments)
    elif method == "vad":
        segments = vad_detect(y, sr, config)
    else:
        segments = amplitude_detect(y, sr, config)
    
    segments = validate_boundaries(segments, max_duration)
    return merge_tiny_gaps(segments, config["min_silence_dur"])

def vad_detect(y: np.ndarray, sr: int, config: Dict) -> List[Tuple[float, float]]:
    """WebRTC VAD implementation with configurable aggressiveness."""
    import webrtcvad
    vad = webrtcvad.Vad(config["vad_aggressiveness"])
    frame_duration = 0.03  # 30ms frames required by WebRTC
    n_samples = int(sr * frame_duration)
    
    # Convert to 16-bit PCM
    y = (y * 32767).astype(np.int16) if y.dtype != np.int16 else y
    
    # Frame processing
    speech_frames = []
    for i in range(0, len(y), n_samples):
        frame = y[i:i+n_samples]
        frame = np.pad(frame, (0, max(0, n_samples - len(frame)), 'constant')
        speech_frames.append(vad.is_speech(frame.tobytes(), sr))
    
    # Convert to segments
    segments = []
    start = None
    for i, is_speech in enumerate(speech_frames):
        time = i * frame_duration
        if is_speech and start is None:
            start = time
        elif not is_speech and start is not None:
            segments.append((start, time))
            start = None
    return segments

def amplitude_detect(y: np.ndarray, sr: int, config: Dict) -> List[Tuple[float, float]]:
    """Librosa amplitude-based detection."""
    non_silent = librosa.effects.split(
        y, 
        top_db=-config["silence_thresh_db"],
        frame_length=2048,
        hop_length=512
    )
    return [(start/sr, end/sr) for start, end in non_silent]

# --------------------------
# 2. Phrase/Word Processing
# --------------------------
def phrase_to_word_tier(
    input_grid: textgrid.Textgrid,
    wav_path: str,
    config: Dict
) -> textgrid.Textgrid:
    """Enhanced with Whisper and acoustic timing fallbacks."""
    word_tier = textgrid.IntervalTier(
        name="words",
        entryList=[],
        minT=input_grid.minTimestamp,
        maxT=input_grid.maxTimestamp
    )
    
    for start, end, text in input_grid.getTier("phrases").entryList:
        if not text.strip():
            continue
            
        words = tokenize_text(text, config["tokenizer"])
        word_times = get_word_timings(wav_path, start, end, text, config)
        
        for word, (w_start, w_end) in zip(words, word_times):
            abs_start = start + w_start
            abs_end = start + w_end
            word_tier.insertEntry(
                (abs_start, abs_end, word),
                collisionMode="replace"  # More aggressive than merge
            )
    
    input_grid.addTier(word_tier)
    return input_grid

def get_word_timings(
    wav_path: str,
    phrase_start: float,
    phrase_end: float,
    text: str,
    config: Dict
) -> List[Tuple[float, float]]:
    """Multi-method word timing extraction."""
    if config["alignment_method"] == "whisper":
        if whisper_available():
            return get_whisper_timings(wav_path, phrase_start, phrase_end)
    
    # Fallback to proportional distribution
    words = tokenize_text(text, config["tokenizer"])
    duration = phrase_end - phrase_start
    return [(i/len(words)*duration, (i+1)/len(words)*duration) 
            for i in range(len(words))]

# --------------------------
# 3. Alignment Methods
# --------------------------
def whisper_available() -> bool:
    try:
        import whisper
        return True
    except ImportError:
        return False

def get_whisper_timings(
    wav_path: str,
    phrase_start: float,
    phrase_end: float
) -> List[Tuple[float, float]]:
    """Extract word-level timings using Whisper."""
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe(wav_path, word_timestamps=True)
    
    # Filter and normalize timings to phrase boundaries
    words = []
    for segment in result["segments"]:
        for word in segment["words"]:
            if phrase_start <= word["start"] <= phrase_end:
                rel_start = word["start"] - phrase_start
                rel_end = word["end"] - phrase_start
                words.append((rel_start, rel_end))
    return words

def forced_align(
    wav_path: str,
    textgrid_path: str,
    config: Dict
) -> str:
    """MFA alignment with error handling."""
    output_dir = config.get("output_dir", "aligned")
    cmd = [
        "mfa", "align",
        "--clean",
        wav_path,
        textgrid_path,
        config["language"],
        output_dir
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return str(Path(output_dir) / f"{Path(wav_path).stem}.TextGrid")
    except subprocess.CalledProcessError as e:
        logging.error(f"MFA failed: {e.stderr.decode()}")
        raise

# --------------------------
# Integration Points for Legacy Code
# --------------------------
def merge_legacy_features(
    input_grid: textgrid.Textgrid,
    legacy_data: Dict,
    feature_map: Dict = {
        "pitch": "pitch_contour",
        "energy": "energy_levels"
    }
) -> textgrid.Textgrid:
    """Incorporate features from legacy systems."""
    for legacy_key, tier_name in feature_map.items():
        if legacy_key in legacy_data:
            tier = textgrid.IntervalTier(
                name=tier_name,
                entryList=legacy_data[legacy_key],
                minT=input_grid.minTimestamp,
                maxT=input_grid.maxTimestamp
            )
            input_grid.addTier(tier)
    return input_grid


def apply_speech_buffers(segments: List[Tuple[float, float]], 
                        audio_duration: float,
                        buffer_ms: int = 250) -> List[Tuple[float, float]]:
    """Add safety buffers to speech segments while respecting audio boundaries"""
    buffer_sec = buffer_ms / 1000
    buffered = []
    for start, end in segments:
        new_start = max(0, start - buffer_sec)
        new_end = min(audio_duration, end + buffer_sec)
        buffered.append((new_start, new_end))
    return buffered

# Modified detect_speech_segments():
segments = detect_speech_segments(wav_path)
if config.get("speech_buffer_ms", 0) > 0:
    duration = librosa.get_duration(filename=wav_path)
    segments = apply_speech_buffers(segments, duration, config["speech_buffer_ms"])
    
def find_audio_files(root_dir: str, 
                    participant_mode: bool = False) -> List[Path]:
    """Flexible file discovery supporting both flat and participant-folder structures"""
    root = Path(root_dir)
    if participant_mode:
        return list(root.glob("Participant_*/*.wav"))
    return list(root.rglob("*.wav"))

# In process_batch():
for wav_path in find_audio_files(input_dir, config.get("participant_mode")):
    process_file(wav_path, config)
    
def get_whisper_timings(wav_path: str, 
                       phrase_start: float,
                       phrase_end: float,
                       model_size: str = "base") -> List[Tuple[float, float]]:
    """More robust local Whisper processing with segment focusing"""
    import whisper
    model = whisper.load_model(model_size)
    
    # Load and trim audio precisely
    audio = whisper.load_audio(wav_path)
    sr = 16000  # Whisper's sample rate
    start_sample = int(phrase_start * sr)
    end_sample = int(phrase_end * sr)
    segment = audio[start_sample:end_sample]
    
    result = model.transcribe(segment, word_timestamps=True)
    
    # Adjust timings relative to original file
    word_times = []
    for word in result["segments"][0]["words"]:
        adj_start = phrase_start + word["start"]
        adj_end = phrase_start + word["end"]
        word_times.append((adj_start, adj_end))
    
    return word_times

def safe_transcribe(wav_path: str, 
                   text: str,
                   config: Dict) -> str:
    """Attempt multiple transcription methods before failing"""
    methods = config.get("transcription_fallback_chain", 
                        ["whisper", "existing_text"])
    
    for method in methods:
        try:
            if method == "whisper":
                return get_whisper_transcription(wav_path)
            elif method == "existing_text":
                return text  # Use original text if provided
        except Exception as e:
            logging.warning(f"Transcription method {method} failed: {e}")
    
    return "[Transcription Unavailable]"

# In phrase_to_word_tier():
text = safe_transcribe(wav_path, text, config)

DEFAULT_CONFIG.update({
    # Speech buffer in milliseconds (0 to disable)
    "speech_buffer_ms": 250,  
    
    # For academic/research folder structures
    "participant_mode": False,
    
    # Fallback chain for transcription
    "transcription_fallback_chain": ["whisper", "existing_text"],
    
    # Whisper model size
    "whisper_model": "base"
})

# In DEFAULT_CONFIG
"mfa_models": {
    "english": {
        "dict": "assets/dicts/english.txt",
        "acoustic": "assets/models/english.zip"
    },
    "french": {
        "dict": "assets/dicts/french.dict",
        "acoustic": "assets/models/french.zip"
    }
}

# New config options
"process_tiers_containing": "phrases",  # Filter string
"preserve_tier_types": ["IntervalTier"]  # Tier classes to keep

def cleanup_mfa_temp(config: Dict):
    """Remove temporary files after processing"""
    temp_dir = Path(config["mfa_temp_dir"])
    if temp_dir.exists():
        for f in temp_dir.glob("*"):
            f.unlink()
        temp_dir.rmdir()
        
        
# --------------------------
# Main Pipeline
# --------------------------
def process_file(
    wav_path: str,
    config: Dict,
    legacy_features: Optional[Dict] = None
) -> textgrid.Textgrid:
    """Complete processing pipeline."""
    # 1. Speech detection
    segments = detect_speech_segments(wav_path, config=config)
    
    # 2. Create initial grid
    tg = textgrid.Textgrid()
    phrase_tier = textgrid.IntervalTier(
        name="phrases",
        entryList=[(s, e, "speech") for s, e in segments],
        minT=0,
        maxT=librosa.get_duration(filename=wav_path)
    )
    tg.addTier(phrase_tier)
    
    # 3. Word-level processing
    tg = phrase_to_word_tier(tg, wav_path, config)
    
    # 4. Incorporate legacy features if available
    if legacy_features:
        tg = merge_legacy_features(tg, legacy_features)
    
    # 5. Final alignment
    temp_grid = Path(config["output_dir"]) / "temp.TextGrid"
    tg.save(temp_grid)
    return forced_align(wav_path, str(temp_grid), config)
