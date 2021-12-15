# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1
# до 9.

from random import randint
from typing import List

square_matrix: List[List[int]] = [[randint(1, 9) for i in range(4)] for j in range(4)]

for i in square_matrix:
    print(i, end="\n")
