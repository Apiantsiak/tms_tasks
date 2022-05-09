# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы. [02-7.2-HL08]

from random import randint, choice
from string import ascii_lowercase
from typing import List

str_gen: List[str] = ["".join(choice(ascii_lowercase)
                      for i in ascii_lowercase[:randint(5, 9)])
                      for j in range(randint(1, 10))
                      ]

user_str: str = " ".join(str_gen).capitalize()
user_reverse_str: str = " ".join(str_gen[::-1]).capitalize()

print(user_str, user_reverse_str, sep="\n")
