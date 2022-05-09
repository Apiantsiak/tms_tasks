# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint
from typing import List

square_matrix: List[List[int]] = [[randint(1, 9) for i in range(4)] for j in range(4)]
sum_values: int = 0

for i in square_matrix:
    print(i, end="\n")
    for j in i:
        if j % 3 == 0:
            sum_values += j

print("Sum of values that are multiples of 3: {}".format(sum_values))
