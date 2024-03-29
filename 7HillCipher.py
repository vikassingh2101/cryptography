# Multi-letter encryption cipher
# Involves matrix multiplication
# C = PK mod 26
# P = CK-1 mod 26
import math


def computeSubmatrix(matrix, row, col):
    submatrix = []
    for i in range(len(matrix)):
        if i == row:
            continue
        submatrix.append(matrix[i][0:col] + matrix[i][col+1:])

    return submatrix


def computeDeterminant(matrix):
    if len(matrix) == 1 and len(matrix[-1]) == 1:
        return matrix[0][0]

    determinant = 0
    for i in range(len(matrix)):
        submatrix = computeSubmatrix(matrix, 0, i)
        minor = computeDeterminant(submatrix)
        cofactor = minor * ((-1)**(i))
        determinant += matrix[0][i] * cofactor

    return determinant


def computeCofactorMatrix(matrix):
    cofactorMatrix = []
    for i in range(len(matrix)):
        cofactorMatrix.append([])
        for j in range(len(matrix)):
            submatrix = computeSubmatrix(matrix, i, j)
            minor = computeDeterminant(submatrix)
            cofactor = minor * ((-1)**(i+j))
            cofactorMatrix[-1].append(cofactor)

    return cofactorMatrix


def transposeMatrix(matrix):
    transposedMatrix = []
    for i in range(len(matrix)):
        transposedMatrix.append([])
        for j in range(len(matrix)):
            transposedMatrix[-1].append(matrix[j][i])

    return transposedMatrix


def computeMatrixInverse(matrix):
    determinant = computeDeterminant(matrix) % 26
    for i in range(1, 26):
        if (determinant * i) % 26 == 1:
            determinant = i
            break

    cofactorMatrix = computeCofactorMatrix(matrix)
    transposedCofactorMatrix = transposeMatrix(cofactorMatrix)
    if determinant == 0:
        print("Inverse Matrix cannot be computed.")
    else:
        for i in range(len(transposedCofactorMatrix)):
            for j in range(len(transposedCofactorMatrix)):
                transposedCofactorMatrix[i][j] *= determinant
                transposedCofactorMatrix[i][j] %= 26

    return transposedCofactorMatrix


def convert_string_to_matrix(text):
    size = math.ceil(math.sqrt(len(text)))
    text = text.upper()
    matrix = []
    for i in range(size):
        matrix.append([ord(char)-65 for char in text[i*size: (i+1)*size]])
    for i in range(size - len(matrix[-1])):
        matrix[-1].append(ord('X')-65)

    return matrix


def encryption(key, plaintext):
    matrix = convert_string_to_matrix(key)
    determinant = computeDeterminant(matrix)
    if determinant == 0:
        print("Inverse of key matrix cannot be computed as determinant is 0")
        return
    ciphertext = ""
    for i in range(0, len(plaintext), len(matrix)):
        substring = plaintext[i:i+len(matrix)].upper()
        ord_substring = [ord(char)-65 for char in substring]
        encrypted_vector = []
        # len(substring) = len(matrix)
        for i in range(len(substring)):
            product = 0
            for j in range(len(substring)):
                product += ord_substring[j] * matrix[j][i]
            encrypted_vector.append(product % 26)

        encrypted_substring = [chr(num + 65) for num in encrypted_vector]
        ciphertext += ''.join(encrypted_substring)

    return ciphertext


def decryption(key, ciphertext):
    matrix = convert_string_to_matrix(key)
    determinant = computeDeterminant(matrix)
    if determinant == 0:
        print("Inverse of key matrix cannot be computed as determinant is 0")
        return
    inverseMatrix = computeMatrixInverse(matrix)
    plaintext = ""
    for i in range(0, len(ciphertext), len(inverseMatrix)):
        substring = ciphertext[i:i+len(inverseMatrix)].upper()
        ord_substring = [ord(char)-65 for char in substring]
        encrypted_vector = []
        # len(substring) = len(matrix)
        for i in range(len(substring)):
            product = 0
            for j in range(len(substring)):
                product += ord_substring[j] * inverseMatrix[j][i]
            encrypted_vector.append(product % 26)

        encrypted_substring = [chr(int(num) + 65) for num in encrypted_vector]
        plaintext += ''.join(encrypted_substring)

    return plaintext


while True:
    print("***** Hill Cipher *****")
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
