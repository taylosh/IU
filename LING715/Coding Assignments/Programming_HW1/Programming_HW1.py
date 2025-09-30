#!/usr/bin/env python3
"""
Programming HW1: Sampling and Quantization
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def continuous_signal(A, f, dur, phi, psudo_fs):
    """
    Generate a psudo continuous signal with the given parameters.
    :param A: Amplitude
    :param f: frequency of the constinuous signal
    :param dur: duration of the signal in seconds
    :param phi: phase of the signal
    :param psudo_fs: sampling frequency to get the pseduo continuous signal
    :return: a continuous signal with the specified parameters
    """

    pass


def sample_signal(fs, *args):
    """
    Sample a continuous signal with the given sampling rate fs
    :param fs: the sampling rate
    :param args: any additional arguments you think should be included when sampling a signal
    :return: sampled signal
    """

    pass

def quantize_signal(num_levels, *args):
    """
    Quantize a sampled signal with a given number of levels using mid-thread quantizer.
    :param num_levels: the number of quantization levels
    :param args: any additional arguments you think should be included when quantize a signal
    :return: quantized signal, and RMS of the quantization error
    """

    pass

if __name__=="__main__":

    ##### Parameters for the continuous signal
    A = 2
    f = 20
    dur = 2 #seconds
    phi = 0
    psudo_fs = 1000 # samples/seconds

    ### Parameters for sampling
    fs1 = 100
    fs2 = 30
    fs3 = 5


    ### Parameters for quantization
    num_levels1= 4
    num_levels2 = 8
    num_levels3 = 9


    ### Code for plots

    # Question: What are the primary aliases of the sampled signals?