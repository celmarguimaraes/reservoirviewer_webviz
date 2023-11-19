from curve.curve import Curve
from .coordinate import Coordinate
from math import sqrt


def calculate_distance(c1: "Coordinate", c2: "Coordinate") -> float:
    return sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)


def calculate_distances(curve: Curve):
    distances = {}
    for i in range(curve.number_of_elements - 1):
        distance = calculate_distance(
            curve.get_coordinate(i), curve.get_coordinate(i + 1)
        )
        if distance not in distances.keys():
            distances[distance] = 1
        else:
            distances[distance] += 1
    return distances


def validate_curve(curve: Curve):
    problem_coordinates = []
    is_error = False
    for i in range(curve.number_of_elements - 1):
        c1 = curve.get_coordinate(i)
        c2 = curve.get_coordinate(i + 1)
        distance = calculate_distance(c1, c2)
        if c1.get_x() == c2.get_x() and distance != 1:
            problem_coordinates.append(f"{c1}x{c2}")
            is_error = True
        elif c1.get_y() == c2.get_y() and distance != 1:
            problem_coordinates.append(f"{c1}x{c2}")
            is_error = True
    return {"is_error": is_error, "problem_coordinates": problem_coordinates}
