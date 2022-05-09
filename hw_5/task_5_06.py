# Создать список учеников подобной структуры.
# Определить средний балл оценок по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.

from random import randint
from typing import List, Dict, Any

pupils: List[Dict[str, str and int]] = [
                                        {
                                            'firstname': 'Masha',
                                            'Group': 42,
                                            'physics': randint(1, 10),
                                            'informatics': randint(1, 10),
                                            'history': randint(1, 10),
                                        },
                                        {
                                            'firstname': 'Sasha',
                                            'Group': 42,
                                            'physics': randint(1, 10),
                                            'informatics': randint(1, 10),
                                            'history': randint(1, 10),
                                        },
                                        {
                                            'firstname': 'Lesha',
                                            'Group': 42,
                                            'physics': randint(1, 10),
                                            'informatics': randint(1, 10),
                                            'history': randint(1, 10),
                                        },
                                       ]
sum_val: Any = 0
avr_point: int = 0

for i in pupils:
    sum_val = i['physics'] + i['informatics'] + i['history']
    avr_point = sum_val / 3
    if avr_point > 4:
        print(f"Pupil that average point greater than 4 and equals {avr_point}:")
        for key, val in i.items():
            print(key.capitalize(), val, sep=" - ")
