# from audio_wave import fs, data
from radix2_iterative_fft import fft_iterative, next_power2

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

fs, data = wavfile.read('star_wars_intro.wav')

if len(data.shape) == 2:
    data = data[:,0]

print(f"Sample Rate: {fs} Hz")
print(f"Number of samples: {len(data)}")


T = 1
samples = int(fs * T)
t = np.linspace(0, T, samples, endpoint=False)


x = data[:samples]
x = x - np.mean(x)
x = x*np.hanning(len(x))

N = len(x)
M = next_power2(N)
x_pad = np.zeros(M)
x_pad[:N] = x

X = fft_iterative(x_pad)
freqs = np.fft.fftfreq(M, 1/fs)
half = M//2

# plt.plot(freqs[:half], np.abs(X[:half])/M)
plt.plot(freqs[:half], np.abs(X[:half]) / np.max(np.abs(X)))
plt.title("FFT Spectrum of Star Wars Intro")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Normalized Magnitude")
plt.show()