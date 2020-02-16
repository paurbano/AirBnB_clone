#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances:
"""

import json
import os
import sys


class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON"""

    __file_path = ""  # path to the JSON file (ex: file.json)
    __objects = {}  # dictionary - store all objects by <class name>.id

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        print("sets in __objects the obj with key <obj class name>.id ")

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        print("serializes __objects to the JSON file (path: __file_path)")

    def reload(self):
        """ deserializes the JSON file to __objects """
        print("deserializes the JSON file to __objects")
