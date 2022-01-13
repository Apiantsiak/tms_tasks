# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл


from typing import List
from random import randint
import json


matrix: List[List[int]] = [[randint(1, 9) for _ in range(10)] for _ in range(10)]

for i in matrix:
    print(i)
print()

with open("test_json.txt", "w") as json_file:
    data = json.dumps({"matrix": matrix}, indent=4)
    json_file.write(data)

with open("test_json.txt") as json_file:
    json_data = json.loads(json_file.read())

for val in json_data.values():
    for ls in val:
        for numb in ls:
            if not numb % 2:
                ls.insert(ls.index(numb), 0)
                del ls[ls.index(numb)]
        print(ls)

with open("test_json(1).txt", "w") as js_file_for_wr:
    data = json.dumps(json_data, indent=4)
    js_file_for_wr.write(data)
