# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).

from random import randint
from typing import List

rand_lst: List[int] = [randint(0, 20) for i in range(randint(0, 20))]
result: int = 0
count: int = 0

print(rand_lst)

for i in range(len(rand_lst) - 2):
    if rand_lst[i + 2] > rand_lst[i + 1] > rand_lst[i]:
        count += 1
    elif count >= 1 and rand_lst[i + 1] > rand_lst[i + 2]:
        result += 1
        count = 0
if rand_lst[-1] > rand_lst[-2] > rand_lst[-3]:
    result += 1

print(result)
