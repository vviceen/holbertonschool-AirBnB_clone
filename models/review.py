#!/usr/bin/python3
"""Review Class model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    ------------

    Attributes
    ----------
    place_id : str
        empty string by defoult, put Place.id here

    user_id : str
        empty string by defoult, put User.id here

    text : str
        empty string by defoult, its a place for user comments
    """
    place_id = ""
    user_id = ""
    text = ""
