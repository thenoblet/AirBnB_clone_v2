#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """Defines the State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", backref="states", cascade="all, delete, delete-orphan"
        )

    elif getenv("HBNB_TYPE_STORAGE") == "file":

        @property
        def cities(self):
            """Returns a list of cities with the same state_id"""
            # print(f"Getting cities for state: {self.id}") # debug
            city_list = []
            for city in models.storage.all(City).values():
                # print(f"Checking city: {city}")  # Debug statement
                if city.state_id == self.id:
                    city_list.append(city)
                    # print(f"Added city: {city}")  # Debug statement
            # print(f"City list for state {self.id}: {city_list}")
            return city_list
