# Дан список имен, отфильтровать все имена, где есть буква k


from random import choice, randint
from string import ascii_lowercase
from typing import List


rand_name_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 9))])
                           for _ in range(randint(1, 10))
                           ]
result = list(filter(lambda name: "k" in name, rand_name_ls))

print(rand_name_ls, result, sep="\n")
