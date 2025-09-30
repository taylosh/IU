# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 09:57:44 2025

@author: taylosh

Programming HW4: Ideal Filters
Apply ideal low-pass, high-pass, and band-pass filters to a violin signal using time-domain convolution.
"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

# ======== Filter Design Functions ========
def get_hn_lp(omega_c, len_h):
    """
    Generate lowpass filter impulse response h[n] using sinc function.
    :param omega_c: Cutoff frequency in radians/sample
    :param len_h: Filter length
    :return: Lowpass filter h[n]
    """
    n = np.arange(len_h)
    middle = len_h // 2
    n_shifted = n - middle
    h_lp = omega_c / np.pi * np.sinc((omega_c / np.pi) * n_shifted)
    return h_lp

def get_hn_hp(omega_c, len_h):
    """
    Generate highpass filter h[n] via h_lp.
    """
    # HPF = delta[n] - LPF
    delta = np.zeros(len_h)
    delta[len_h//2] = 1  # centered impulse
    return delta - get_hn_lp(omega_c, len_h)

def get_hn_bp(omega_c1, omega_c2, len_h):
    """
    Generate band-pass filter h[n] as difference of two lowpass filters.
    """
    # BPF = LPF(omega_c2) - LPF(omega_c1)
    return get_hn_lp(omega_c2, len_h) - get_hn_lp(omega_c1, len_h)

# ======== Spectrum Plotting Function using np.fft ========
def plot_spectrum(signal, fs, title):
    """
    Plot frequency spectrum using FFT
    :param signal: Input signal
    :param fs: Sampling frequency
    :param title: Plot title
    """
    N = len(signal)
    freq = np.fft.rfftfreq(N, d=1/fs)
    spectrum = np.abs(np.fft.rfft(signal))
    
    plt.figure(figsize=(12, 6))
    plt.plot(freq, spectrum)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title(title)
    plt.grid(True)
    plt.xlim(0, fs/2)
    plt.show()

# ======== Main Script ========
if __name__ == "__main__":
    # ---- Load the violin audio file ----
    filename = 'note_violin.wav'
    signal, fs = sf.read(filename)  # shape: (N,)

    # ---- Filter parameters ----
    len_h = 2 * len(signal) + 1  # Long filter for better frequency resolution

    # Define cutoff frequencies in Hz
    f_lp = 1000       # for low-pass
    f_hp = 3000       # for high-pass
    f_bp1 = 2000      # lower bound for band-pass
    f_bp2 = 6000      # upper bound for band-pass

    # Convert to radians/sample
    omega_lp = 2 * np.pi * f_lp / fs
    omega_hp = 2 * np.pi * f_hp / fs
    omega_bp1 = 2 * np.pi * f_bp1 / fs
    omega_bp2 = 2 * np.pi * f_bp2 / fs

    # ---- Design Filters ----
    h_lp = get_hn_lp(omega_lp, len_h)
    h_hp = get_hn_hp(omega_hp, len_h)
    h_bp = get_hn_bp(omega_bp1, omega_bp2, len_h)

    # ---- Apply Filters via Convolution fftconvolve ----
    y_lp = fftconvolve(signal, h_lp, mode='same')
    y_hp = fftconvolve(signal, h_hp, mode='same')
    y_bp = fftconvolve(signal, h_bp, mode='same')

    # ---- Plot Spectra ----
    plot_spectrum(signal, fs, 'Original Violin Spectrum')
    plot_spectrum(y_lp, fs, 'Low-Pass Filtered (f < 1000 Hz)')
    plot_spectrum(y_hp, fs, 'High-Pass Filtered (f > 3000 Hz)')
    plot_spectrum(y_bp, fs, 'Band-Pass Filtered (2000-6000 Hz)')

    # ---- Save filtered audio ----
    sf.write('violin_lowpass.wav', y_lp, fs)
    sf.write('violin_highpass.wav', y_hp, fs)
    sf.write('violin_bandpass.wav', y_bp, fs)

    # Add observations
    observations = """
    Filter Effects Analysis:
    1. Low-Pass Filter (1000 Hz cutoff):
       - Preserves the fundamental and lower harmonics
       - Result sounds warmer but loses brightness
       - Spectrum shows removal of frequencies above 1kHz
    
    2. High-Pass Filter (3000 Hz cutoff):
       - Removes fundamental and lower harmonics
       - Result sounds thin and airy with only high overtones
       - Spectrum shows elimination of frequencies below 3kHz
    
    3. Band-Pass Filter (2000-6000 Hz):
       - Isolates the mid-range harmonic content
       - Result has a nasal, focused quality
       - Spectrum shows passband between 2-6kHz with attenuation outside
    """
    
    with open("filter_observations.txt", "w") as f:
        f.write(observations)