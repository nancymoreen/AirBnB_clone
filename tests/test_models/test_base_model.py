#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(
                my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_model.created_at)

        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

        print(my_model)
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            value_type = type(my_model_json[key])
            print("\t{}: ({}) - {}".format(
                key, value_type, my_model_json[key]))


if __name__ == '__main__':
    unittest.main()
