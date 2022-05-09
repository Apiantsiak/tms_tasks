# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).


from random import randint
from typing import List


matrix_size: int = randint(1, 10)


def matrix_func(rand_from=1, rand_to=9) -> List[List[int]]:
    matrix: List[List[int]] = [[randint(1, 10) for _ in range(rand_from)]
                               for _ in range(rand_to)
                               ]
    return matrix


for i in matrix_func(matrix_size, matrix_size):
    print(i)
