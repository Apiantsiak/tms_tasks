# Ex2
# Реализовать вычисление факториала через генератор
# n!=1⋅2⋅3⋅...⋅(n−2)⋅(n−1)⋅n


from math import factorial


def factorials_collection(collection_size: int):
    zero_fact = 1
    a = 1
    for i in range(collection_size + 1):
        if not i:
            yield zero_fact
            continue
        a *= i
        yield a


def test_check_calculation():
    assert list(factorials_collection(10)) == [factorial(numb) for numb in range(11)]
    assert list(factorials_collection(10))[10] == factorial(10)
