# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 09:57:44 2025

@author: taylosh

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
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))  # Reshape k to column vector
    e = np.exp(-2j * np.pi * k * n / N)  # Compute exponential term
    # I changed this to matrix multiplication to compute DFT; the nested loop took a very long time
    X = np.dot(e, x)  
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
    plt.stem(freq[:N // 2], np.abs(X[:N // 2]) / N, basefmt=" ")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('DFT Magnitude Spectrum')
    plt.grid(True)
    plt.show()
    
    
# Save observations to a .txt file
observations = """
Observations on the Impact of Sampling Frequency (fs) on DFT Output:
The sampling frequency (fs) majorly influences the DFT output. At fs = 
1000 Hz, the frequency resolution is 1 Hz, and the Nyquist frequency is 500 Hz. 
The DFT clearly shows peaks at 50 Hz and 120 Hz, matching the input signal's 
frequencies. Increasing fs to 2000 Hz improves the resolution to 0.5 Hz and 
raises the Nyquist frequency to 1000 Hz, resulting in sharper, more distinct 
peaks. Conversely, reducing fs to 500 Hz lowers the resolution to 2 Hz and the 
Nyquist frequency to 250 Hz, making the peaks broader and less distinct. When fs 
is set too low (e.g., 200 Hz), the Nyquist frequency drops to 100 Hz, causing 
the 120 Hz component to alias and appear at 80 Hz. This demonstrates the 
trade-off between resolution, Nyquist frequency, and the risk of aliasing when 
choosing fs.
"""

with open("Shane_Taylor_Programming_HW3.txt", "w") as file:
    file.write(observations)