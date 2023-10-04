#!/usr/bin/python3
""" Write the first class """
import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id: integer, no test required
        """
        # This ensures that each object created
        # without specifying an id receives a
        # unique id starting from 1 and
        # incrementing with each new object.
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON str rep of list_objs"""
        file = cls.__name__ + ".json"
        with open(file, "w") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                fd.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        file = cls.__name__ + ".json"
