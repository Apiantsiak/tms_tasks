# Ex. 1
# Написать функцию, которая определяет, является переданная строка палиндромом
# Написать тесты, в тч параметризационные


import pytest


def palindrome_checker(word: str) -> bool:
    if not isinstance(word, str):
        raise ValueError
    word_lowercase = word.strip().lower()
    return True if word_lowercase == word_lowercase[::-1] else False


@pytest.mark.parametrize(
    'word,expected',
    [
        ('Anna', True),
        ('python', False),
        ('civiC', True),
        ('level', True),
        ('Tom', False),
    ]
)
def test_correct_res(word, expected):
    assert palindrome_checker(word) == expected


@pytest.mark.parametrize(
    'invalid_value',
    [
        12321,
        ['TeNeT']
    ]
)
def test_negative_invalid_value(invalid_value):
    with pytest.raises(ValueError):
        palindrome_checker(invalid_value)
