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


def primes_list(n):
    lst = []
    boundary = 2
    # primes < boundary are in lst
    while len(lst) < n:
        if is_prime(boundary):
            lst.append(boundary)
        boundary += 1

    return lst


print('The first ten primes:')
print(primes_list(10))