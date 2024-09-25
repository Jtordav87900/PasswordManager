from database.schema import create_user, create_password_entry, get_user_info
from passwordHashing.crypto import encrypt_text, decrypt_text
from database.getDB import obtain_session

# Create a user
with obtain_session() as session:
    user = create_user("Jtordav87900", "Pass123", "jamesdak231@gmail.com", session)[0]
    print("User ID: " + str(user.id))  # Access user.id while session is open

    # Create password entries with encryption
    create_password_entry(user.id, "google.com", "jamesdak231@gmail.com", "password123", session)
    create_password_entry(user.id, "minecraft.com", "jamesdak231@gmail.com", "password123", session)
    create_password_entry(user.id, "google.com", "jamesdak231@gmail.com", "password123", session)

# Retrieve user info and print decrypted passwords
with obtain_session() as session:
    userInfo = get_user_info("Jtordav87900", session)

    print(userInfo)
    for entry in userInfo['password_entries']:
        userID = userInfo['user.id']
        unencrypted_pass = entry['password']
        print("Unencrypted Password: "+ unencrypted_pass)
        password = decrypt_text(entry['password'], userID)
        print(f"Website: {entry['website']}, Username: {entry['username']}, Decrypted Password: {password}")
    print("\n\n")
