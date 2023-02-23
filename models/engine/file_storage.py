#!/usr/bin/python3
"""
Holds FileStorage class
for serialization/deserialization
"""
from os import path


class FileStorage():
    """
    DOC in proces
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects.update({f"{objs.__class__.__name__.id}":})
