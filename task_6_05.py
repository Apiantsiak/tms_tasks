# Создать функцию, принимающая на вход неопределенное
# количество аргументом и возвращающая сумму args[i] * i
# Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


from random import randint
from typing import List


def args_sum_func(args_ls: List[int]) -> int:
    sum_args = 0
    for pos, var in enumerate(args_ls):
        sum_args += var * pos
    return sum_args


rand_ls = [randint(1, 10) for _ in range(randint(1, 20))]

print(f"The sum(args[i] * i) of {rand_ls}\n"
      f"Equals: {args_sum_func(rand_ls)}")
