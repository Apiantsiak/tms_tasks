# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.


from typing import List


with open("test.txt") as test_file:
    text_form_file: List[str] = test_file.readlines()
    last_file_line: int = len(text_form_file)

with open("test.txt", "a") as test_file:
    text_for_wr: List[str] = [f"{i}. Text line\n" for i in range(last_file_line + 1, last_file_line + 4)]

    # Or can be use [f"{i}. {input('Enter text: ')}\n" for i in range(4)]

    test_file.writelines(text_for_wr)
