# Дан список словарей. Каждый словарь описывает машину(серийный номер и год
# выпуска). Создать новый список со всеми машинами, год выпуска которых больше n


from typing import Dict, List
from random import randint


car_year: int = randint(1993, 2009)

cars_ls: List[Dict[str, int]] = [{'number': 1234, "year": 2006},
                                 {'number': 4356, "year": 2008},
                                 {'number': 7878, "year": 1999},
                                 {'number': 454545, "year": 1999},
                                 {'number': 4545454, "year": 1994},
                                 {'number': 15451, "year": 1996},
                                 {'number': 24545, "year": 1998},
                                 ]

cars_sort_ls: List[Dict[str, int]] = [i for i in cars_ls if i["year"] > car_year]
print(car_year, cars_sort_ls, sep="\n")
