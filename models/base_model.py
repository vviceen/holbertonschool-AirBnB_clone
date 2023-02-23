#!/usr/bin/python3
"""Holds abstract class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models.__init__ import storage

class BaseModel():
    """
    BaseModel:
        Abstract base class

    Attributes
    ----------
    id : str
        UUID of instance

    created_at : str
        datetime of instance creation

    update_at : str
        datetime of instance modification

    Methods
    -------
    save : public method
        update update_at attribute with
        datime.today method

    to_dict : public method
        return a dict representation of
        the instance

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' and key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)

        elif args:
            storage.new(args)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates @update_at attribute"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Return self.__dict__ of instance"""
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        a_dict = self.__dict__.copy()
        a_dict.update({"__class__" : self.__class__.__name__})

        return a_dict
