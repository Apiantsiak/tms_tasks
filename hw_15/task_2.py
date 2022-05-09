# Ex.2
# Найти сумму всех чисел, меньших 1000, кратных 3 и 7
# Реализовать через filter/map/reduce


from functools import reduce
from typing import List

lst: List[int] = list(range(1000))

res_filter = sum(filter(lambda x: x % 3 + x % 7 == 0, lst))
res_map = sum(map(lambda x: x if not x % 3 + x % 7 else 0, lst))
res_reduce = reduce(lambda x, y: x + y if not y % 3 + y % 7 else x, lst)


def test_positive():
    result = sum([numb for numb in lst if not numb % 3 and not numb % 7])
    assert res_filter == result
    assert res_map == result
    assert res_reduce == result
