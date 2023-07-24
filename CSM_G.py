
import numpy as np


class G:
    """
    A deconvolution approach for the mapping of acoustic sources (DAMAS) determined from phased microphone arrays
    формула 1 - но сразу с diag == 0 во избежание самокорреляции. Матрица Эрмитова. Для упрощения я не провожу
    суммирования по небольшим промежуткам времени, а считаю КросСпектральнуюМатрицу тупо на одном временном про
    межутке. В класс просто подается массив фурье с микрофонофонов (обрезание до нужного будет ВНЕ этого класса
    это просто класс работяга). На выходе будет объект, к которому можно обращаться и для заданной частоты
    (надо бы ее сделать дискретной) выдает матрицу CSM.

    TODO: надо чтобы подавалась дискретная частота, а не индекс, нужна А) целочисленная частота Б) перевод
    TODO: частоты в индекс
    """
    def __init__(self, *microphones_fouriers) -> None:
        L = len(microphones_fouriers)
        self.L = L
        self.G = [[0 for i in range(L)] for i in range(L)]#np.zeros((L,L))
        self.fouries = microphones_fouriers
        self.make_G_matrix()

    def make_G_matrix(self):
        L = len(self.fouries)
        for i in range(L):
            for j in range(L):
                if i == j: self.G[i][j] = 0#G[i,j] = 0
                else:
                    self.G[i][j] = np.conjugate(self.fouries[i])*self.fouries[j]

    def __call__(self, frequence_index : int):
        """

        :param frequence_index: индекс частоты
        :return:

        NB -- принимает не частоту а ее ИНДЕКС
        """
        L = self.L
        resultG = [[0 for i in range(L)] for i in range(L)]
        for i in range(L):
            for j in range(L):
                if i == j: resultG[i][j] = 0#G[i,j] = 0
                else:
                    resultG[i][j] = (np.conjugate(self.fouries[i])*self.fouries[j])[frequence_index]
        resultG = np.array(resultG,dtype=object)
        return resultG

if __name__ == "__main__":
    p1 = np.array([1+1j, 2+2j, 3+3j])
    p2 = np.array([10+10j, 20+2j, 30+30j])
    _G_ = G(p1,p2)
    print(_G_.G, "\n")
    print(_G_(1))
    print(type(_G_(0)))
    print(_G_(0).shape)

    right_col_vector = np.array([[10],[20]])
    print(right_col_vector)
    print(_G_(1)@right_col_vector)


if __name__ == "__main__" and 0:
    import matplotlib.pyplot as plt

    # чтобы plt работало

    #отрисовка сигнала


