# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.


from random import randint, choice
from datetime import timedelta

times_arrival_ls = [timedelta(hours=randint(0, 12), minutes=randint(0, 60)) for i in range(5)]
time_departure_ls = [timedelta(hours=randint(13, 23), minutes=randint(0, 60)) for j in range(5)]

train_info = {'887B': [['Rome', choice(times_arrival_ls)],
                       ['Milan', choice(time_departure_ls)]
                       ],
              '411C': [['Paris', choice(times_arrival_ls)],
                       ['Brno', choice(time_departure_ls)]
                       ],
              '445C': [['Minsk', choice(times_arrival_ls)],
                       ['Brest', choice(time_departure_ls)]
                       ],
              '113F': [['London', choice(times_arrival_ls)],
                       ['Tokio', choice(time_departure_ls)]
                       ],
              }

travel_time = timedelta(hours=7, minutes=20)

for tr_numb, var in train_info.items():
    if var[1][1] - var[0][1] > travel_time:
        print(tr_numb, end="-")
        for i in var:
            for j in i:
                print(j, end=" ")
