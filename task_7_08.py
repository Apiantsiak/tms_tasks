# Дан массив целых чисел A.
# Найти суммы положительных и отрицательных элементов массива,
# используя функцию определения суммы.


from random import randint
from typing import Tuple, List


def sum_val_func(ls: List[int]) -> Tuple[int, int]:
    sum_1, sum_2 = 0, 0
    for i in ls:
        if i > 0:
            sum_1 += i
        else:
            sum_2 += i
    return sum_1, sum_2


rand_ls = [randint(-100, 100) for _ in range(randint(10, 100))]
print(sum_val_func(rand_ls))
