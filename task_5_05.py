# Создать список с фамилиями. Вывести все фамилии,
# которые начинаются на П и заканчиваются на а

from random import randint, choice
from string import ascii_lowercase
from typing import List


last_names_gen: List[List[str]] = [[choice(ascii_lowercase[0:16:5]) for _ in range(randint(3, 20))]
                                   for _ in range(randint(3, 10))]
last_names: List[str] = ["".join(i).capitalize() for i in last_names_gen]

for i in last_names:
    if "P" in i and i[-1] == "a":
        print("Last Name 'P...a' type is: {}".format(i))

print(last_names)
