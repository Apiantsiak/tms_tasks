# Дана целочисленная матрица А[n,m].
# Посчитать количество элементов матрицы, превосходящих среднее арифметическое значение элементов матрицы
# и сумма индексов которых четна.

from random import randint
from typing import List

n: int = randint(3, 10)
m: int = randint(3, 10)

A: List[List[int]] = [[randint(0, 10) for n in range(n)]for m in range(m)]
avr_sum = 0

for i in A:
    avr_sum += sum(i)
    print(i)
    print(avr_sum / n * m)
    for j in i:
        if j > avr_sum / n*m:
            print(j)
