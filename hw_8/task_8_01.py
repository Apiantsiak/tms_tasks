# Создать lambda функцию, которая  принимает на вход имя и выводит его в формате “Hello, {name}”


names_func = (lambda name: "Hello, {}".format(name))

print(names_func("Alexey"))
