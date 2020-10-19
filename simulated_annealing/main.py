import math
import random

from PIL import Image, ImageDraw

from collections import namedtuple
from utils import simulated_annealing

Point = namedtuple('Point', ('x', 'y'))

# Parameters for traveling salesman problem.
SIZE = 1024
COUNT = 100

# Parameters for drawing solution.
WIDTH = 2
RADIUS = 5


def get_path_length(path):
    path_length = 0
    for i in range(0, COUNT):
        point1 = points[path[i]]
        point2 = points[path[(i + 1) % COUNT]]
        path_length += math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    return path_length


def transform_path(path):
    transformed_path = path.copy()
    point1 = random.randint(0, COUNT - 1)
    point2 = random.randint(0, COUNT - 1)

    transformed_path[point1:point2] = reversed(transformed_path[point1:point2])
    return transformed_path


def draw_solution(solution):
    solution_image = Image.new('RGB', (SIZE, SIZE), (0, 0, 0))
    solution_drawer = ImageDraw.Draw(solution_image)
    for i in range(0, COUNT):
        point1 = points[solution[i]]
        point2 = points[solution[(i + 1) % COUNT]]
        solution_drawer.line([point1.x, point1.y, point2.x, point2.y], width=WIDTH, fill='white')
        solution_drawer.ellipse(
            [point1.x - RADIUS, point1.y - RADIUS, point1.x + RADIUS, point1.y + RADIUS], fill='white'
        )

    solution_image.save("solution.png")


points = [Point(x=random.randint(0, SIZE - 1), y=random.randint(0, SIZE - 1)) for _ in range(0, COUNT)]
initial_solution = [i for i in range(0, COUNT)]
final_solution = simulated_annealing(initial_solution, transform_path, get_path_length, is_maximize=False)
draw_solution(final_solution)
