from scipy.fft import fft, fftfreq, fftshift
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

def FFTdata_spectr_freq(signal, samplerate):
    spectr = fftshift(fft(signal))         # сдвигает нулевую частоту в центр массива
    freq = fftshift(fftfreq(len(signal), 1./samplerate)) # нулевая частота помещается в центра, И расчитываются все частоты
    return spectr, freq

def obrezanie(signal, frequency):
    s,f =  signal[len(signal)//2:], frequency[len(frequency)//2:]
    return s[(f<3000) & (f>100)], f[(f<3000) & (f>100)]

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    QtWidgets.QApplication(sys.argv)

    FILE = "./test_sound/dron-vzletaet-i-uletaet.wav"

    samplerate, data = wavfile.read(FILE)
    # plt.plot(np.linspace(0,1, len(data)), data)
    # plt.show()
    # print(data.shape)
    # # отрисовка спектра
    data0 = data[:, 0]
    data1 = data[:, 1]
    spectr, freq = FFTdata_spectr_freq(data0, samplerate)
    spectr, freq = obrezanie(spectr, freq)
    #plt.plot(freq, spectr.imag)
    #plt.show()
    print(spectr)
    print(freq)