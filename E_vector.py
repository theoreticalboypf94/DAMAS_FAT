"""
A deconvolution approach for the mapping of acoustic sources (DAMAS) determined from phased microphone arrays
У мужиков этот вектор значится как "направляющий" или "смещающий" вводится формулой (3) и (4) содержит в себе
связь с геометрией реального мира, и как я понимаю, формирует что то вроде ортогонального базиса, котороый
потом будет подсунут в метод Зейделя. Нам надо использовать Grid.py чтобы знать узлы сетки и положения микрофонов


Grid.py ----> E_vector.py ----> Y_number.py
                            ^
              CSM_G.py  ----|
"""


from Grid import *
from Physic import *
import numpy as np

class E:
    """
        реализация (3) вектор связывающий n-й узел со всеми m микрофонами
        Принимает номер узла
        Параметры сетки
        Координаты микрофона
    """
    def __init__(self,
                 number_of_nodes: int, coordinat_of_center_node: np.array, node_dx: float, node_dy: float,
                 microphones: np.array
                 ):

        self.grid = Grid(number_of_nodes, coordinat_of_center_node, node_dx, node_dy)
        self.microphones = microphones

    def __call__(self, n, frequency):
        """
            Выдает вектор столбец направляющих функций для данного узла n для данной частоты frequency
            n - номер узла
            frequency - частота в герцах
        """
        node = self.grid(n)
        m0 = len(self.microphones)
        micro = self.microphones
        e_n = []
        for i in range(m0):
            node_minus_ith_microphone = node - micro[i]
            distance = np.linalg.norm(node_minus_ith_microphone)
            time_i = distance / v_c                         # время достижения сигнала
            e_i = 1./distance * np.exp(1.j*2*np.pi*frequency*time_i)
            e_n.append([e_i])
        return np.array(e_n, dtype=object)

if __name__ == "__main__":
    e = E(11*11, np.array([0,0, 5]), 0.5, 0.5,
          [np.array([0.25,0.25,0]), np.array([-.25,.25,0])])
    print(e(20, 1000))
    vec = e(20,1000)
    print(vec.shape)
    print(vec.conj().T)
    print(vec.shape)
    print(vec.T)