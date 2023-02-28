#!/usr/bin/ptyhon3
"""" Tests for the file user.py """
import unittest
from models.user import User


class Test_attributes_methods_User(unittest.TestCase):
    """ tests for the class User """
    def test_email(self):
        t_user = User()
        self.assertTrue(not t_user.email)
        self.assertTrue(type(t_user.email) is str)

    def test_password(self):
        t_user = User()
        self.assertTrue(not t_user.password)
        self.assertTrue(type(t_user.password) is str)

    def test_first_name(self):
        t_user = User()
        self.assertTrue(not t_user.first_name)
        self.assertTrue(type(t_user.first_name) is str)


    def test_last_name(self):
        t_user = User()
        self.assertTrue(not t_user.last_name)
        self.assertTrue(type(t_user.last_name) is str)