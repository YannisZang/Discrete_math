from fraction import Fraction

print(Fraction(31, 177) + Fraction(29, 59))


def gcd(a, b):
    assert a >= 0, b >= 0 and a + b > 0

    if a == 0 or b == 0:
        return max(a, b)

    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d

    return 1


print(gcd(24, 16))