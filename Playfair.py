def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            prepared += a + "X"
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += "X"
    return prepared


def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(text, key):
    text = prepare_text(text)
    matrix = generate_key_matrix(key)
    encrypted = ""

    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(matrix, text[i], text[i+1])
    return encrypted


def playfair_decrypt(cipher_text, key):
    matrix = generate_key_matrix(key)
    decrypted = ""

    for i in range(0, len(cipher_text), 2):
        decrypted += decrypt_pair(matrix, cipher_text[i], cipher_text[i+1])
    return decrypted


# Example usage
key = "MONARCHY"
plain_text = "HELLO WORLD"

cipher_text = playfair_encrypt(plain_text, key)
decrypted_text = playfair_decrypt(cipher_text, key)

print("Key Matrix:")
for row in generate_key_matrix(key):
    print(row)

print("\nOriginal Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
