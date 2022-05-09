# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]

from random import randint
from typing import List

numbs: List[int] = [randint(1, 60) for _ in range(19)]

print("Original massive {}".format(numbs))

for i in range(len(numbs)):
    if numbs[i] % 2 == 0:
        numbs[i] = max(numbs)


print("Modified massive {}\n"
      "Length of massive {}\n"
      "Max value is {}".format(numbs, len(numbs), max(numbs)))
