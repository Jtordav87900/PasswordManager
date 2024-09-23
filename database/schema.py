from database.models import User, Base, PasswordEntry
from sqlalchemy import and_
from sqlalchemy.orm import Session
from database import get_session
from passwordHashing.crypto import encrypt_text
from passwordHashing.hashmypassword import hash_password, generate_salt

def create_user(Username, password, session):
    existing_user = get_user_by_username(session, Username)
    if existing_user:
        print(f"User {Username} already exists")
        return existing_user, -1

    # salty = generate_salt()
    hashed_password, salty = hash_password(password)
    new_user = User(username=Username, password_hash=hashed_password, salt=salty)
    session.add(new_user)
    session.flush()  # Flush to ensure ID is assigned
    print(f"User ID after flush: {new_user.id}")  
    session.commit()
    return new_user, 1

def get_user_info(username, session):
        user = get_user_by_username(session, username)
        if not user:
            print(f"{username} does not exist")
            return None
        
        password_entries = [{
            'website': entry.website,
            'username': entry.username,
            'password': entry.password  
        } for entry in user.password_entries]

        user_info = {
            'username': user.username,
            'password_hash': user.password_hash,
            'user.id' :user.id,
            'salt' :user.salt,
            'password_entries': password_entries
        }
        return user_info


def create_password_entry(user_id: int, website: str, username: str, password: str, session):
        # Check if a password entry already exists for the given website and user
        existing_entry = session.query(PasswordEntry).filter(and_(PasswordEntry.user_id == user_id, PasswordEntry.website == website)).first()
        if existing_entry:
            print(f"Password entry already exists for {website}")
            return existing_entry
        
        # Encrypt the password before storing it
        print("Before encryption: " + password)
        encrypted_password = encrypt_text(password, user_id)
        print("After encrpytion: " + encrypted_password)
        # Create a new password entry since it does not exist
        new_entry = PasswordEntry(user_id=user_id, website=website, username=username, password=encrypted_password)
        session.add(new_entry)
        try:
            session.commit()
            print(f"Password entry for {website} created successfully.")
            return new_entry
        except Exception as e:
            print(f"Error creating password entry: {e}")
            session.rollback()
            return None




def get_user_by_username(session, username):
     return session.query(User).filter(User.username == username).first()

