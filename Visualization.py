from Grid import *

import matplotlib.pyplot as plt

# чтобы plt работало
import sys
from PyQt5 import QtWidgets
QtWidgets.QApplication(sys.argv)

def plot_grid_and_microphones(N: int, R_centr: np.array, dx: float, dy: float,
                              *microphones):
    g = Grid(N, R_centr, dx, dy)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(0, 0, 0, marker="o", color="grey")

    for i in range(N):
        xs, ys, zs = g(i)
        ax.scatter(xs, ys, zs, marker="o",color="blue")

    for micro in microphones:
        xs, ys, zs = micro
        ax.scatter(xs, ys, zs, marker="o", color="red")
    ax.set_xlabel('X ')
    ax.set_ylabel('Y ')
    ax.set_zlabel('Z ')
    plt.show()

def plot_intensity_on_grid( SOLUTION: float):
    """
    g = Grid(N, R_centr, dx, dy)
    grid =
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(heatmap, interpolation='nearest')
    cbar = fig.colorbar(ax=ax, mappable=im, orientation='horizontal')
    """
    heatmap = []
    shape_x = int(np.sqrt(len(SOLUTION)))
    order = 1
    row = []
    counter = 0
    for i in range(len(SOLUTION)):
        if counter < shape_x:
            row.append(SOLUTION[i])

        else:
            counter = 0
            if order == 1:
                heatmap.append(row)
            else:
                #heatmap.append(row[::-1])
                heatmap.append(row)
            row = []
            row.append(SOLUTION[i])
            order *= -1
        counter += 1
    heatmap.append(row)         # очень по бичевому, но выбора у меня нет(  ОБЯЗАТЕЛЬНО БЛЯДЬ нечетное число узлов а то пизда
    fig, ax = plt.subplots()
    im = ax.imshow(heatmap[::-1])           # очень по ублюдочному но работает   plot_intensity_on_grid([i for i in range(9)])
    plt.show()
if __name__ == "__main__":
    #plot_grid_and_microphones(9*9, np.array([1,1,1]),1,1,
                              #np.array([0.5,0.5,0]), np.array([-0.5, 0.5,0]))
    #plot_intensity_on_grid([i for i in range(9)])
    pass