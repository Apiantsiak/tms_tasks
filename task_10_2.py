# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.


class Car:

    def __init__(self, brand, model, year_of_manufacture, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_manufacture = year_of_manufacture
        self.__speed = speed

    def move_faster(self):
        self.__speed += 5

    def move_slower(self):
        self.__speed -= 5

    def backward_movement(self):
        self.__speed *= -1

    def stop_moving(self):
        self.__speed *= 0

    def get_speed_info(self):
        return self.__speed


car_audi = Car("Audi", "RS2", 1995)

for i in range(12):
    if i <= 5:
        car_audi.move_faster()
        print(f"Speed is {car_audi.get_speed_info()} km/h",
              f"{'-' * car_audi.get_speed_info()}>")
    elif 5 < i <= 10:
        car_audi.move_slower()
        print(f"Speed is {car_audi.get_speed_info()} km/h",
              f"{'-' * car_audi.get_speed_info()}>")
    else:
        car_audi.stop_moving()
        print(f"Speed is {car_audi.get_speed_info()} km/h",
              f"{'-' * car_audi.get_speed_info()}>")
        car_audi.stop_moving()
        car_audi.move_faster()
        car_audi.backward_movement()
        print(f"<{'-' * -car_audi.get_speed_info()}",
              f"Reverse speed is {car_audi.get_speed_info()} km/h")
