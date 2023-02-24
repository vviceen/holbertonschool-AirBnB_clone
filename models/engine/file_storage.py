#!/usr/bin/python3
"""
Holds FileStorage class
for serialization/deserialization
"""
from os import path
import json


class FileStorage():
    """
    DOC in proces
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        json_objs = {}
        for key, value in self.__objects.items():
            json_objs.update({key:value.to_dict()})

        with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
            json.dump(json_objs, a_file)

    def reload(self):
        from models.base_model import BaseModel
        if not path.exists(self.__file_path):
            return

        else:
            with open(self.__file_path, mode='r', encoding='utf-8') as a_file:
                self.__objects = {}
                json_loads = json.load(a_file)
                for key, value in json_loads.items():
                    self.__objects.update({key:BaseModel(**value)})
