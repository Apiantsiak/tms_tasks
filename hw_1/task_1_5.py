# The legs of a right-angled triangle are given. Find its hypotenuse and area.


triangle_leg_1 = int(input("Enter first leg: "))
triangle_leg_2 = int(input("Enter second leg: "))

hypotenuse_squared = (triangle_leg_1 ** 2) + (triangle_leg_2 ** 2)
hypotenuse_length = hypotenuse_squared ** 0.5
triangle_area = (triangle_leg_1 * triangle_leg_2) * 0.5

print(hypotenuse_length)
print(triangle_area)
