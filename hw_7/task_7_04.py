# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Использовать функцию.
#
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in

from random import randint
from typing import Dict, List
from collections import defaultdict


def repeat_numb_func(rand_ls: List[int]) -> Dict[int, int]:
    numb_repeat_dct = defaultdict(int)
    for number in rand_ls:
        numb_repeat_dct[number] += 1
    return numb_repeat_dct


numbers = [randint(1, 10)for _ in range(randint(20, 100))]

print(repeat_numb_func(numbers))
