#!/usr/bin/env python3
"""
Programming HW3: Spectrum Representations (Discrete Fourier Transform)
"""
import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    """
    Implement DFT using the given formula:
    :param x: discrete-time signal
    :return: Phasor representation X
    """
    X = np.zeros(len(x), dtype=complex)

    ### Start your implementation here

    return X



if __name__ == "__main__":

    # Signal parameters
    fs = 1000  # Sampling frequency (Hz)
    t = np.arange(0, 1, 1 / fs)  # Time array for 1 second
    f1 = 50  # Frequency of first sine wave (Hz)
    f2 = 120  # Frequency of second sine wave (Hz)

    # Generate the signal: sum of two sine functions
    x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Compute the DFT of the signal
    X = dft(x)

    # Frequency bins
    N = len(x)
    freq = np.arange(N) * fs / N

    # Plot the magnitude spectrum (showing only the positive frequencies)
    plt.figure(figsize=(12, 6))
    plt.stem(freq[:N // 2], np.abs(X[:N // 2]) / N, basefmt=" ", use_line_collection=True)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('DFT Magnitude Spectrum')
    plt.grid(True)
    plt.show()