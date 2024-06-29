def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1

    k = 1
    while (1 - k * n) % a != 0:
        k = k + 1

    s = (1 - n * k) / a
    k = s % n
    x = (k * b) % n

    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
    return x


print(divide(2, 7, 9))
print(divide(1, 5, 7))