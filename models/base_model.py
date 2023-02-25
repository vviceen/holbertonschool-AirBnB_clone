#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ print the class, the id, and instance method """
        return f"[{self.__class__.__name__}] ({self.id}) {vars(self)}"

    def save(self):
        """ update time method """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        result = dict(vars(self))
        result.update({"__class__" : self.__class__.__name__})
        result.update({'created_at': self.created_at.isoformat()})
        result.update({"updated_at": self.updated_at.isoformat()})

        return result
