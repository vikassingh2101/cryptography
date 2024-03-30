# Polyalphabetic substitution cipher
# C = C0,C1,...,Cn-1 = E[(k0,k1,...,km-1) , (p0,p1,...,pn-1)] where m < n


def encryption(key, plaintext):
    ciphertext = ""
    key_index = 0
    for char in plaintext.upper():
        ciphertext += chr((ord(char) - 65 + ord(key[key_index].upper()) - 65) % 26 + 65)
        key_index = (key_index + 1) % len(key)

    return ciphertext


def decryption(key, ciphertext):
    plaintext = ""
    key_index = 0
    for char in ciphertext.upper():
        plaintext += chr((ord(char) - 65 - (ord(key[key_index].upper()) - 65)) % 26 + 97)
        key_index = (key_index + 1) % len(key)

    return plaintext


while True:
    print("***** Vignere Cipher *****")
    option = input("Enter E for encrytion or D for decryption or X for exit:")
    if option == 'E':
        plaintext = input("Enter plaintext:")
        key = input("Enter key:")
        print("Encrypted message:" + encryption(key, plaintext))
    elif option == 'D':
        ciphertext = input("Enter ciphertext:")
        key = input("Enter key:")
        print("Decrypted message:" + decryption(key, ciphertext))
    elif option == 'X':
        exit(0)
    else:
        print("Invalid choice")
