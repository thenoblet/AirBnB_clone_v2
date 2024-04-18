#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    This class defines a user by various attributes

    Attributes:
        __tablename__ (str): The table name for the database.
        email (str): The email address of the user.
        password (str): The password for the user's login.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): One-to-many relationship with Place model.
        reviews (relationship):One-to-many relationship with Review model.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)


    places = relationship(
        "Place", backref="user", cascade="all, delete, delete-orphan"
    )
    reviews = relationship(
        "Review", backref="user", cascade="all, delete, delete-orphan"
    )
