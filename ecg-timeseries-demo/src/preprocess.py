
import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(x, fs=250, low=0.5, high=40):
    ny = 0.5 * fs
    lowcut = low / ny
    highcut = high / ny
    b, a = butter(3, [lowcut, highcut], btype='band')
    y = filtfilt(b, a, x)
    return y
