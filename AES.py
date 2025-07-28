from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plain_text, key):
    # Ensure key is 16, 24, or 32 bytes long
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long (128/192/256 bits).")

    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plain_text.encode(), AES.block_size))

    return iv + encrypted  # Prepend IV for use in decryption


def aes_decrypt(cipher_text, key):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long.")

    iv = cipher_text[:16]
    encrypted = cipher_text[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    return decrypted.decode()


# Example usage
key = b'ThisIsA16ByteKey'  # 16 bytes = 128-bit AES key
plain_text = "Hello AES Encryption!"

cipher_text = aes_encrypt(plain_text, key)
print("Encrypted (hex):", cipher_text.hex())

decrypted_text = aes_decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)

