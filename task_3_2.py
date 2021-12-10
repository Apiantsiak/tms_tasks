# There is a wedding in the N family. They decided to choose the place where they would celebrate
# depending on the number of people arriving in the morning.

# If there are more than 50 of them, they will order a restaurant, if there are 20 to 50 cafe,
# and if there are less than 20, they will celebrate at home.

# Display "restaurant", "cafe", "house" depending on the number of guests (read the variable from the console)

number_visitors = int(input("Enter count of visitors: "))

if number_visitors < 20:
    print("house")
elif 20 <= number_visitors < 50:
    print("cafe")
else:
    print("restaurant")
