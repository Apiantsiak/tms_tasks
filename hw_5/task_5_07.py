# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку (больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.

from random import randint, choice
from typing import List

rand_range: int = randint(2, 10)
numb_tries: int = randint(1, 5)
rand_numbers: List[int] = [i for i in range(rand_range)]
win_numb: int = choice(rand_numbers)

prompt: List[str] = ["Hi, enter your range of numbers:",
                     f"Ok, your range is from {rand_numbers[0]} to {rand_numbers[-1]}\nNow enter number of tries:",
                     f"Ok, you have {numb_tries} tries",
                     f"You are the winner the right number was {win_numb}",
                     f"You are the loser the right number was {win_numb}",
                     "Try enter number lower next time",
                     "Try enter number bigger next time"
                     ]
user_numb: int = 0
counter: int = 0
print(prompt[0], prompt[1], prompt[2], sep="\n")

while True:
    user_numb = choice(rand_numbers)
    print(f"\nNow enter the number: {user_numb}")
    counter += 1
    if user_numb == win_numb:
        print(prompt[3])
        break
    elif counter == numb_tries:
        print(prompt[4])
        break
    elif user_numb > win_numb:
        print(prompt[5])
        continue
    elif user_numb < win_numb:
        print(prompt[6])
        continue
