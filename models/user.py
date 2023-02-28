#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class Model
    ----------------
    email : str
        empty string by defoult

    password : str
        empty string by defoult

    first_name : str
        empty string by defoult

    last_name : str
        empty string by defoult
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
