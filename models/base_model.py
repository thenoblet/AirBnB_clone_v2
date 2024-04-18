#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
import models

Base = declarative_base()

class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    
    id = Column(String(60), unique=True, nullable=False, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            try:
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"]
                )
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"]
                )
            except (KeyError, ValueError):
                kwargs["updated_at"] = kwargs["created_at"] = datetime.now()

            kwargs.pop("__class__", None)
            self.__dict__.update(kwargs)

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())
    
    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        # Remove '_sa_instance_state' key if it exists
        if '_sa_instance_state' in dictionary:
            dictionary.pop("_sa_instance_state", None)
            
        return dictionary

    
    def delete(self):
        """ Deletes the current instance from the storage. """
        models.storage.delete(self)
