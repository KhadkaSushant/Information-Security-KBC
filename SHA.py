import hashlib


def sha_hash(data, algorithm='sha256'):
    """
    Compute the SHA hash of the given data using the specified algorithm.

    Supported algorithms: 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    """
    if algorithm not in hashlib.algorithms_guaranteed:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_func = hashlib.new(algorithm)
    hash_func.update(data.encode())
    return hash_func.hexdigest()


# Example usage:
text = "Hello, SHA!"
for algo in ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
    print(f"{algo.upper()}:", sha_hash(text, algo))
