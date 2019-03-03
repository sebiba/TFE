import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import random

fs = 2400  # sample rate


def initsignal(frequence, t1, t2):
    t = np.linspace(t1, t2, fs)
    # compute the value (amplitude) of the sin wave at the for each sample
    return np.sin(frequence * 2 * np.pi * t)


def correlation(signal):
    result = np.correlate(signal, signal, mode='full')
    signal = result[result.size // 2:]

    # plt.stem(x,y, 'r', )
    plt.plot(signal[:600])
    plt.show()
    return signal


def frequence(signal):
    X = fftpack.fft(signal)
    freqs = fftpack.fftfreq(len(signal)) * fs

    plt.stem(freqs, np.abs(X))
    plt.xlabel('Frequency in Hertz [Hz]')
    plt.ylabel('Frequency Domain (Spectrum) Magnitude')
    plt.xlim(-1000, 1000)
    plt.show()

    return freqs[np.where(np.abs(X) == np.max(np.abs(X)))[0][0]] + 1


y = np.append(initsignal(220, 0, 1), initsignal(440, 1, 2))
# y = initsignal(220, 0, 1)
test = np.array_split(y, len(y)/500)
for i in range(len(test)):
    y1 = derange(test[i])
    y2 = correlation(y1)
    print(str(i) + ":\t" + str(frequence(y2)))
