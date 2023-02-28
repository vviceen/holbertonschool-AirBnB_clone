#!/usr/bin/python3
"""Tests on City class"""
import unittest
from models.city import City


class Test_attributes_methods_City(unittest.TestCase):
    """ tests for two strings """
    def test_state_id(self):
        t_city = City()
        self.assertTrue(not t_city.name)
        self.assertTrue(type(t_city.name) is str)

    def test_name(self):
        t_city = City()
        self.assertTrue(not t_city.name)
        self.assertTrue(type(t_city.name) is str)
