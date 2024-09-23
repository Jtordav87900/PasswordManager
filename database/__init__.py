from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User, Base, PasswordEntry

# Database URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///D:/Code/Password Manager/db/db.db"

# Create the engine; this will automatically create the SQLite database file if it doesn't exist
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a Session maker
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure that the tables are created (this creates the tables if they don't exist yet)
Base.metadata.create_all(engine)

# Session management
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

print("Database setup completed.")
