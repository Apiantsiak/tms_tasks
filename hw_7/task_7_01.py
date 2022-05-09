# Дан список слов. Сгенерировать новый список с
# перевернутыми словами


from random import choice, randint
from string import ascii_lowercase
from typing import List


first_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 10))])
                       for _ in range(11)
                       ]
reverse_ls: List[str] = [i[::-1] for i in first_ls]

print(first_ls, reverse_ls, sep="\n")
