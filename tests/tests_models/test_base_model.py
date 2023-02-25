#!/usr/bin/python3
"""Tests on BaseModel"""
import unittest
from models.base_model import BaseModel
from os import path


class Test_attributes_methods_BaseModel(unittest.TestCase):
    """Let's rock"""
    def test_save(self):
        """Instance is saved and updated?"""
        my_model = BaseModel()
        up_time = my_model.updated_at
        my_model.save()

        self.assertTrue(up_time != my_model.updated_at)
        self.assertTrue(path.exists('file.json'))

    def test_to_dict(self):
        """There is a dict to serialize?"""
        my_model = BaseModel()
        dict_model = my_model.to_dict()

        print(dict_model)
        self.assertTrue(dict_model == my_model.to_dict())

    def test_id(self):
        """There is a Id?"""
        my_model = BaseModel()
        id_model = my_model.id

        print(id_model)
        self.assertTrue(id_model == my_model.id)

    def test_created_at(self):
        """created_at exists?"""
        my_model = BaseModel()
        created_model = my_model.created_at

        print(created_model)
        self.assertTrue(created_model == my_model.created_at)

    def test_str(self):
        """There is a str representation?"""
        my_model = BaseModel
        print(my_model)


if __name__ == "__main__":
    unittest.main()
