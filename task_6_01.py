# Написать функцию, которая получает на вход
# имя и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен. Вызвать функцию
# для каждого элемента списка в цикле.


from random import randint, choice
from string import ascii_lowercase
from typing import List


def user_greetings(name: str) -> None:
    print(f"Hello, {name}")


names_ls: List[str] = ["".join([choice(ascii_lowercase) for _ in range(randint(3, 6))]) for _ in range(6)]

for ch in names_ls:
    user_greetings(ch.capitalize())
