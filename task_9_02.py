# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.


from typing import List


with open("test.txt", "w") as test_file:
    prompt: List[str] = [f"{i}. Text line\n" for i in range(1, 7)]

    # Or can use [f"{input('Enter text: ')}\n" for _ in range(1, 7)]

    test_file.writelines(prompt)
