#!/usr/bin/python3
"""Tests on State class"""
import unittest
from models.state import State

class Test_attributes_methods_State(unittest.TestCase):
    def test_name(self):
        t_state = State()
        self.assertTrue(not t_state.name)
        self.assertTrue(type(t_state.name) is str)
