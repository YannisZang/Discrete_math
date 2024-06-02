# find counterexample

from itertools import combinations

for n in range(100):
    if int(str(2 ** n)[:2]) == 17:
        print(f'2**{n}={2 ** n}')


def is_prime(n):
    return n != 1 and all(n % d != 0 for d in range(2, n))


print(next(n for n in range(2, 100) if
           not is_prime(n * n - n + 41)))


print(next(n for n in range(2, 100) if
           not is_prime(pow(2, pow(2, n)) + 1)))


for a, b, c in combinations(range(1, 20), 3):
    if a ** 2 + b ** 2 == c ** 2:
        print(f'{a}**2 + {b}**2 = {c}**2')


for a, b, c in combinations(range(1, 100), 3):
    if a ** 3 + b ** 3 == c ** 3:
        print(f'{a}**3 + {b}**3 = {c}**3')

