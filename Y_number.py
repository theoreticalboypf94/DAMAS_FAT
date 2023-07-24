from CSM_G import *
from E_vector import *

class Y_number:
    def __init__(self,
                 number_of_nodes: int, coordinat_of_center_node: np.array, node_dx: float, node_dy: float,
                 microphones: np.array,
                 *microphones_fouriers
                 ):
        self.m0 = len(microphones)
        self._E_ = E(number_of_nodes, coordinat_of_center_node, node_dx, node_dy, microphones)
        self._G_ = G(*microphones_fouriers)

    def __call__(self, n, frequency, frequency_index):
        """

        :param n:   номер узла
        :param frequency: частота в герцах
        :return:
        """
        vec_col_e = self._E_(n, frequency)                          # вектор столбец будет справа
        vec_row_e = vec_col_e.conj().T                              # вектор строка будет слева
        mat_G = self._G_(frequency_index)                           # принимает не частоту, а частотный индекс
        denuminator = self.m0**2 - self.m0
        Y_n_f = vec_row_e @ (mat_G @ vec_col_e)
        Y_n_f = Y_n_f/denuminator
        #return Y_n_f  # надо бы выделить реальную часть
        return Y_n_f[0][0].real  # надо бы выделить реальную часть


if __name__ == "__main__":
    p1 = np.array([1 + 1j, 2 + 2j, 3 + 3j])
    p2 = np.array([10 + 10j, 20 + 2j, 30 + 30j])

    Yn = Y_number(
                    11*11, np.array([0,0, 5]), 0.5, 0.5,[np.array([0.25,0.25,0]), np.array([-.25,.25,0])],
                    p1, p2
                  )
    print((Yn(19,1)))
    # print((Yn(19,1).shape))
    # print(type(Yn(19,1)[0][0]))
    # print((Yn(19,1)[0][0]).real)