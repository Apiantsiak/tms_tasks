# Receive the number of "рублей" and "копеек" for input and output it in the correct form,
# for example, 3 "рубля", 1 "рубль" 25 "копеек", 3 "копейки".

rubles, coins = int(input("Enter value of rubles: ")), int(input("Enter value of coins: "))

rubles_ending: dict = {}
coins_ending: dict = {}

for numb in range(0, 1001):
    if numb % 10 == 1:
        rubles_ending[numb] = "рубль"
        coins_ending[numb] = "копейка"
    elif numb % 10 in range(2, 5):
        rubles_ending[numb] = "рубля"
        coins_ending[numb] = "копейки"
    else:
        rubles_ending[numb] = "рублей"
        coins_ending[numb] = "копеек"

print("{} {} {} {}".format(rubles, rubles_ending[rubles], coins, coins_ending[coins]))
