#!/usr/bin/python3
""" New engine for our program. """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Class for the new engine. """
    __engine = None
    __session = None
    __models = [State, City, User, Place, Review]

    def __init__(self):
        """ Initializer for the instances of the class. """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects in the current
        database session."""
        objects = {}

        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for model in self.__models:
                for obj in self.__session.query(model):
                    objects[obj.__class__.__name__ + "." + obj.id] = obj

        return objects

    def new(self, obj):
        """ Add the object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session. """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and the session. """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """ Close function. """
        self.__session.close()
