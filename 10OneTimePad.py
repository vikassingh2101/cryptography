#!/usr/bin/env python

# Polyalphabetic substitution cipher - One to many substitution
# Key length same as plaintext length
# C = C0,C1,...,Cn-1 = E[(k0,k1,...,kn-1) , (p0,p1,...,pn-1)]
# Ci = (pi ^ ki) mod 26
# Pi = (ci ^ ki) mod 26
# Same as Vernam cipher but for each message completely new key to be used


def encryption(key, plaintext):
    ciphertext = ""
    for index in range(len(plaintext)):
        ciphertext += chr((((ord(plaintext[index].upper()) - 65) ^ (ord(key[index].upper()) - 65)) % 26 ) + 65)

    return ciphertext


def decryption(key, ciphertext):
    plaintext = ""
    for index in range(len(ciphertext)):
        plaintext += chr((((ord(ciphertext[index].upper()) - 65) ^ (ord(key[index].upper()) - 65)) % 26 ) + 97)

    return plaintext


while True:
    print("***** One Time Pad Cipher *****")
    option = input("Enter E for encrytion or D for decryption or X for exit:")
    if option == 'E':
        plaintext = input("Enter plaintext:")
        key = input("Enter key of same length as plaintext:")
        print("Encrypted message:" + encryption(key, plaintext))
    elif option == 'D':
        ciphertext = input("Enter ciphertext:")
        key = input("Enter key of same length as ciphertext:")
        print("Decrypted message:" + decryption(key, ciphertext))
    elif option == 'X':
        exit(0)
    else:
        print("Invalid choice")
