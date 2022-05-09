# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.


from typing import List
from random import randint


numbers_ls: List[int] = [randint(1, 20) for _ in range(randint(5, 20))]


def decorator_func(func):

    def wrapper(rand_ls):
        rand_ls = [i for i in rand_ls if i % 2]
        return func(rand_ls)

    return wrapper


@decorator_func
def my_func(rand_ls: List[int]) -> List[int]:
    return rand_ls


print(numbers_ls, my_func(numbers_ls), sep="\n")
