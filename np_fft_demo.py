import numpy as np
import matplotlib.pyplot as plt

#set sampling rate (hz)
fs = 8000
T = 1.0
t = np.linspace(0, T, int(fs*T), endpoint=False)

x = 3*np.sin(2*np.pi*100*t) + 2*np.sin(2*np.pi*1000*t) + 10*np.sin(2*np.pi*2400*t) + 6*np.sin(2*np.pi*3900*t)

N=len(x)
X=np.fft.fft(x)
freqs = np.fft.fftfreq(N, 1/fs)

half = N//2
plt.plot(freqs[:half], np.abs(X[:half])/N)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|X(f)|")
plt.show()

# plt.plot(t[:400], x[:400])
# plt.title("Time domain signal")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.show()