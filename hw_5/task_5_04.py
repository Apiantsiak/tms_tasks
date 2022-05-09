# Дана целочисленная матрица А[n,m].
# Посчитать количество элементов матрицы, превосходящих среднее арифметическое значение элементов матрицы
# и сумма индексов которых четна.

from random import randint
from typing import List

n: int = randint(3, 10)
m: int = randint(3, 10)

A: List[List[int]] = [[randint(0, 10) for n in range(n)]for m in range(m)]
avr_sum: float = sum(sum(i) for i in A) / (n * m)

avr_ind_check: int = 0
counter: int = 0

for i in A:
    for j in range(len(i)):
        if i[j] > avr_sum:
            avr_ind_check += j
            counter += 1

if avr_ind_check % 2 == 0:
    print(f"Number of elements {counter}")
else:
    print(f"The sum of the indices is not even and is equal to {avr_ind_check}")
