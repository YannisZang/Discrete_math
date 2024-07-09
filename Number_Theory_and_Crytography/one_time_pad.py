# the key = 0 means no change in the message, and k = 1 means bits reversal, like operation "xor"

from itertools import product


def encode(plain_text, private_key):
    assert plain_text in {0, 1} and private_key in {0, 1}
    return plain_text ^ private_key


def decode(cypher_text, private_key):
    assert cypher_text in {0, 1} and private_key in {0, 1}
    return cypher_text ^ private_key


for plaintext, private_key in product({0, 1}, repeat=2):
    ciphertext = encode(plaintext, private_key)
    print(f'key: {private_key}, '
          f'plaintext: {plaintext}, '
          f'ciphertext: {ciphertext}, '
          f'decoded: {decode(ciphertext, private_key)}')

print()


# conversions between hex string and regular string


def to_hex(plain_text):
    hex_codes = []
    for symbol in plain_text:
        hex_code = hex(ord(symbol)).replace('0x', '')
        if len(hex_code) == 1:
            hex_code = '0' + hex_code
        hex_codes.append(hex_code)
    return ''.join(hex_codes)


def to_str(hex_code):
    if hex_code:
        return chr(int(hex_code[:2], base=16)) + to_str(hex_code[2:])
    return ''


message = 'Hello World'
print(f'hex of {message} is: {to_hex(message)}')

code = '736f6d65206d657373616765'
print(f'str of {code} is: {to_str(code)}')
print()


def bitwise_xor(first_text, second_text):
    assert len(first_text) == len(second_text)
    return ''.join(format(int(s1, 16) ^ int(s2, 16), '01x')
                   for s1, s2 in zip(first_text, second_text))


message = 'secret message'
key = 'my secret keys'
print(f'hex of {message} is: {to_hex(message)}')
print(to_hex(key))

ciphertext = bitwise_xor(to_hex(message), to_hex(key))
print('ciphertext:', ciphertext)

recovered_message = to_str(bitwise_xor(ciphertext, to_hex(key)))
print('recovered message:', recovered_message)
print()

# see what happens if the same key is used to encrypt two different messages.
message1 = 'steal the secret'
message2 = 'the boy the girl'
key = 'supersecretverys'

ciphertext1 = bitwise_xor(to_hex(message1), to_hex(key))
ciphertext2 = bitwise_xor(to_hex(message2), to_hex(key))

print('ciphertext1:', ciphertext1)
print('ciphertext2:', ciphertext2)

xor_ciphertexts = bitwise_xor(ciphertext1, ciphertext2)
xor_messages = bitwise_xor(to_hex(message1), to_hex(message2))

print(xor_ciphertexts)
print(xor_messages)

if xor_ciphertexts == xor_messages:
    print('Xor of the ciphertexts is the same as xor of messages')
else:
    print('Xor of the ciphertexts differs from the xor of messages')


# guess
print()
def try_guessing_substring(substring, message_length, xor_messages):
    good_guesses = []
    for pos in range(message_length - len(substring) + 1):
        guess = to_hex(chr(0) * pos + substring +
                       chr(0) * (message_length - len(substring) - pos))
        other_message_part = to_str(
            bitwise_xor(guess, xor_messages)
        )[pos:pos + len(substring)]
        good_guess = True
        for i in range(len(other_message_part)):
            if not other_message_part[i].isalpha() and \
                    not other_message_part[i].isspace():
                good_guess = False
                break
        if good_guess:
            good_guesses.append((guess, pos, other_message_part))

    print('Good guesses:')
    for guess in good_guesses:
        print(f'position: {guess[1]}, '
              f'one message part: \"{substring}\", '
              f'another message part: \"{guess[2]}\"')


try_guessing_substring(' the ', len(message1), xor_messages)
try_guessing_substring('oy the ', len(message1), xor_messages)
