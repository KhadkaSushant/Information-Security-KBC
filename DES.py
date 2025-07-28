from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt(plain_text, key):
    # Ensure the key is 8 bytes
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long.")

    cipher = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text


def des_decrypt(cipher_text, key):
    if len(key) != 8:
        raise ValueError("Key must be 8 bytes long.")

    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(cipher_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()


# Example usage
plain_text = "HELLODES"
key = "8bytekey"  # Must be 8 bytes

# Encrypt
cipher_text = des_encrypt(plain_text, key)
print("Encrypted (hex):", cipher_text.hex())

# Decrypt
decrypted_text = des_decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
