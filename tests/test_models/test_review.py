#!/usr/bin/python3
"""Tests on Review class"""
import unittest
from models.review import Review


class Test_attributes_methods_Review(unittest.TestCase):
    def test_place_id(self):
        t_review = Review()
        self.assertTrue(not t_review.place_id)
        self.assertTrue(type(t_review.place_id) is str)
    def test_user_id(self):
        t_review = Review()
        self.assertTrue(not t_review.user_id)
        self.assertTrue(type(t_review.user_id) is str)
    def test_text(self):
        t_review = Review()
        self.assertTrue(not t_review.text)
        self.assertTrue(type(t_review.text) is str)
