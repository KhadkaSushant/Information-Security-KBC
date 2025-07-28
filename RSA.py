import random

# Function to compute GCD (Euclidean Algorithm)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd_val, x, _ = extended_gcd(e, phi)
    return x % phi if gcd_val == 1 else None

# Check for primality (basic)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Generate a small prime number
def generate_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # common choice
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Encrypt a message (as integer)
def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

# Decrypt a message (as integer)
def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

# Example usage
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = 123  # must be less than n
cipher = encrypt(message, public_key)
decrypted = decrypt(cipher, private_key)

print("\nOriginal Message:", message)
print("Encrypted Cipher:", cipher)
print("Decrypted Message:", decrypted)
