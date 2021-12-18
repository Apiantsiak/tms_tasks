# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

from random import randint
from typing import List

high_matrix: int = 6
length_matrix: int = 6

matrix: List[List[int or str]] = [[randint(0, 100) for _ in range(high_matrix)]
                                  for _ in range(length_matrix)
                                  ]

max_value_index: int = 0
max_value: int = 0

for i in matrix:
    max_value = max(i)
    i.remove(max(i))
    i.insert(max_value_index, f"|{max_value}|")
    max_value_index += 1
    print(i, f"Max is {max_value}")
