# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

from random import randint
from typing import List


numb_ls: List[int] = [randint(1, 10) for _ in range(10)]


def decorator_func(func):
    def wrapper(arg_2=2, arg_1=1):
        func(arg_1, arg_2)
    return wrapper


@decorator_func
def my_func(arg_1=1, arg_2=2):
    print(arg_1, arg_2)


my_func()
