import cmath, math
import numpy as np
import matplotlib.pyplot as plt

def FFT(x):
    N = len(x)
    if N <= 1:
        return x
    
    even = FFT(x[0::2])
    odd = FFT(x[1::2])

    combined = [0] * N

    for k in range(N//2):
        twiddle = cmath.exp(-2j*math.pi*k/N)
        combined[k] = even[k] + odd[k] * twiddle
        combined[k+N//2] = even[k] - odd[k] * twiddle
    
    return combined

def next_power2(n):
    return 1 << (n-1).bit_length()


fs = 8000
T = 1.0
t = np.linspace(0, T, int(fs*T), endpoint=False)

x = 3*np.sin(2*np.pi*100*t) + 2*np.sin(2*np.pi*1000*t) + 10*np.sin(2*np.pi*2400*t) + 6*np.sin(2*np.pi*3900*t)
x = x - np.mean(x)
x = x*np.hanning(len(x))

N = len(x)
M = next_power2(N)
x_pad = np.zeros(M)
x_pad[:N] = x

X = FFT(x_pad)
freqs = np.fft.fftfreq(M, 1/fs)
half = M//2

# # x = 3*np.sin(2*np.pi*100*t)

# X = FFT(x)
# freqs = np.fft.fftfreq(len(x), 1/fs)
# half = len(x)//2

plt.plot(freqs[:half], np.abs(X[:half])/M)
plt.show()