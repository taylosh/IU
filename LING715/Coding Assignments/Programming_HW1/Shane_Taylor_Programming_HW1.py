# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:23:45 2025

@author: taylosh

Programming HW1: Sampling and Quantization
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def continuous_signal(A, f, dur, phi, psudo_fs):
    """
    Generate a pseudo-continuous signal with the given parameters.
    :param A: Amplitude
    :param f: frequency of the continuous signal
    :param dur: duration of the signal in seconds
    :param phi: phase of the signal
    :param psudo_fs: sampling frequency to get the pseudo-continuous signal
    :return: a continuous signal with the specified parameters
    """
    t = np.linspace(0, dur, int(psudo_fs * dur), endpoint=False)  # Time vector
    signal = A * np.sin(2 * np.pi * f * t + phi)  # Sinusoidal signal with amplitude A and phase phi
    return t, signal

def sample_signal(fs, t_continuous, signal_continuous, psudo_fs):
    """
    Sample a continuous signal with the given sampling rate fs.
    :param fs: the sampling rate
    :param t_continuous: time vector of the continuous signal
    :param signal_continuous: continuous signal
    :param psudo_fs: pseudo-continuous sampling frequency to compute the sampling indices
    :return: sampled time vector, sampled signal
    """
    # Ensure the step size is a valid integer
    step_size = max(1, round(psudo_fs / fs))  # Rounds to nearest integer, prevents zero or negative steps

    # Select indices corresponding to sampling times
    sample_indices = np.arange(0, len(t_continuous), step_size)

    # Ensure we do not go out of bounds
    sample_indices = sample_indices[sample_indices < len(t_continuous)]

    sampled_signal = signal_continuous[sample_indices]
    sampled_t = t_continuous[sample_indices]

    return sampled_t, sampled_signal


def quantize_signal(num_levels, sampled_signal):
    """
    Quantize a sampled signal with a given number of levels using a mid-tread quantizer.
    :param num_levels: the number of quantization levels
    :param sampled_signal: the sampled signal to be quantized
    :return: quantized signal, and RMS of the quantization error
    """
    # Define quantization step size
    min_val, max_val = np.min(sampled_signal), np.max(sampled_signal)
    step_size = (max_val - min_val) / num_levels

    # Apply mid-tread quantization
    quantized_signal = np.round(sampled_signal / step_size) * step_size

    # Compute RMS error
    quantization_error = sampled_signal - quantized_signal
    rms_error = np.sqrt(np.mean(quantization_error ** 2))

    return quantized_signal, rms_error

if __name__=="__main__":

    ##### Parameters for the continuous signal
    A = 2
    f = 20  # Frequency in Hz
    dur = 2  # Duration in seconds
    phi = 0  # Phase shift
    psudo_fs = 1000  # Pseudo-continuous sampling frequency (samples per second)

    ### Parameters for sampling
    fs1 = 100  # Sampling frequency 1
    fs2 = 30   # Sampling frequency 2
    fs3 = 5    # Sampling frequency 3

    ### Parameters for quantization
    num_levels1 = 4
    num_levels2 = 8
    num_levels3 = 9

    # Generate continuous signal
    t_continuous, signal_continuous = continuous_signal(A, f, dur, phi, psudo_fs)

    # Sample signals at different frequencies
    sampled_t1, sampled_signal1 = sample_signal(fs1, t_continuous, signal_continuous, psudo_fs)
    sampled_t2, sampled_signal2 = sample_signal(fs2, t_continuous, signal_continuous, psudo_fs)
    sampled_t3, sampled_signal3 = sample_signal(fs3, t_continuous, signal_continuous, psudo_fs)

    # Quantize signals
    quantized_signal1, rms_error1 = quantize_signal(num_levels1, sampled_signal1)
    quantized_signal2, rms_error2 = quantize_signal(num_levels2, sampled_signal2)
    quantized_signal3, rms_error3 = quantize_signal(num_levels3, sampled_signal3)

    # Plot the continuous and sampled signals
    # Create subplots   
    plt.figure(figsize=(10, 8))

    # Plot continuous signal
    plt.subplot(4, 1, 1)  # 4 rows, 1 column, 1st plot
    plt.plot(t_continuous, signal_continuous, label="Continuous Signal", linestyle='-', color='b')
    plt.title("Continuous Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    # Plot sampled signal at fs1
    plt.subplot(4, 1, 2)  # 4 rows, 1 column, 2nd plot
    plt.stem(sampled_t1, sampled_signal1, markerfmt='o', basefmt=" ")
    plt.title(f"Sampled Signal (fs={fs1} Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Plot sampled signal at fs2
    plt.subplot(4, 1, 3)  # 4 rows, 1 column, 3rd plot
    plt.stem(sampled_t2, sampled_signal2, markerfmt='x', basefmt=" ")
    plt.title(f"Sampled Signal (fs={fs2} Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Plot sampled signal at fs3
    plt.subplot(4, 1, 4)  # 4 rows, 1 column, 4th plot
    plt.stem(sampled_t3, sampled_signal3, markerfmt='^', basefmt=" ")
    plt.title(f"Sampled Signal (fs={fs3} Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Adjust layout for overlap
    plt.tight_layout()
    plt.show()


    # Answer to the question in the assignment
'''
The primary aliases of the sampled signals are those that fall within the Nyquist range [0,fs/2][0,fs​/2]. Aliasing occurs when the sampling frequency is lower than twice the original signal frequency, causing higher frequencies to fold back into this range.

    For fs=100fs​=100 Hz:
        The Nyquist limit is 5050 Hz. Since the original signal frequency is 2020 Hz (well below 5050 Hz), no aliasing occurs.

    For fs=30fs​=30 Hz:
        The Nyquist limit is 1515 Hz. Since 2020 Hz is greater than 1515 Hz, aliasing occurs.
        The alias frequency is calculated as:
        falias=∣20−1(30)∣=10 Hz
        falias​=∣20−1(30)∣=10 Hz
        This means the sampled signal behaves as if it were a 10 Hz sinusoid with an opposite phase.

    For fs=5fs​=5 Hz:
        The Nyquist limit is 2.52.5 Hz. Since 2020 Hz is much greater than 2.52.5 Hz, strong aliasing occurs.
        The alias frequency is:
        falias=∣20−round(20/5)×5∣=0 Hz
        falias​=∣20−round(20/5)×5∣=0 Hz
        This results in a signal that appears constant or oscillates extremely slowly, making it indistinguishable from a DC signal.

Thus, aliasing becomes more severe as the sampling frequency decreases, leading to misrepresentation of the original signal.
'''