# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.


from random import choice, randint
from string import ascii_lowercase
from typing import List


rand_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 9))])
                      for _ in range(randint(1, 10))]

format_rand_ls: List[str] = [f"{pos} - {i}" for pos, i in enumerate(rand_ls)]

print(rand_ls, format_rand_ls, sep="\n")
