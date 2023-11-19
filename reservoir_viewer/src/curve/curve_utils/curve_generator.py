from matplotlib import pyplot as plt
from typing import List, Callable

from curve.curve import Curve
from curve.curve_utils.plot_utils import plot_curve
from curve.curve_utils.dimension import Dimension
from curve.pseudo_hilbert_curve import PseudoHilbertCurve
from curve.curve_utils.curve_validator import calculate_distances, validate_curve


def save_image_curve(curve: Curve, filename: str):
    '''
    Salva curva em um arquivo de imagem .png
    curve: curva a ser plotada
    filename: nome do arquivo da imagem a ser gerada
    '''
    fig, ax = plt.subplots()
    ax.add_collection(plot_curve(curve))
    fig.savefig(filename + '.png')


def generate_curves(curve_type: Callable[[int, Dimension], Curve], dimensions: List[Dimension]) -> List[Curve]:
    '''
    Gera curvas com base nas dimensões passadas
    curve: tipo de curva a ser gerada
    dimensions: dimensões das curvas a serem geradas
    '''
    curves = []
    for dimension in dimensions:
        curve = curve_type(dimension.x * dimension.y, dimension)
        curves.append(curve)
    return curves


def save_100_pseudo_hilbert_curves():
    '''
    Salva imagens de curvas com dimensões de 1x1 à 10x10
    '''
    for i in range(1, 11):
        for j in range(1, 11):
            c1 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=0, sense_of_rotation=0)
            c2 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=1, sense_of_rotation=0)
            c3 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=2, sense_of_rotation=0)
            c4 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=3, sense_of_rotation=0)
            c5 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=0, sense_of_rotation=1)
            c6 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=1, sense_of_rotation=1)
            c7 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=2, sense_of_rotation=1)
            c8 = PseudoHilbertCurve(i*j, Dimension(i, j), direction=3, sense_of_rotation=1)
            save_image_curve(c1, f'./plots/pseudohilbert_curve({c1.get_dimension().x}x{c1.get_dimension().y})_direction_0_rotation_0')
            save_image_curve(c2, f'./plots/pseudohilbert_curve({c2.get_dimension().x}x{c2.get_dimension().y})_direction_1_rotation_0')
            save_image_curve(c3, f'./plots/pseudohilbert_curve({c3.get_dimension().x}x{c3.get_dimension().y})_direction_2_rotation_0')
            save_image_curve(c4, f'./plots/pseudohilbert_curve({c4.get_dimension().x}x{c4.get_dimension().y})_direction_3_rotation_0')
            save_image_curve(c5, f'./plots/pseudohilbert_curve({c5.get_dimension().x}x{c5.get_dimension().y})_direction_0_rotation_1')
            save_image_curve(c6, f'./plots/pseudohilbert_curve({c6.get_dimension().x}x{c6.get_dimension().y})_direction_1_rotation_1')
            save_image_curve(c7, f'./plots/pseudohilbert_curve({c7.get_dimension().x}x{c7.get_dimension().y})_direction_2_rotation_1')
            save_image_curve(c8, f'./plots/pseudohilbert_curve({c8.get_dimension().x}x{c8.get_dimension().y})_direction_3_rotation_1')



def calculate_distances_100_pseudo_hilbert_curves():
    '''
    Valida curvas com dimensões de 1x1 à 10x10
    '''
    curves_distances = {}
    for i in range(1, 11):
        for j in range(1, 11):
            curve = PseudoHilbertCurve(i*j, Dimension(i, j))
            coord_label = f'{i}x{j}'
            distances = calculate_distances(curve)  
            if coord_label not in distances.keys():
                curves_distances[coord_label] = calculate_distances(curve)
            else:
                distances = calculate_distances(curve)
                curves_distances[coord_label] = distances
    return curves_distances
    

def validate_100_pseudo_hilbert_curves():
    '''
    Valida curvas com dimensões de 1x1 à 10x10
    '''
    valid_curves = []
    for i in range(1, 20):
        for j in range(1, 20):
            curve = PseudoHilbertCurve(i*j, Dimension(i, j))
            valid_curves.append(validate_curve(curve))
    return valid_curves
