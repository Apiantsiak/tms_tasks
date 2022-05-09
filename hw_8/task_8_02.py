# Создать lambda функцию, которая принимает на вход список имен и
# выводит их в формате “Hello, {name}” в другой список


from random import choice, randint
from string import ascii_lowercase
from typing import List


rand_name_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 9))]).capitalize()
                           for _ in range(randint(1, 10))]

result_map: List[str] = list(map(lambda name: f"Hello, {name}", rand_name_ls))

print(result_map, sep="\n")
