# Создать функцию, которая принимает на вход неопределенное
# количество аргументов и возвращает их сумму и максимальное из них


from random import randint
from typing import List, Tuple


def args_sum_func(*args) -> Tuple[int, int]:
    sum_args = 0
    max_value = max(args)
    for var in args:
        sum_args += var
    return sum_args, max_value


rand_ls: List[int] = [randint(1, 10) for _ in range(randint(1, 20))]
sum_args_val, max_val = args_sum_func(*rand_ls)

print("The sum is {}\nThe Max value is {}".format(sum_args_val, max_val))
