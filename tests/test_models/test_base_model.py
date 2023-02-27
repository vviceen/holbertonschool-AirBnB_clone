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

        self.assertEqual(type(dict_model), dict)
        self.assertEqual(type(dict_model["created_at"]), str)
        self.assertEqual(type(dict_model["updated_at"]), str)

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
        m = BaseModel()
        m_print = f'[{m.__class__.__name__}] ({m.id}) {m.__dict__}'

        self.assertEqual(m_print, m.__str__())

    def test_save(self):
        """@FileStorage.save runs?"""
        my_model = BaseModel()
        my_model.save()
        x = storage.all().get(f"BaseModel.{my_model.id}")
        self.assertEqual(my_model, x)


if __name__ == "__main__":
    unittest.main()








