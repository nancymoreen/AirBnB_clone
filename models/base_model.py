#!/usr/bin/python3
"""
Creating a class BaseModel that defines all
common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel

class BaseModel:
    """
    This defines a class named BaseModel. This class
    will serve as a base class for other classes and
    contains common attributes and methods.
    """

    def __init__(self):
        """
        A constructor method that when a new instance
        of the class is created. Inside this method,
        we initialize three instance attributes

        self.id: stores a unique ID using the uuid.uuid4()
        function and convert it to a string using str().
        self.created_at: stores current date and time.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        a string representation of the object that return a
        string that includes the class name, the instance's ID,
        and the instance's attributes (stored in self.__dict__).
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current timestamp
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance, including
        all the instance attributes stored in __dict__. The __class__ key 
        ith the class name, and the created_at and updated_at attributes
        are converted to ISO-formatted strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
