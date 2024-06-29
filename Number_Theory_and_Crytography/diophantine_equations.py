def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  d = gcd(a, b)
  t = c / d
  x_1 = -1
  y_1 = (d - x_1 * a) / b

  return (t*x_1, t*y_1)


print(diophantine(10, 6, 14))