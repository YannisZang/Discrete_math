# Finds the minimal divisor>1 of the given integer m>1
def min_divisor(m):
    for d in range(2, m + 1):
        if m % d == 0:
            return d
        # optimization:
        if d * d > m:
            return m


def is_prime(m):
    return m == min_divisor(m)


def factoring(m):
    if is_prime(m):
        return [m]
    else:
        divisor = min_divisor(m)
        factors = factoring(m // divisor)
        factors.append(divisor)
        return factors


for i in (101, 60, 1001, 2 ** 32 + 1, 2 ** 64 + 1):
    print(f'Factoring of {i}: {factoring(i)}')