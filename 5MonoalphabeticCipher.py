# Replaces each letter with a letter from key space
# One to one mapping between plaintext alphabet and ciphertext alphabet
# Assumptions:
#   Plaintext is small case
#   Ciphertext is upper case

def encryption(key, plaintext):
    ciphertext = ""
    for p in plaintext:
        if p == ' ':
            ciphertext += ' '
        else:
            ciphertext += key[ord(p) - 97]

    return ciphertext


def decryption(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        if c == ' ':
            plaintext += ' '
        else:
            plaintext += chr(key.index(c) + 97)

    return plaintext


while True:
    print("***** Monoalphabetic Cipher *****")
    option = input("Enter E for encrytion or D for decryption or X for exit:")
    if option == 'E':
        plaintext = input("Enter plaintext in small case:")
        key = input("Enter key (all upper case letters arranged in random order):")
        print("Encrypted message in upper case:" + encryption(key, plaintext))
    elif option == 'D':
        ciphertext = input("Enter ciphertext in upper case:")
        key = input("Enter key (all upper case letters arranged in random order):")
        print("Decrypted message in lower case:" + decryption(key, ciphertext))
    elif option == 'X':
        exit(0)
    else:
        print("Invalid choice")
