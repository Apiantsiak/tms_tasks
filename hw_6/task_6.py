# 1. Написать 12 функций по переводу:
# -Дюймы в сантиметры и Сантиметры в дюймы
# -Мили в километры и Километры в мили
# -Фунты в килограммыи и Килограммы в фунты
# -Унции в граммы и Граммы в унции
# -Галлон в литры и Литры в галлоны
# -Пинты в литры и Литры в пинты


from random import randint, choice
from typing import List, Dict, Union, Any, NoReturn


def inches_to_centimeters(var: Union[int, float]) -> Union[int, float]:
    result = var * 2.54
    return result


def centimeters_to_inches(var: Union[int, float]) -> Union[int, float]:
    result = var / 2.54
    return result


def miles_to_kilometers(var: Union[int, float]) -> Union[int, float]:
    result = var * 1.609
    return result


def kilometers_to_miles(var: Union[int, float]) -> Union[int, float]:
    result = var / 1.609
    return result


def pounds_to_kilograms(var: Union[int, float]) -> Union[int, float]:
    result = var / 2.205
    return result


def kilograms_to_pounds(var: Union[int, float]) -> Union[int, float]:
    result = var * 2.205
    return result


def ounces_to_grams(var: Union[int, float]) -> Union[int, float]:
    result = var * 28.35
    return result


def grams_to_ounces(var: Union[int, float]) -> Union[int, float]:
    result = var / 28.35
    return result


def gallons_to_liters(var: Union[int, float]) -> Union[int, float]:
    result = var * 4.546
    return result


def liters_to_gallons(var: Union[int, float]) -> Union[int, float]:
    result = var / 4.546
    return result


def pints_to_liters(var: Union[int, float]) -> Union[int, float]:
    result = var / 1.76
    return result


def liters_to_pints(var: Union[int, float]) -> Union[int, float]:
    result = var * 1.76
    return result


def pprint_ls_func(rand_ls: List[Any]) -> NoReturn:
    for i in rand_ls:
        print(i)


# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче).
#
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


prompt_text_ls: List[str] = ["For exit use key - 0",
                             "From inches to centimeters use key - 1",
                             "From centimeters to inches use key - 2",
                             "From miles to kilometers use key - 3",
                             "From kilometers to miles use key - 4",
                             "From pounds to kilograms use key - 5",
                             "From kilograms to pounds use key - 6",
                             "From ounces to grams use key - 7",
                             "From grams to ounces use key - 8",
                             "From gallons to liters use key - 9",
                             "From liters to gallons use key - 10",
                             "From pints to liters use key - 11",
                             "From liters to pints use key - 12",
                             ]

sign_ls: List[str] = [str(i) for i in range(0, 13)]

pprint_ls_func(prompt_text_ls)

while True:
    user_sign = choice(sign_ls)
    user_numb = randint(0, 100)
    print(f"\nEnter key number: {user_sign}")
    func_ls: List[Union[int, float, str]] = ["Exit",
                                             inches_to_centimeters(user_numb),
                                             centimeters_to_inches(user_numb),
                                             miles_to_kilometers(user_numb),
                                             kilometers_to_miles(user_numb),
                                             pounds_to_kilograms(user_numb),
                                             kilograms_to_pounds(user_numb),
                                             ounces_to_grams(user_numb),
                                             grams_to_ounces(user_numb),
                                             gallons_to_liters(user_numb),
                                             liters_to_gallons(user_numb),
                                             pints_to_liters(user_numb),
                                             liters_to_pints(user_numb),
                                             ]
    sign_func_dct: Dict[str, Union[int, float, str]] = dict(zip(sign_ls, func_ls))
    if user_sign == "0":
        print(f"{sign_func_dct[user_sign]}")
        break
    else:
        if user_sign != "0":
            print(f"Enter value to convert: {user_numb}\n")
            text = prompt_text_ls[int(user_sign)].split(" ", 5)
            print(f"{user_numb} {text[1].capitalize()} equals "
                  f"{sign_func_dct[user_sign]} {text[3].capitalize()}\n")
