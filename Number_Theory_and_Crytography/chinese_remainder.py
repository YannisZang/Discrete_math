from sympy import gcdex


def chinese_remainder_theorem(n1, r1, n2, r2):
    x, y, d = gcdex(n1, n2)
    assert n1 * x + n2 * y == d  # == gcd(n1, n2)
    y = -y
    assert n1 * x - n2 * y == d
    assert (r2 - r1) % d == 0
    x *= (r2-r1) // d
    y *= (r2-r1) // d
    assert n1 * x - n2 * y == r2 - r1
    return (n1 * x+r1) % (n1 * n2)


for n1, r1, n2, r2 in (
    (5, 3, 12, 7),
    (10, 3, 13, 8),
    (10, 3, 14, 1),
    (11, 3, 17, 7)
):
    result = chinese_remainder_theorem(n1, r1, n2, r2)
    print(f'If {r1} = x mod {n1}, and {r2} = x mod {n2}, then x={result}')