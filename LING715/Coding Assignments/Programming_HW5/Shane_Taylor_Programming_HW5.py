#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 09:57:44 2025

@author: taylosh

Programming HW5: Spectrogram Computation

Computes a spectrogram from an audio signal using Short-Time Fourier Transform (STFT).
Returns time-frequency representation in dB with proper framing, windowing, and FFT.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import soundfile as sf

def spectrogram(sig, sr, win_len=0.025, frame_len=0.01, window_fn=np.hamming):
    '''
    Compute the spectrogram of a signal using the Short-Time Fourier Transform (STFT).

    :param sig: input 1D NumPy array representing the audio waveform
    :param sr: sampling rate (Hz)
    :param win_len: window length in seconds
    :param frame_len: frame step in seconds
    :param window_fn: window function generator, such as np.hamming
    :return:
    ;param spec: 2D NumPy array of shape (num_freq_bins, num_frames) — the magnitude of the DFT in dB
    ;param t: 1D array of time stamps for each frame
    ;param f: 1D array of frequency stamps
    '''
    
    # Convert window and frames from sec to sample
    win_len_samples = int(win_len * sr)
    frame_len_samples = int(frame_len * sr)
    
    # Create window 
    window = window_fn(win_len_samples)
    
    # Calculate next power of 2 for zero-padding FFT
    fft_size = 2 ** math.ceil(math.log2(win_len_samples))
    
    # Pad signal for enough samples for last window
    padded_sig = np.pad(sig, (0, win_len_samples), mode='constant')
    
    # Calculate frames
    num_frames = 1 + (len(padded_sig) - win_len_samples) // frame_len_samples
    
    # Initialize spectrogramm matrix
    num_freq_bins = fft_size // 2 + 1
    spec = np.zeros((num_freq_bins, num_frames))
    
    # Compute DFT for frame
    for i in range(num_frames):
        start = i * frame_len_samples
        end = start + win_len_samples
        
        # Extract frame and apply window
        frame = padded_sig[start:end] * window
        
        # Zero-pad to FFT size and compute FFT
        padded_frame = np.pad(frame, (0, fft_size - win_len_samples), mode='constant')
        dft = np.fft.rfft(padded_frame)
        
        # Store magnitude spectrum in decibels
        spec[:, i] = 20 * np.log10(np.abs(dft) + 1e-10)  # Add small value to avoid log(0)
    
    # Create time & frequency axes
    t = np.arange(num_frames) * frame_len
    f = np.fft.rfftfreq(fft_size, d=1/sr)
    
    return spec, t, f

if __name__ == "__main__":

    ### Read the sound file
    sig, sr = sf.read("sample.wav")

    ### Plot the spectrogram
    spec, t, f = spectrogram(sig, sr, win_len=0.025, frame_len=0.01, window_fn=np.hamming)
    plt.figure(figsize=(16, 10))
    plt.imshow(20 * np.log10(np.abs(spec) + 1e-10), aspect='auto', origin='lower', extent=[t[0], t[-1], f[0], f[300]])
    plt.title("Spectrogram with Hamming window)")
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [Hz]")
    plt.colorbar(label="Magnitude [dB]")