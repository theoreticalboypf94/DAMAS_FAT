"""
Сетка будет плоская как у мужиков в статье - никакой кривизны, только плоскость
входной параметр это количество узлов - по оси Х и У - объект будет принимать
один аргумент - номер узла, начиная с 1 до N. Сетка- квадратная. Общет
змейкой снизу слева
16  15  14  13
9   10  11  12
8   7   6   5
1   2   3   4
для сетки 4 на 4.
"""

import numpy as np

class Grid:
    def __init__(self, N: int, R_centr: np.array, dx: float, dy: float) -> None:
        """

        :param N:   полное количество узлов - должно быть квадратом НЕЧЕТНОГО числа (так удобно)
        :param R_centr: координаты центрального узла, относительно НУЛЕВОЙ точки
        """
        self.N = N
        self.grid = [np.array([0,0,0]) for i in range(N)]
        self.R = R_centr
        self.dx = dx
        self.dy = dy
        self.width_height = int(np.sqrt(N))
        self.form_grid()

    def form_grid(self):
        """
                формирую сетку так что в центре будет координата R, а остальные - отступами от нее
        """
        x = 0
        y = 0
        x_order = 1

        # восходя змейкой снизу слева - вправо и вверх
        for y in range(0, self.width_height):
            if y%2 == 0:
                for x in range(0, self.width_height):
                    self.grid[y*self.width_height + x] = np.array([x*self.dx, y*self.dy, 0])
            else:
                for x in range(self.width_height-1, -1,-1):
                    self.grid[y*self.width_height + self.width_height-x-1] = np.array([x*self.dx, y*self.dy, 0])

        # теперь в центре у нас ноль
        center_number = self.N//2
        val = 1*self.grid[center_number]
        for i in range(0, self.N):
            self.grid[i] -= val

        # добавляем вектор смещения плоскости относительно 0
        for i in range(0, self.N):
            self.grid[i] += self.R

    def __call__(self, N):
        return self.grid[N]

if __name__ == "__main__":
    microphone_coordinates = [np.array([0.5,0.5,0]), np.array([-0.5, 0.5,0])]
    g = Grid(3*3, np.array([1,1,1]),1,1)
    print(g(3))