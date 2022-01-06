# Написать декоратор, который будет выводить время выполнения функции


from typing import List
from time import time


def execution_time_func(func):

    def decorator_func():
        start = time()
        func()
        end = time()
        ex_time = end - start
        print("Function execution time is {} sec.".format(ex_time))

    return decorator_func


@execution_time_func
def rand_func():
    rand_ls: List[List[int]] = [[i for i in range(10)] for _ in range(10)]
    for i in rand_ls:
        print(i)


print(rand_func())
