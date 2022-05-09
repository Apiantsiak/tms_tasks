# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех
# натуральных чисел от 1 до n включительно


from random import randint
from math import factorial


user_numb: int = randint(1, 20)


def my_factorial_func(numb: int) -> int:
    fact_value = 1
    for i in range(2, numb + 1):
        fact_value *= i
    return fact_value


print(f"Factorial {user_numb} is {my_factorial_func(user_numb)},\n"
      f"The check value calculated using the 'math' module {factorial(user_numb)}")
