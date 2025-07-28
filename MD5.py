import hashlib

def md5_hash_string(input_string):
    # Encode the string to bytes, then hash
    md5_hash = hashlib.md5(input_string.encode())
    return md5_hash.hexdigest()

# Example usage
text = "Hello, MD5!"
hashed = md5_hash_string(text)
print("Original Text:", text)
print("MD5 Hash:", hashed)
