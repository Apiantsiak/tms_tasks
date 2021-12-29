# Создать lambda функцию, которая принимает на вход список имен и
# выводит их в формате “Hello, {name}” в другой список


from random import choice, randint
from string import ascii_lowercase
from typing import List, Tuple, Any


rand_name_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 9))]).capitalize()
                           for _ in range(randint(1, 10))
                           ]

result_map: List[str] = list(map(lambda name: f"Hello, {name}", rand_name_ls))

result_list_comp: Tuple[Any] = (lambda rand_ls: [f"Hello, {name}" for name in rand_ls],)

print("Use 'list_comp' method:", result_list_comp[0](rand_name_ls),
      "\nUse 'map' method:", result_map, sep="\n")
