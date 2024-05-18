#!/usr/bin/env python

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


# Function to encrypt data using DES
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext


# Function to decrypt data using DES
def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size)
    return plaintext.decode()


# Example usage
if __name__ == "__main__":
    key = b'12345678'  # DES key must be 8 bytes long
    plaintext = "Hello, DES!"

    print("Key:", key)
    print("Plaintext:", plaintext)

    # Encrypt
    ciphertext = des_encrypt(key, plaintext)
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt
    decrypted_text = des_decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text)
