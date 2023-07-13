#!/usr/bin/python3
"""
Creating a class BaseModel that defines all
common attributes/methods for other classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This defines a class named BaseModel. This class
    will serve as a base class for other classes and
    contains common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing current BaseModel.
        
        Arguments:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        DT_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, DT_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current timestamp
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns all the instance attributes stored in __dict__. The __class__ key 
        ith the class name, and the created_at and updated_at attributes
        are converted to ISO-formatted strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Returns string representation of the class"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
