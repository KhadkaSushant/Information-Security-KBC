import pyotp
import time

# Step 1: Generate a secret key for the user (do this once at setup/registration)
secret = pyotp.random_base32()
print("Your secret key (store this safely):", secret)

# Step 2: Generate a provisioning URI for QR code (optional)
# This URI can be used to generate a QR code that apps like Google Authenticator can scan
user_email = "user@example.com"
issuer_name = "MyApp"
uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user_email, issuer_name=issuer_name)
print("Provisioning URI for QR code:", uri)

# Step 3: Generate the current OTP (for demonstration)
totp = pyotp.TOTP(secret)
current_otp = totp.now()
print("Current OTP:", current_otp)

# Simulate user input of OTP and verify
user_input = input("Enter the OTP from your authenticator app: ")

if totp.verify(user_input):
    print("Authentication successful!")
else:
    print("Authentication failed! Invalid OTP.")
