from passwordHashing.crypto import encrypt_text, decrypt_text

# Encrypt a message
encrypted_message = encrypt_text("password123")
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_text(encrypted_message)
print(f"Decrypted message: {decrypted_message}")  # No need for .decode() here since it's already a string
