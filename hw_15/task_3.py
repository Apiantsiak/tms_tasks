# Ex.3
# Реализовать декоратор кэширования вызова функции
# В случае, если вызывается функция c одинаковыми
# параметрами, то результат не должен заново вычисляться,
# а возвращаться из хранилища (* изучить lru_cache)


from functools import wraps
from typing import Dict, Tuple
from random import randint


CACHE: Dict[Tuple[str, Tuple[int, int]], int] = {}


def save_in_cache_deco(func):

    @wraps(func)
    def wrapper(a: int, b: int):
        func_name = func.__name__
        func_attr = (a, b)
        key_for_cache = (func_name, func_attr)
        func_result = func(a, b)

        if key_for_cache in CACHE:
            return CACHE[key_for_cache]
        else:
            CACHE[key_for_cache] = func_result
            return CACHE[key_for_cache]

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
    rand_a = randint(1, 100)
    rand_b = randint(1, 100)
    name_of_cached_func = sum_of_numbers.__name__
    sum_of_numbers(rand_a, rand_b)
    assert (name_of_cached_func, (rand_a, rand_b)) in CACHE
