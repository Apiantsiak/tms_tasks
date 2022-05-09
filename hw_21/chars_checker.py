# Ex.4
# Написать функцию, которая подсчитывает число вхождений символов в строке и
# выводит их в порядке убывания.
# Реализацию покрыть параметризационными тестами.
# Дополнительно написать тест, используя фикстуру из Ex.3

import pytest

from collections import defaultdict
from typing import List, Tuple


def calculate_chars(rand_str: str) -> List[Tuple[str, int]]:
    if not isinstance(rand_str, str):
        raise ValueError
    dct = defaultdict(int)
    for char in rand_str:
        dct[char] += 1
    ls = [*dct.items()]
    ls_sort = sorted(ls, key=lambda x: x[1], reverse=True)
    return ls_sort


@pytest.mark.parametrize(
    'rand_str,expected',
    [
        ('Hello Word!', ('l', 2)),
        ('Pycharm Professional Edition', ('o', 3)),
        ('A b c d', (' ', 3))
    ]
)
def test_correct_result(rand_str, expected):
    assert calculate_chars(rand_str)[0] == expected


@pytest.mark.parametrize(
    'value',
    [
        ['a', 'b', 'c'],
        42,
        ['www.google.com']
    ]
)
def test_negative_invalid_value(value):
    with pytest.raises(ValueError):
        calculate_chars(value)


@pytest.mark.xfail(reason='Sometimes characters in sorted tuples are not equal')
def test_use_fixture(gen_random_letters_range):
    rand_str = gen_random_letters_range
    result = {(char, rand_str.count(char)) for char in rand_str}
    result = sorted(result, key=lambda x: x[1], reverse=True)
    assert calculate_chars(rand_str)[0] == result[0]
