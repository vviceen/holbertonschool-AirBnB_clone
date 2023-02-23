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
        __objects.update({f"{self.__class__.__name__}.{self.id}":obj})

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as a_file:
            json.dump(self.__objects, a_file)

    def reload(self):
        if os.path.exist(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as a_file:
                self.__objects = json.load(a_file)
        else:
            pass
