import math
import random

# Parameters for simulated annealing algorithm.
INITIAL_TEMP = 100
STEPS = 100000
TEMP_STEP = INITIAL_TEMP / STEPS


def simulated_annealing(initial_solution, transform_solution, calc_solution, is_maximize=True):
    current_temp = INITIAL_TEMP
    solution = initial_solution

    while current_temp > 0:
        transformed_solution = transform_solution(solution)
        solution_score = calc_solution(transformed_solution) - calc_solution(solution)
        if is_maximize is False:
            solution_score *= -1

        if solution_score > 0:
            solution = transformed_solution
        else:
            if random.uniform(0, 1) < math.exp(solution_score / current_temp):
                solution = transformed_solution

        current_temp -= TEMP_STEP

    return solution
