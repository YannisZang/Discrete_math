
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))


def factorial(n):
    assert (n > 0)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# amount starts with 8, and can be combination of 3 and 5
def change(amount):
    assert (amount >= 8)
    if amount == 8:
        return [3, 5]
    if amount == 9:
        return [3, 3, 3]
    if amount == 10:
        return [5, 5]

    coins = change(amount - 3)
    coins.append(3)
    return coins


print(change(10))


def change2(amount):
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]

    coins = change2(amount - 5)
    coins.append(5)
    return coins


print(change2(30))


