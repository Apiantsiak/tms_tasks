# Дано число. Найти сумму и произведение его цифр.

from random import randint
from typing import List

numb: int = randint(1, 1000)
prompts: List[str] = [
                     "Number -",
                     "The sum of the digits of this number -",
                     "The product of the digits of this number -",
                     ]

numb_sum: int = 0
numb_add: int = 1

for i in str(numb):
    numb_sum += int(i)
    numb_add *= int(i)

print(f"{prompts[0]} {int(numb)}\n{prompts[1]} {numb_sum}\n{prompts[2]} {numb_add}")
