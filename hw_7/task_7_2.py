# Даны три слова. Выяснить, является ли хоть одно из них палиндромом("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)


from typing import List, NoReturn


def palindromes_func(*args) -> NoReturn:
    for i in args:
        if i.lower() == i[::-1].lower():
            print("Word '{}' is palindrome ".format(i))


words_ls: List[str] = ["Noon", "Alexey", "Level", "car", "cat", "Python", "Bob"]
palindromes_func(*words_ls)
