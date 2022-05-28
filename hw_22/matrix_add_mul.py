# Ex.1
# Даны 2 матрицы A[5x5], B[5x5]
# Каждая из них содержит экземпляр класса Shape из less16
# Найти результат сложения 2х матриц

# Ex2
# Дана матрица A[4, 6] и B[?x?]
# Каждая из них содержит экземпляр класса Shape из less16
# Найти результат перемножения 2х матриц


import numpy as np
from random import choice

from hw_16.task_3 import Rectangle, Triangle, Circle
from my_array import MyArray


def create_matrix_of_shapes(row: int, col: int) -> MyArray:
    ls_of_shapes = [
        Rectangle(),
        Triangle(),
        Circle(),
    ]
    matrix = np.array([[choice(ls_of_shapes) for _ in range(col)] for _ in range(row)])
    result_mat = MyArray((row, col), dtype=object, buffer=matrix)
    return result_mat


def matrix_addition(mat_a, mat_b):
    if len(mat_a) != len(mat_b):
        raise ValueError('Matrices are not the same size')
    return mat_a + mat_b


def matrix_multiplication(mat_a, mat_b):
    if len(mat_a) != len(mat_b):
        raise ValueError('Matrices are not the same size')
    return mat_a * mat_b
