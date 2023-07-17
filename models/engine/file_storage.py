#!/usr/bin/python3
"""Defining File Storage"""
import json
import sys
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def serialize(self):
        """Serializes objects to a JSON file"""
        obj_dict = {}
        for obj_id, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                if isinstance(obj, User):
                    obj_dict[f"{obj.__class__.__name__}.{obj_id}"] = obj.to_dict()
                else:
                    obj_dict[obj_id] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def deserialize(self):
        """Deserializes objects from a JSON file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for obj_key, obj_data in obj_dict.items():
                    class_name, instance_id = obj_key.split(".")
                    if class_name == "User":
                        obj = User(**obj_data)
                    else:
                        obj = BaseModel(**obj_data)
                        self.__objects[f"{class_name}.{instance_id}"] = obj
        except FileNotFoundError:
            pass
