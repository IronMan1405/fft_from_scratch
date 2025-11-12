import cmath, math
import numpy as np
import matplotlib.pyplot as plt

def fft_iterative(x):
    N = len(x)
    levels = int(math.log2(N))
    assert 2**levels == N, "Length must be power of 2"

    # 1. Bit-reversal permutation
    def bit_reverse(n, bits):
        rev = 0
        for i in range(bits):
            if (n >> i) & 1:
                rev |= 1 << (bits - 1 - i)
        return rev

    X = [0]*N
    for i in range(N):
        X[bit_reverse(i, levels)] = x[i]

    # 2. Iterative butterfly stages
    size = 2
    while size <= N:
        half_size = size // 2
        table_step = N // size
        for i in range(0, N, size):
            for k in range(half_size):
                twiddle = cmath.exp(-2j*math.pi*k/size)
                t = twiddle * X[i + k + half_size]
                X[i + k + half_size] = X[i + k] - t
                X[i + k] = X[i + k] + t
        size *= 2
    return X

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

X = fft_iterative(x_pad)
freqs = np.fft.fftfreq(M, 1/fs)
half = M//2

plt.plot(freqs[:half], np.abs(X[:half])/M)
plt.show()