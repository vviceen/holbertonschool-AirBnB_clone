#!/usr/bin/python3
"""City Class model"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class
    ----------
    state_id : str
        empty string by default, here put @State.id

    name : str
        empty string by default
    """
    state_id = ""
    name = ""
