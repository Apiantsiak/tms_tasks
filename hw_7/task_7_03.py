# Дан словарь, создать новый словарь,
# поменяв местам ключ и значение


from typing import Dict


user_dct: Dict[str, int or str] = {"name": "Alexey",
                                   "age": 28,
                                   "group": "z18",
                                   }

user_new_dct: Dict[str, int or str] = {value: key for key, value in user_dct.items()}

print(user_dct, user_new_dct, sep="\n")
