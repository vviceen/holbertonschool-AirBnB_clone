#!/usr/bin/python3
"""tests on Amenity class"""
import unittest
from models.amenity import Amenity


class Test_attributes_methods_Amenity(unittest.TestCase):
    """ Test class for Amenity """
    def test_name(self):
        """ tests for str name """
        amenity = Amenity()
        self.assertTrue(not amenity.name)
        self.assertTrue(type(amenity.name) is str)
