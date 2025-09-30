# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:23:45 2025

@author: taylosh

Programming HW2: LTI Systems and Convolution
"""
import numpy as np
import soundfile as sf

def convolve(x, h):
    """
    Implement convolution.
    :param x: Input signal (numpy array)
    :param h: System impulse response (numpy array)
    :return: Full convolution (numpy array)
    """
    # Lengths of the input signals
    len_x = len(x)
    len_h = len(h)
    
    # Length of the output signal
    len_y = len_x + len_h - 1
    
    # Initialize the output signal
    y = np.zeros(len_y)
    
    # Perform convolution
    for i in range(len_x):
        y[i:i + len_h] += x[i] * h  # Vectorized operation
    
    return y

if __name__ == "__main__":
    # Load the glottal excitation signal and vocal tract impulse responses
    excitation, fs = sf.read("vowel/excitation.wav")
    vocal_tract_a, _ = sf.read("vowel/IR_a.wav")
    vocal_tract_i, _ = sf.read("vowel/IR_i.wav")
    vocal_tract_u, _ = sf.read("vowel/IR_u.wav")
    
    # Synthesize vowel sounds by convolution
    synthesized_a = convolve(excitation, vocal_tract_a)
    synthesized_i = convolve(excitation, vocal_tract_i)
    synthesized_u = convolve(excitation, vocal_tract_u)
    
    # Normalize output signals to avoid clipping
    synthesized_a = synthesized_a / np.max(np.abs(synthesized_a))
    synthesized_i = synthesized_i / np.max(np.abs(synthesized_i))
    synthesized_u = synthesized_u / np.max(np.abs(synthesized_u))
    
    # Save synthesized vowel sounds
    sf.write("synthesized_a.wav", synthesized_a, fs)
    sf.write("synthesized_i.wav", synthesized_i, fs)
    sf.write("synthesized_u.wav", synthesized_u, fs)
    
    # Load the anechoic speech and room impulse responses
    anechoic_speech, fs_speech = sf.read("reverb/speech.wav")
    room_response_01, _ = sf.read("reverb/RIR_1.wav")
    room_response_02, _ = sf.read("reverb/RIR_2.wav")
    
    # Apply reverberation effect by convolution
    reverbed_01 = convolve(anechoic_speech, room_response_01)
    reverbed_02 = convolve(anechoic_speech, room_response_02)
    
    # Normalize output signals to avoid clipping
    reverbed_01 = reverbed_01 / np.max(np.abs(reverbed_01))
    reverbed_02 = reverbed_02 / np.max(np.abs(reverbed_02))
    
    # Save reverberated speech
    sf.write("reverbed_01.wav", reverbed_01, fs_speech)
    sf.write("reverbed_02.wav", reverbed_02, fs_speech)