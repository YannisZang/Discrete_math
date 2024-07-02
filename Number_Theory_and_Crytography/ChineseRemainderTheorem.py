def ChineseRemainderTheorem(n1, r1, n2, r2):
    (d, x, y) = ExtendedEuclid(n1, n2)
    assert n1 * x + n2 * y == d  # == gcd(n1, n2)
    y = -y
    assert n1 * x - n2 * y == d
    assert (r2 - r1) % d == 0
    x *= (r2 - r1) // d
    y *= (r2 - r1) // d
    assert n1 * x - n2 * y == r2 - r1
    return (n1 * x + r1) % (n1 * n2)


def ExtendedEuclid(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = ExtendedEuclid(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


print(ExtendedEuclid(686579304, 26855093))
print(ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))