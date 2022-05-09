# Написать программу, которая будет выводить на экран случайные числа
# от 1 до 10 до тех пор, пока не выпадет 7.

from random import randint

numb: int = 0

while numb != 7:
    numb = randint(1, 10)
    print(numb)
