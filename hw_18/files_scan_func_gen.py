# Ex.3
# Написать функцию-генератор, которая сканирует папки/файлы и
# возвращает полный путь к файлам, размер которых больше 1 МБ
# '/ful_path_to_file', 'file_size'
# Результат записывается в файл out.txt


import os
from os.path import getsize, join


PATH = '/home/ap/Documents/TMS'


def scan_directory():
    for root, directories, files in os.walk(PATH):
        for name in files:
            condition = getsize(join(root, name)) > 10**6
            if condition:
                with open('out.txt', 'a') as out:
                    out.write(f'{join(root, name)}, {getsize(join(root, name))} bytes\n')


def test_check_file_size():
    with open('out.txt') as log:
        data = log.readlines()
    sizes = [int(line.split(' ')[1])for line in data]
    for size in sizes:
        assert size > 10**6
