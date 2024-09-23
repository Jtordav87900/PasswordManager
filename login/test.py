from login.loginScript import login_function
from database.schema import create_user
from database.getDB import obtain_session

with obtain_session() as session:
    create_user("Jtordav87900", "GreenHouse123", session)
    print(login_function("jtordav87900", "GreenHouse123", session))
    print(login_function("Jtordav87900", "GeenHouse123", session))
    print(login_function("Jtordav87900", "GreenHouse123", session))