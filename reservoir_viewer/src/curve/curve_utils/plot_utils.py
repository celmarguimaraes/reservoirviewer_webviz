from typing import List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from .dimension import Dimension

from ..curve import Curve


# TODO: Arrumar plot para dimenões variadas


def _create_segments(x: List, y: List) -> List[List]:
    '''
    Create segments from x and y coordinates.
    Takes a list of x coordinates and a list of y coordinates and returns a list of segments.
    Each segment is a list of two points.
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    segments = [[[1, 1], [2, 2]], [[2, 2], [3, 3]], [[3, 3], [4, 4]]]
    '''
    points = list(zip(x, y))
    segments = list(zip(points[:-1], points[1:]))
    return segments


def lineplot(x: List, y: List, x_max = None, y_max = None,  cmap=plt.get_cmap('coolwarm'), linewidth=3, alpha=1.0, size=(5, 5), all_ticks=False):
    '''
    Cria um gráfico de linha com as listas de x e y de cada coordenada.
    coolwarm: começa no azul e termina no vermelho
    o ponto (0, 0) começa no canto superior esquerdo como funciona nas matrizes em 
    computação e não no canto inferior esquerdo como começam no eixo cartesiano.
    '''
    z = np.linspace(0.0, 1.0, len(x))
    
    segments = _create_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, linewidth=linewidth, alpha=alpha)
    
    plt.rcParams["figure.figsize"] = size
    ax = plt.gca()
    ax.add_collection(lc)
    
    plt.xlim(-0.5, max(x) + 0.5) if x_max is None else plt.xlim(-0.5, x_max)
    plt.ylim(-0.5, max(y) + 0.5) if y_max is None else plt.ylim(-0.5, y_max)

    # if all_ticks:
    plt.xticks(np.arange(0, max(x) + 1, 1)) if x_max is None else plt.xticks(np.arange(0, x_max + 1, 1))
    plt.yticks(np.arange(0, max(y) + 1, 1)) if y_max is None else plt.yticks(np.arange(0, y_max + 1, 1))
    ax.invert_yaxis()
    
    return lc


def get_xy_from_curve(curve: Curve):
    coords = [(curve.get_coordinate(i).x, curve.get_coordinate(i).y) for i in range(curve.number_of_elements)]
    x, y = zip(*coords)
    return x, y


def plot_curve(curve: Curve, cmap=plt.get_cmap('coolwarm'), linewidth=3, alpha=1.0, size=(5, 5), all_ticks=False):
    x, y = get_xy_from_curve(curve)
    print(x, y)
    return lineplot(x, y, curve.dimension.x, curve.dimension.y, cmap, linewidth, alpha, size, all_ticks)


def plot_heatmap(heatmatrix: List[List]):
    ax, fig = plt.subplots()
    fig.imshow(heatmatrix, cmap='bwr', interpolation='nearest')
    return fig