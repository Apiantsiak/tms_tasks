# Описать функцию is_power_n( k , n ) логического типа, возвращающую True,
# если целый параметр k (> 0) является степенью числа n (> 1), и False в противном случае.
#
# Дано число n (> 1) и набор из 10 целых положительных чисел.
# С помощью функции is_power_n найти количество степеней числа N в данном наборе.


from typing import List
from random import randint


def is_power_n(k: int, n: int) -> bool:
    while True:
        k /= n
        if k == 1:
            return True
        elif k < 1:
            return False


numb_ls: List[int] = [randint(20, 200) for i in range(50, 100)]

rand_numb: int = randint(0, 100)
counter: int = 0

for number in numb_ls:
    if is_power_n(number, rand_numb):
        print(number, rand_numb)
        counter += 1

print(counter, rand_numb, numb_ls, sep="\n")
