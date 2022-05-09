# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

data_d: dict = {'test': 'test_value',
                'europe': 'eur',
                'dollar': 'usd',
                'ruble': 'rub',
                }

data_keys: list = list(data_d.keys())

# Using a for loop

for key in data_keys:
    data_d[key + str(len(key))] = data_d.pop(key)

print("Result using a for loop:", data_d)

# Using a while loop

data_d: dict = {'test': 'test_value',
                'europe': 'eur',
                'dollar': 'usd',
                'ruble': 'rub',
                }

counter: int = 0
while counter != len(data_d):
    data_d[data_keys[counter] + str(len(data_keys[counter]))] = data_d.pop(data_keys[counter])
    counter += 1

print("Result using a while loop:", data_d)
