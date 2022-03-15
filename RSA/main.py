import sys
import math

p = 7
q = 13

def divider(n):
    i = 2
    j = 0  # флаг
    while i**2 <= n and j != 1:
        if n %i == 0:
            j = 1
        i += 1
    if j == 1:
        print("Это составное число")
        sys.exit()
    else:
        print("Это простое число")

divider(p)
divider(q)
n = p * q
Euler = (p-1) * (q-1)
print(n, Euler)
e = 5

m = math.gcd(n, e)
print(m)
if m == 1:
    open_key = (e, n)
    close_key = (0, 0)
    for k in range(100):
        d = ((k + 1) * Euler + 1) / e
        if str(d).split('.')[1] == '0':  # if 0 -> integer
            close_key = (int(d), n)
            break

    # dict
    symbols = {1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ё', 8: 'Ж',
               9: 'З', 10: 'И', 11: 'Й', 12: 'К', 13: 'Л', 14: 'М', 15: 'Н',
               16: 'О', 17: 'П', 18: 'Р', 19: 'С', 20: 'Т', 21: 'У', 22: 'Ф',
               23: 'Х', 24: 'Ц', 25: 'Ч', 26: 'Ш', 27: 'Щ', 28: 'Ъ', 29: 'Ы',
               30: 'Ь', 31: 'Э', 32: 'Ю', 33: 'Я', 34: ' ', 35: '0', 36: '1',
               37: '2', 38: '3', 39: '4', 40: '5', 41: '6', 42: '7', 43: '8',
               44: '9'}

    word = "КАФСИ"
    print(f'initial word = {word}')
    encoded_word = []

    reversed_symbols = {v: k for k, v in symbols.items()}
    print(f'open key = {open_key}')
    for i in word:
        encoded_word.append((reversed_symbols[i] ** open_key[0]) % open_key[1])

    print(f"encoded_word = {encoded_word}")

    decoded_word = []
    print(f'close key = {close_key}')
    for j in encoded_word:
        decoded_word.append(symbols[(j ** close_key[0]) % close_key[1]])

    decoded_word = "".join(decoded_word)
    print(f"decoded_word = {decoded_word}")
else:
    quit()






