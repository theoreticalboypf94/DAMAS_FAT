from CSM_G import *
from E_vector import *

class An1n2:
    """
    Класс вычисляющий коэффициенты в модельном восстановлении входящего сигнала в статье по формуле (20)
    """
    def __init__(self,
                 number_of_nodes: int, coordinat_of_center_node: np.array, node_dx: float, node_dy: float,
                 microphones: np.array
                 ):
        """

        :param number_of_nodes:             число узлов в сетке напралений
        :param coordinat_of_center_node:    координата центрального узла в сетке
        :param node_dx:                     шаг сетки по х
        :param node_dy:
        :param microphones:                 координаты микрофоноф
        """
        self.m0 = len(microphones)
        self._E_ = E(number_of_nodes, coordinat_of_center_node, node_dx, node_dy, microphones)

    def __call__(self, n1, n2, frequency):
        """

        :param n1:              главный индекс n
        :param n2:              безмолвный индекс суммирования n'
        :param frequency:       частота в герцах
        :return:
        """
        e1 = self._E_(n1, frequency)
        e2 = self._E_(n2, frequency)
        m0 = self.m0
        denuminator = m0**2 - m0
        _G_ = [[0 for i in range(self.m0)] for i in range(self.m0)]
        for i in range(m0):
            for j in range(m0):
                if i == j:
                    _G_[i][j] = 0  # G[i,j] = 0
                else:
                    _G_[i][j] = (np.conjugate(1./e1[i]) * 1./e1[j])[0]/denuminator

        vec_col_e = e2
        vec_row_e = vec_col_e.conj().T

        mat_G = np.array(_G_, dtype=object)
        A_n1n2 = vec_row_e @ (mat_G @ vec_col_e)
        return A_n1n2[0][0].real

if __name__ == "__main__":
    A = An1n2(
        11 * 11, np.array([0, 0, 5]), 0.5, 0.5, [np.array([0.25, 0.25, 0]), np.array([-.25, .25, 0])]
    )
    #print(A(3,13,300))
    mat = (A(3,11,300))                 #[[(0.36781006531243354-5.551115123125783e-17j)]]
    print(mat)
