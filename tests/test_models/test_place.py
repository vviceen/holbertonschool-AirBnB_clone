#!/usr/bin/python3
"""Tests on Place class"""
import unittest
from models.place import Place


class Test_attributes_methods_Place(unittest.TestCase):
    def test_city_id(self):
        t_place = Place()
        self.assertTrue(not t_place.name)
        self.assertTrue(type(t_place.name) is str)

    def test_user_id(self):
        t_place = Place()
        self.assertTrue(not t_place.name)
        self.assertTrue(type(t_place.name) is str)

    def test_name(self):
        t_place = Place()
        self.assertTrue(not t_place.name)
        self.assertTrue(type(t_place.name) is str)

    def test_description(self):
        t_place = Place()
        self.assertTrue(not t_place.name)
        self.assertTrue(type(t_place.name) is str)

    def test_number_rooms(self):
        t_place = Place()
        self.assertTrue(t_place.number_rooms == 0)
        self.assertTrue(type(t_place.number_rooms) is int)

    def test_number_bathrooms(self):
        t_place = Place()
        self.assertTrue(t_place.number_bathrooms == 0)
        self.assertTrue(type(t_place.number_bathrooms) is int)

    def test_max_guest(self):
        t_place = Place()
        self.assertTrue(t_place.max_guest == 0)
        self.assertTrue(type(t_place.max_guest) is int)

    def test_price_by_night(self):
        t_place = Place()
        self.assertTrue(t_place.price_by_night == 0)
        self.assertTrue(type(t_place.price_by_night) is int)

    def test_latitude(self):
        t_place = Place()
        self.assertTrue(t_place.latitude == 0.0)
        self.assertTrue(type(t_place.latitude) is float)

    def test_longitude(self):
        t_place = Place()
        self.assertTrue(t_place.longitude == 0.0)
        self.assertTrue(type(t_place.longitude) is float)

    def test_amenity_ids(self):
        t_place = Place()
        self.assertTrue(not t_place.amenity_ids)
        self.assertTrue(type(t_place.amenity_ids) is list)
