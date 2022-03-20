# Ex.3
# Реализовать декоратор кэширования вызова функции
# В случае, если вызывается функция c одинаковыми
# параметрами, то результат не должен заново вычисляться,
# а возвращаться из хранилища (* изучить lru_cache)


from functools import wraps
from typing import Dict
from random import randint


CACHE: Dict[tuple, int] = {}


def save_in_cache_deco(func):

    @wraps(func)
    def wrapper(a: int, b: int):

        if (a, b) in CACHE:
            return CACHE[(a, b)]
        else:
            CACHE[(a, b)] = func(a, b)
            return CACHE[(a, b)]

    return wrapper


@save_in_cache_deco
def sum_of_numbers(a: int, b: int) -> int:
    """Add number 'a' to number 'b'

    :param a: int
    :param b: int
    :return: int
    """
    return a + b


def test_save_in_cache():
    rand_numb_a = randint(1, 100)
    rand_numb_b = randint(1, 100)

    sum_of_numbers(rand_numb_a, rand_numb_b)

    assert (rand_numb_a, rand_numb_b) and sum_of_numbers(rand_numb_a, rand_numb_b) not in CACHE
