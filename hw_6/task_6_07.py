# Создать функцию, которая принимает на вход
# неопределенное количество именных аргументов
# и выводит на экран те из них, длина ключа которых четна.


from random import randint, choice
from string import ascii_lowercase
from typing import List, Dict, NoReturn


def even_key_func(**kwargs) -> NoReturn:
    for key, val in kwargs.items():
        if len(key) % 2 == 0:
            print(key, val)


rand_names: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 8))])
                         for _ in range(10)
                         ]

user_dct: Dict[str, int] = dict(zip(rand_names, (i for i in range(10))))
even_key_func(**user_dct)
