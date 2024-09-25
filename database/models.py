from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    salt = Column(String, nullable=False)

    # Relationship to PasswordEntry
    password_entries = relationship("PasswordEntry", back_populates="user")

class PasswordEntry(Base):
    __tablename__ = 'password_entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    website = Column(String, nullable=False)
    username = Column(String, nullable=False)
    # email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="password_entries")
