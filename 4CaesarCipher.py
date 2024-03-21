# Replaces each letter with a letter standing 3 places down
# Wrapped around when end is reached
# Algorithm is written with a general value k for shifting
# C = E(k,P) = (p+k) mod 26
# P = D(k,C) = (c-k) mod 26
# Assumptions:
#   Plaintext is small case
#   Ciphertext is upper case

def encryption(key, plaintext):
    ciphertext = ""
    for p in plaintext:
        if p == ' ':
            ciphertext += ' '
        else:
            ciphertext += chr(((ord(p) - 97 + key) % 26) + 65)

    return ciphertext


def decryption(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        if c == ' ':
            plaintext += ' '
        else:
            plaintext += chr(((ord(c) - 65 - key) % 26) + 97)

    return plaintext


while True:
    print("***** Caesar Cipher *****")
    option = input("Enter E for encrytion or D for decryption or X for exit:")
    if option == 'E':
        plaintext = input("Enter plaintext in small case:")
        key = int(input("Enter numerical key:"))
        print("Encrypted message in upper case:" + encryption(key, plaintext))
    elif option == 'D':
        ciphertext = input("Enter ciphertext in upper case:")
        key = int(input("Enter numerical key:"))
        print("Decrypted message in lower case:" + decryption(key, ciphertext))
    elif option == 'X':
        exit(0)
    else:
        print("Invalid choice")
