# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное;
# n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел


from random import randint
from typing import List, Dict, Generator


def double_fact_func(rand_ls: List[int]) -> Dict[int, int]:
    result_dct = {}
    for numb in rand_ls:

        if numb % 2 == 0:
            values: Generator = (i for i in range(1, numb + 1) if i % 2 == 0)
            fact_even = 1
            for val in values:
                fact_even *= val
            result_dct[numb] = fact_even

        elif numb % 2 != 0:
            values: Generator = (i for i in range(1, numb + 1) if i % 2 != 0)
            fact_odd = 1
            for val in values:
                fact_odd *= val
            result_dct[numb] = fact_odd

    return result_dct


numbs: List[int] = [randint(1, 10) for _ in range(5)]

print(double_fact_func(numbs))
