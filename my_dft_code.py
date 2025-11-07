import numpy as np
import math
import cmath

def DFT(x):
    N = len(x)
    X = []

    for k in range(N):
        s=0
        for n in range(N):
            power = -2j * math.pi * k * n/N
            s += x[n] * cmath.exp(power)

        X.append(s)
    return np.array(X)

fs = 8000
T = 1.0
t = np.linspace(0, T, int(fs*T), endpoint=False)

x = 3*np.sin(2*np.pi*100*t) + 2*np.sin(2*np.pi*1000*t) + 10*np.sin(2*np.pi*2400*t) + 6*np.sin(2*np.pi*3900*t)
# x = 3*np.sin(2*np.pi*100*t)

X = DFT(x)

freqs = np.fft.fftfreq(len(x), 1/fs)

import matplotlib.pyplot as plt
half = len(x)//2
plt.plot(freqs[:half], np.abs(X[:half])/len(x))
plt.show()