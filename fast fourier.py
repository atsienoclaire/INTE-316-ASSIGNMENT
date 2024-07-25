import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f1 = 50  # Frequency of the first signal
f2 = 120 # Frequency of the second signal
fs = 1000 # Sampling frequency
t = np.arange(0, 1, 1/fs) # Time vector

# Signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute FFT
S = np.fft.fft(s)
freq = np.fft.fftfreq(len(S), 1/fs)

# Plot the frequency components
plt.plot(freq[:len(freq)//2], np.abs(S)[:len(S)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Components')
plt.show()
