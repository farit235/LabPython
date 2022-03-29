import os
import sys

def menu():
    while True:
        menu = int(input("Choose menu type: 1 - encode; 2 - decode; 3 - quit\n"))

        if menu == 1:
            encrypt()
        if menu == 2:
            decrypt()
        if menu == 3:
            break
        else:
            print("Enter right command!")

def encrypt():
    degree = int(input("\nEnter degree of encoding (1/2/4/8): "))

    text_len = os.stat('encoded.txt').st_size
    img_len = os.stat('1.bmp').st_size
    if text_len >= (img_len * degree / 8 - 54):
        print("Too long text")
        return

    start_bmp = open("1.bmp", 'rb')
    encode_bmp = open("encode.bmp", 'wb')
    text = open("encoded.txt", 'r')

    first54 = start_bmp.read(54)  # write first 54 bits
    encode_bmp.write(first54)

    text_mask, img_mask = create_mask(degree)
    print("text: {0:b}; image: {1:b}".format(text_mask, img_mask))
    print(bin(0b11111111 & text_mask))
    print(bin(0b11111111 & img_mask))

    # byte = start_bmp.read(1)
    # print(byte)
    # byte = int.from_bytes(byte, sys.byteorder)
    # print(bin(byte))

    # symbol = text.read(1)
    # print(bin(ord(symbol)))

    # if read all file -> exit file
    while True:
        symbol = text.read(1)
        if not symbol:
            break
        print("\nSymbol: " + symbol + " bin: " + bin(ord(symbol)))
        symbol = ord(symbol)

        for byte_amount in range(0, 8, degree):
            img_byte = int.from_bytes(start_bmp.read(1), sys.byteorder) & img_mask
            bits = symbol & text_mask
            bits >>= (8-degree)

            print("img {0}, bits {1:b}, num {1:d}".format(img_byte, bits))

            img_byte |= bits

            print("Encoded: " + str(img_byte))
            print("Writing: " + str(img_byte.to_bytes(1,sys.byteorder)))

            encode_bmp.write(img_byte.to_bytes(1, sys.byteorder))
            symbol <<= degree

    print(start_bmp.tell())
    encode_bmp.write(start_bmp.read())  # считываем все до конца файла и записываем в encode


    text.close()
    encode_bmp.close()
    start_bmp.close()

def create_mask(degree):
    text_mask = 0b11111111
    img_mask = 0b11111111

    text_mask <<= 8-degree
    text_mask %= 256
    img_mask <<= degree
    return text_mask, img_mask

def decrypt():
    degree = int(input("\nEnter degree of encoding (1/2/4/8): "))
    to_read = int(input("\nHow many symbols to read: "))
    img_len = os.stat('encode.bmp').st_size
    if to_read >= (img_len * degree / 8 - 54):
        print("Too long")
        return

    text = open('decode.txt', 'w')
    encoded_bmp = open('encode.bmp', 'rb')
    encoded_bmp.seek(54)

    text_mask, img_mask = create_mask(degree)
    img_mask = ~img_mask

    read = 0
    while read < to_read:
        symbol = 0

        for bits_range in range(0, 8, degree):
            img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask  # берем последний degree битов
            symbol <<= degree
            symbol |= img_byte

        print("Symbol: " + str(read) + " is ", chr(symbol))
        read += 1
        text.write(chr(symbol))



    text.close()
    encoded_bmp.close()


menu()