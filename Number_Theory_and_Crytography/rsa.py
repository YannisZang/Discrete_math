from math import gcd
p, q = 5915587277, 2860486313

n = p * q
print(f'n={n}')


phi = (p - 1) * (q - 1)
print(f'phi={phi}')
e = 3
print(f'e={e}')
assert gcd(phi, e) == 1

# e*a mod phi == 1, result is a
d = pow(e, -1, phi)
print(f'd={d}')
assert d * e % phi == 1


def encode(m):
    assert 0 <= m < n
    return pow(m, e, n)


message = 92616855427
print(f'message: {message}')
cipher_text = encode(message)

print(f'ciphertext: {cipher_text}')


def decode(c):
    return pow(c, d, n)


print(f'decoded: {decode(cipher_text)}')
print()




