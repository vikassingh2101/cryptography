from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


def encrypt_AES_GCM(data, key):
    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (nonce, ciphertext, tag)


def decrypt_AES_GCM(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext


# Example usage:
if __name__ == "__main__":
    # Example data
    data = b"Hello, this is a secret message!"

    # Generate a 256-bit key using PBKDF2
    password = b"password"
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)

    # Encrypt the data
    nonce, ciphertext, tag = encrypt_AES_GCM(data, key)
    print("Ciphertext:", ciphertext.hex())

    # Decrypt the data
    decrypted_data = decrypt_AES_GCM(nonce, ciphertext, tag, key)
    print("Decrypted data:", decrypted_data.decode("utf-8"))
