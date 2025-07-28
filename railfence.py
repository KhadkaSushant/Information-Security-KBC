def rail_fence_encrypt(text, key):
    # Create the rail matrix
    rail = [['' for _ in range(len(text))] for _ in range(key)]

    direction_down = False
    row = 0

    for i in range(len(text)):
        # Change direction when top or bottom rail is reached
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Place character in the rail
        rail[row][i] = text[i]

        # Move to next row in direction
        row += 1 if direction_down else -1

    # Concatenate all characters from rails
    result = ''
    for r in rail:
        result += ''.join(r)
    return result


def rail_fence_decrypt(cipher, key):
    # Create the rail matrix
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]

    # Mark the places with '*'
    direction_down = None
    row, index = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][i] = '*'
        row += 1 if direction_down else -1

    # Fill the matrix with cipher text
    idx = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and idx < len(cipher):
                rail[i][j] = cipher[idx]
                idx += 1

    # Read the matrix to reconstruct the plain text
    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result += rail[row][col]
        col += 1
        row += 1 if direction_down else -1

    return result


# Example usage
plain_text = "HELLOTHISISRAILFENCE"
key = 3

encrypted = rail_fence_encrypt(plain_text, key)
decrypted = rail_fence_decrypt(encrypted, key)

print("Original Text:", plain_text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
