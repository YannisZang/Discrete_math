# implement the function which computes b^(2^k) mod m using only around 2k modular multiplication
def FastModularExponentiation(b, k, m):
  assert m > 0 and k >= 0
  if k == 0:
    return b
  else:
    return FastModularExponentiation((b*b)%m, k-1,m)

print(FastModularExponentiation(3, 5, 10))


# implement the function which computes b^e mod m using around 2Log(n) modular multiplications

def FastModularExponentiation(b, e, m):
  assert m > 0 and e >= 0
  if e == 0:
    return 1
  if e == 1:
    return b
  if e % 2 == 0:
    return FastModularExponentiation((b*b) % m, e / 2, m)
  else:
    return (FastModularExponentiation(b, e - 1, m) * b) % m


print(FastModularExponentiation(3, 5, 10))