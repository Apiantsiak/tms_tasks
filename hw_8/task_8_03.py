# Дан список чисел. Вернуть список, где каждый число переведено в строку [5, 3] -> [‘5’, ‘3’]


from random import randint
from typing import List


rand_ls: List[int] = [randint(1, 10) for _ in range(randint(10, 30))]
convert_ls: List[str] = list(map(lambda numb: str(numb), rand_ls))

print(convert_ls)
