#!/usr/bin/python3
"""Refactored version using SQLAlchemy ORM"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost/example_db"
engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()


class User(Base):
    """User model mapped to the users table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


def create_user(username: str, email: str):
    """Add a new user using the ORM"""
    if not username or not email:
        print("Username and email are required.")
        return

    new_user = User(username=username, email=email)
    session.add(new_user)
    try:
        session.commit()
        print(f"User '{username}' created successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {e}")


def get_user_by_username(username: str):
    """Query a user by username using the ORM"""
    user = session.query(User).filter_by(username=username).first()
    return user


# Example usage
if __name__ == "__main__":
    create_user("john_doe", "john@example.com")
    user = get_user_by_username("john_doe")
    print(user)
