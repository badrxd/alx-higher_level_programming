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

    @classmethod
    def save_to_file(cls, list_objs):
        """save the JSON string representation of the list_objs
        to a file
        Args:
            cls(cls): the class
            list_objs (object): list of instances
        """
        filename = cls.__name__ + ".json"
        ls = []
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                ls = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation of json_string
        Args:
            json_string (str): string representing the list of dic
        Returns:
            A list of json string
        """
        if len(json_string) == 0 or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns the instance with allthe attributes
        Args:
            dictionary (dict): A dictionary
        Returns:
            An instance with attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
