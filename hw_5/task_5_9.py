# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

from random import randint

m: int = randint(2, 200)
n: int = randint(2, 200)

if m > n:
    print(f"n = {n} m = {m}")
    for numb in range(n, m + 1):
        print()
        print(numb, end=": ")
        for var in range(2, numb - 1):
            if numb % var == 0:
                print(var, end=" ")
elif n > m:
    print(f"m = {m} n = {n}")
    for numb in range(m, n + 1):
        print()
        print(numb, end=": ")
        for var in range(2, numb - 1):
            if numb % var == 0:
                print(var, end=" ")
