"""
Holds FileStorage class
for serialization/deserialization
"""
import json
import os.path


class FileStorage:
    """
    Serializes and deserializes objects
    to/from a JSON file
    """

    __file_path = "/root/holbertonschool-AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict_to_save = {}
        for key, obj in self.__objects.items():
            dict_to_save[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                dict_loaded = json.load(file)
                for key, value in dict_loaded.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = eval(class_name)(**value)
