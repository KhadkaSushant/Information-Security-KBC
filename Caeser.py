def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Shift within uppercase or lowercase letters
            offset = 65 if char.isupper() else 97
            shifted = (ord(char) - offset + shift) % 26 + offset
            result += chr(shifted)
        else:
            result += char  # Non-alphabetical characters remain unchanged

    return result


def caesar_cipher_decrypt(cipher_text, shift):
    return caesar_cipher_encrypt(cipher_text, -shift)


# Example usage
plain_text = "Hello, World!"
shift_value = 3

encrypted = caesar_cipher_encrypt(plain_text, shift_value)
decrypted = caesar_cipher_decrypt(encrypted, shift_value)

print("Original Text:", plain_text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
w