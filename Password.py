import bcrypt

# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

# Function to verify a password against a hash
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

# Example usage
if __name__ == "__main__":
    # Registration (hash and store this securely)
    user_password = "MySecureP@ssw0rd!"
    stored_hash = hash_password(user_password)
    print("Stored Hash:", stored_hash)

    # Authentication attempt
    input_password = input("Enter your password to login: ")
    if verify_password(input_password, stored_hash):
        print("Authentication successful! Welcome.")
    else:
        print("Authentication failed! Invalid password.")
