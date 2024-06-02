# logic

a = (6, 2, 4)
print(all((i % 2 == 0) for i in a))
a = (2, 7, 6)
print(all((i % 2 == 0) for i in a))


a = (1, 7, 9)
print(any((i % 2 == 0) for i in a))
a = (9, 2, 3)
print(any((i % 2 == 0) for i in a))


def is_divisible_by_3(x):
    return x % 3 == 0


lst = [5, 17, 6, 10]

print(not any([is_divisible_by_3(x) for x in lst]))
print(all([not is_divisible_by_3(x) for x in lst]))