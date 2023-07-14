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
<<<<<<< HEAD
        A constructor method that when a new instance
        of the class is created. Inside this method,
        we initialize three instance attributes

        self.id: stores a unique ID using the uuid.uuid4()
        function and convert it to a string using str().
        self.created_at: stores current date and time.

        If kwargs is empty, it creates the id and created_at
        attributes as before.  If kwargs is not empty, it sets
        the attributes from the dictionary and converts
        the created_at and updated_at strings to datetime objects.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
        else:
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
=======
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
>>>>>>> 5cf723acfac871b997b4760177b461ff3b13b5a9

    def save(self):
        """
        Updates the updated_at attribute with the current timestamp
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
<<<<<<< HEAD
        Returns a dictionary representation of the instance, including
        all the instance attributes stored in __dict__. The __class__ key
=======
        Returns all the instance attributes stored in __dict__. The __class__ key 
>>>>>>> 5cf723acfac871b997b4760177b461ff3b13b5a9
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
