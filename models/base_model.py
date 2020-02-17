#!/usr/bin/python3
"""Model Base """
import uuid
import models
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """class Base"""
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")

                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())  # unique id
            self.created_at = datetime.now()  # datetime when is created
            self.updated_at = datetime.now()  # date when is updated
            storage.new(self)

    def __str__(self):
        """ print() __str__ method """
        """" For pep8 validation"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.created_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''''returns a dictionary with all keys/value of the instance'''
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["updated_at"] = self.updated_at.strftime(
                                                    "%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    @property
    def id(self):
        return self.id
