# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}


from random import randint, choice
from typing import Dict
from string import ascii_lowercase


gen_dct: Dict[str, int] = {"".join(choice(ascii_lowercase) for _ in range(randint(2, 5))): i
                           for i in range(randint(2, 5))}


func_l = (lambda **kwargs: {key * 2: val for key, val in kwargs.items()})


print(gen_dct, func_l(**gen_dct), sep="\n")
