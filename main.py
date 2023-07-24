"""

Перевод из частоты в индекс частоты
            FFT_data.py
             |
             |
            \|
(ПРАВАЯ ЧАСТЬ СЛАУ)
Grid.py ----> E_vector.py ----> Y_number.py ----------> |
                            ^                           |
              CSM_G.py  ----|                           |
                                                        | ------> Seidel.py  ---> полученное решение  --> вычислитель координат
(ЛЕВАЯ ЧАСТЬ СЛАУ)                                      |                                |
A_n1n2_coefficients.py      ------------------------->  |                                |
                                                                                         |
                                                                                        \/
Visualization.py -----------------------------------------------------------------------------> картинки

"""

from Visualization import *
from FFT_data import *
from Y_number import *
from A_n1n2_coefficients import *
from Seidel import Seidel
from Visualization import plot_intensity_on_grid
#
from tqdm import tqdm
import sys
from PyQt5 import QtWidgets
QtWidgets.QApplication(sys.argv)

FILE = "./test_sound/dron-vzletaet-i-uletaet.wav"

samplerate, data = wavfile.read(FILE)
# # отрисовка спектра
data0 = data[:, 0]
data1 = data[:, 1]

spectr0, freq = FFTdata_spectr_freq(data0, samplerate)
spectr0, freq = obrezanie(spectr0, freq)

spectr1, freq = FFTdata_spectr_freq(data1, samplerate)
spectr1, freq = obrezanie(spectr1, freq)

Grid_size = 21*21

Yn = Y_number(
                Grid_size, np.array([0,0, 5]), 0.5, 0.5,[np.array([0.25,0.25,0]), np.array([-.25,.25,0])],
                spectr0,spectr1
            )

# Формирую правую часть СЛАУ
right = []
FREQ_INDEX = 321
N = Grid_size
for i in range(N):
    print(freq[FREQ_INDEX])
    right.append(Yn(i, freq[FREQ_INDEX],FREQ_INDEX))
right = np.array(right)
#print(right)

matr = []
row = []
_An1n2_ = An1n2(
    Grid_size, np.array([0,0, 5]), 0.5, 0.5,[np.array([0.25,0.25,0]), np.array([-.25,.25,0])]
)

print("Calculate matrix element to SLAU:\n")
for n in tqdm(range(N)):
    for sum_index in range(N):
        row.append(_An1n2_(n, sum_index,freq[FREQ_INDEX]))
    matr.append(row)
    row = []
A = np.array(matr, dtype=object)

print("Seidel compute solution:\n")
solution = Seidel(A,right)
plot_intensity_on_grid(solution)
