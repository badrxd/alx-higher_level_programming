#!/usr/bin/python3
""" Module represent class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string represent the list_dictionaries
        Args:
            list_dictionaries(dit): object
        Returns:
            The JSON string representation of the
            list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
