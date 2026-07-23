import numpy as np
from scipy import signal

x = np.array([2, 3, 1, 0, 4, 5, 3, 2], dtype=float)

f, Pxx = signal.welch(x,fs=8.0,window='hann',nperseg=4, noverlap=2, nfft=4,detrend=False,return_onesided = True,scaling='density',average='mean')

print(Pxx)
""" output : [2.52083333 2.04166667 0.07638889]"""
