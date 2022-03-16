# Ex.2
# Найти сумму всех чисел, меньших 1000, кратных 3 и 7
# Реализовать через filter/map/reduce


from functools import reduce
from typing import List

lst: List[int] = list(range(1000))


res_filter = sum(list(filter(lambda x: x if (x % 3 == 0) and (x % 7 == 0) else 0, lst)))
print(f"Using filter: {res_filter}")

res_map = sum(list(map(lambda x: x if (x % 3 == 0) and (x % 7 == 0) else 0, lst)))
print(f"Using map:{' ' * 4}{res_map}")

res_reduce = reduce(lambda x, y: x + y, [numb for numb in lst if not numb % 3 and not numb % 7])
print(f"Using reduce: {res_reduce}")
