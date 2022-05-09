# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.


from random import randint
from typing import List


numb_ls: List[int] = [i for i in range(randint(5, 10))]


def decorator_func(func):
    def wrapper(*args):
        func_vals = list(func(*args))
        return func_vals[::-1]
    return wrapper


@decorator_func
def my_func(*args):
    return args


print(numb_ls, my_func(*numb_ls), sep="\n")
