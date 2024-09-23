from passwordHashing.hashmypassword import hash_password
from database.getDB import obtain_session
from database.schema import get_user_by_username, get_user_info

def login_function(username, password, session):
    """
    Authenticates a user by verifying their password against the hashed password stored in the database.

    Args:
        username (str): The username of the user trying to log in.
        password (str): The plaintext password provided by the user for login.
        session (Session): An active database session.

    Returns:
        int: Returns 1 if login is successful, -1 if the password is incorrect, and 0 if the user does not exist.
    """
    # Retrieve the user from the database based on the username
    existing_user = get_user_by_username(session, username)
    if not existing_user:
        print("User does not exist")
        return 0  # Return 0 if the user is not found

    # Retrieve additional information about the user
    user_info = get_user_info(username, session)
    if 'password_hash' not in user_info:
        print("User info is incomplete")
        return -1  # Return -1 if the essential user info is missing

    # Retrieve the stored salt used during the user's password hash creation
    user_salt = user_info['salt']

    # Hash the provided password with the stored salt
    password_hash, _ = hash_password(password, user_salt)

    # Compare the hashed password with the stored hash
    if password_hash == user_info['password_hash']:
        print("Login Successful")
        return 1  # Return 1 if the password is correct
    else:
        print("Password incorrect")
        return -1  # Return -1 if the password does not match the stored hash

