# Multi-letter encryption cipher
# 5 x 5 matrix of letters
# To make accurate depiction, 2-d martrix has been used


def constructKeyMatrix(key):
    letterList = []
    for letter in key:
        if letter == 'J':
            letter = 'I'
        if letter not in letterList:
            letterList.append(letter.upper())

    ascii = 65
    remaining = 25 - len(letterList)
    i = 0
    while i < remaining:
        if chr(ascii) == 'J':
            ascii += 1
            continue
        if chr(ascii) not in letterList:
            letterList.append(chr(ascii))
            i += 1
        ascii += 1

    keyMatrix = []
    for i in range(0, len(letterList), 5):
        keyMatrix.append(letterList[i:i+5])

    return keyMatrix


def prepareDigrams(message):
    digrams = []
    i = 0
    prev = ""
    while i < len(message):
        if len(prev) == 0:
            prev += message[i]
            i += 1
        else:
            if message[i] == prev:
                prev += 'X'
            else:
                prev += message[i]
                i += 1
            digrams.append(prev)
            prev = ""

    if len(prev) == 1:
        prev += 'X'
        digrams.append(prev)
        prev = ""

    return digrams


def computeCipherDigrams(keyMatrix):
    digramMap = {}
    for i in range(65, 65+26):
        for j in range(65, 65+26):
            for index, row in enumerate(keyMatrix):
                if chr(i) in row:
                    row_i, col_i = index, row.index(chr(i))
                if chr(j) in row:
                    row_j, col_j = index, row.index(chr(j))

            if row_i == row_j:
                a = keyMatrix[row_i][(col_i + 1) % 5]
                b = keyMatrix[row_j][(col_j + 1) % 5]
            elif col_i == col_j:
                a = keyMatrix[(row_i + 1) % 5][col_i]
                b = keyMatrix[(row_j + 1) % 5][col_j]
            else:
                a = keyMatrix[row_i][col_j]
                b = keyMatrix[row_j][col_i]

            digramMap[chr(i)+chr(j)] = a + b

    return digramMap


def computePlaintextDigrams(keyMatrix):
    digramMap = {}
    for i in range(65, 65+26):
        for j in range(65, 65+26):
            for index, row in enumerate(keyMatrix):
                if chr(i) in row:
                    row_i, col_i = index, row.index(chr(i))
                if chr(j) in row:
                    row_j, col_j = index, row.index(chr(j))

            if row_i == row_j:
                a = keyMatrix[row_i][(col_i - 1) % 5]
                b = keyMatrix[row_j][(col_j - 1) % 5]
            elif col_i == col_j:
                a = keyMatrix[(row_i - 1) % 5][col_i]
                b = keyMatrix[(row_j - 1) % 5][col_j]
            else:
                a = keyMatrix[row_i][col_j]
                b = keyMatrix[row_j][col_i]

            digramMap[chr(i)+chr(j)] = a + b

    return digramMap


def encryption(key, plaintext):
    keyMatrix = constructKeyMatrix(''.join(key.upper().split(' ')))
    cipherDigramMap = computeCipherDigrams(keyMatrix)
    digrams = prepareDigrams(''.join(plaintext.upper().split(' ')))
    ciphertext = ""
    for digram in digrams:
        ciphertext += cipherDigramMap[digram]

    return ciphertext


def decryption(key, ciphertext):
    keyMatrix = constructKeyMatrix(''.join(key.upper().split(' ')))
    plaintextDigramMap = computePlaintextDigrams(keyMatrix)
    digrams = prepareDigrams(''.join(ciphertext.upper().split(' ')))
    plaintext = ""
    for digram in digrams:
        plaintext += plaintextDigramMap[digram]

    return plaintext


while True:
    print("***** Playfair Cipher *****")
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
