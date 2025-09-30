"""
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
    pass

def get_hn_bp(omega_c1, omega_c2, len_h):
    """
    Generate band-pass filter h[n] as difference of two lowpass filters.
    """
    pass

# ======== Spectrum Plotting Function using np.fft ========
def plot_spectrum():
    pass

# ======== Main Script ========
if __name__ == "__main__":
    # ---- Load the violin audio file ----
    filename = 'note_violin.wav'
    signal, fs = sf.read(filename)  # shape: (N,)


    # ---- Filter parameters ----
    len_h = 2 * len(signal) + 1

    # Define cutoff frequencies in Hz
    f_lp = 1000       # for low-pass
    f_hp = 3000       # for high-pass
    f_bp1 = 2000      # lower bound for band-pass
    f_bp2 = 6000      # upper bound for band-pass

    # Convert to radians/sample
    omega_lp = ...
    omega_hp = ...
    omega_bp1 = ...
    omega_bp2 = ...

    # ---- Design Filters ----
    h_lp = ...
    h_hp = ...
    h_bp = ...

    # ---- Apply Filters via Convolution fftconvolve----
    y_lp = ...
    y_hp = ...
    y_bp = ...

    # ---- Plot Spectra ----


    # ---- Save filtered audio ----
