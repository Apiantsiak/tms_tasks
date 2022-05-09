# Дан список чисел. Найти произведение всех чисел, которые кратны 3.


from random import randint
from typing import List
from functools import reduce

rand_ls: List[int] = [randint(1, 10) for _ in range(randint(1, 10))]

try:
    result: int = reduce(lambda x, y: x * y, (i for i in rand_ls if i % 3 == 0))
    print(rand_ls, f"\nThe product of the numbers from the list is {result}")
except TypeError:
    print("The sheet has no multiples of 3:", rand_ls)
