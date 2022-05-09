# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

from random import randint

N: int = randint(1, 40)
S: float = sum(1 / i for i in range(1, N + 1))

print(f"N = {N}\nS = {S}")
