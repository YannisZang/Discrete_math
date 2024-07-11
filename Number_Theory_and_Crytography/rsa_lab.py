import sys, threading


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)


def Decrypt(ciphertext, p, q, exponent):
    phi = (p - 1) * (q - 1)
    d = InvertModulo(exponent, phi)
    return ConvertToStr(PowMod(ciphertext, d, p * q))

p = 779849711281
q = 748173698927
e = 1018651
ciphertext = 148784435264686331994392
decrypt_first_puzzle = Decrypt(ciphertext, p, q, e)
print(decrypt_first_puzzle)
print()


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  for text in potential_messages:
    if ciphertext == Encrypt(text, modulo, exponent):
      return text
  return "don't know"

ciphertext = 336184023047118677086739
modulo = 1110014195838866450995043
exponent = 767549
potential_messages = ["http://goo.gl/", "http://tinyurl.com/", "http://bit.ly/", "http://t.co/", "http://ow.ly/", "https://is.gd/", "https://buff.ly/", "http://adf.ly/", "http://bit.do/"]
decrypt_second_puzzle = DecipherSimple(ciphertext, modulo, exponent, potential_messages)
print(decrypt_second_puzzle)

secret_link = decrypt_second_puzzle + decrypt_first_puzzle
print(secret_link)


def DecipherSmallPrime(ciphertext, modulo, exponent):
  for q in range(2, 1000000):
    if modulo % q == 0:
      small_prime = q
      big_prime = modulo // q
      return Decrypt(ciphertext, small_prime, big_prime, exponent)
  return "don't know"


ciphertext = 1
modulo = 100000000000000000
exponent = 1
decrypt_third_puzzle = DecipherSmallPrime(ciphertext, modulo, exponent)
print(decrypt_third_puzzle)


def IntSqrt(n):
    low = 1
    high = n
    iterations = 0
    while low < high and iterations < 5000:
        iterations += 1
        mid = (low + high + 1) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid - 1
    return low


def DecipherSmallDiff(ciphertext, modulo, exponent):
    # Substitute this implementation with your code from question 5 of the "RSA Quiz".
    small_prime = IntSqrt(modulo)
    big_prime = modulo // small_prime
    return Decrypt(ciphertext, small_prime, big_prime, exponent)


ciphertext = 1
modulo = 10000000000000000000
exponent = 1
decrypt_fourth_puzzle = DecipherSmallDiff(ciphertext, modulo, exponent)
print(decrypt_fourth_puzzle)


second_secret_link = decrypt_third_puzzle + decrypt_fourth_puzzle
print(second_secret_link)


def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)

def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  # Substitute this implementation with your code from question 6 of the "RSA Quiz".
  for common_prime in range(2, 1000000):
    if first_modulo % common_prime == 0 and second_modulo % common_prime == 0:
      q1 = first_modulo // common_prime
      q2 = second_modulo // common_prime
      return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))
  return ("unknown message 1", "unknown message 2")

first_ciphertext = 1
first_modulo = 1000000000000000
first_exponent = 1
second_ciphertext = 1
second_modulo = 9999999999999999
second_exponent = 1

decrypt_sixth_puzzle = DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent)
print(decrypt_sixth_puzzle)


def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)
  return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # Substitute this implementation with your code from question 7 of the "RSA Quiz".
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  return ConvertToStr(IntSqrt(first_ciphertext * second_ciphertext))

first_ciphertext = 1
first_modulo = 100000000000000
second_ciphertext = 1
second_modulo = 999999999999999

decrypt_seventh_puzzle = DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo)
print(decrypt_seventh_puzzle)


final_answer = decrypt_sixth_puzzle[0] + decrypt_sixth_puzzle[1] + decrypt_seventh_puzzle
print(final_answer)


