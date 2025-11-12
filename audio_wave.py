import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, data = wavfile.read('star_wars_intro.wav')

if len(data.shape) == 2:
    data = data[:,0]

print(f"Sample Rate: {fs} Hz")
print(f"Number of samples: {len(data)}")

T = 0.1
N = int(T*fs)
t = np.arange(N) / fs

plt.plot(t, data[:N])
plt.title("Time-Domain Waveform")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()