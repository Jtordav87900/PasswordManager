from database.schema import create_user, get_user_by_username
from database.getDB import obtain_session

def sign_up(username, password, session):
    return create_user(username, password, session)

with obtain_session() as session:
   
    username = "Jtordav87900"
    password = "password12fa3"
    print(get_user_by_username(session, username))
    print(sign_up("Jtordav87900", "password123", session))
    print(sign_up("Jtordav87900", "password123", session))