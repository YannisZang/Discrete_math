def fast_modular_exponentiation(b, e, m):
    assert m > 0 and e >= 0
    if e == 0:
        return 1
    if e == 1:
        return b
    if e % 2 == 0:
        return fast_modular_exponentiation((b * b) % m, e // 2, m)
    else:
        return (fast_modular_exponentiation(b, e - 1, m) * b) % m


for p in (2 ** 32 + 1, 2 ** 512 + 1):
    for a in (2, 3):
        print(fast_modular_exponentiation(a, p - 1, p))