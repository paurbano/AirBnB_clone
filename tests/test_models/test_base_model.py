#!/usr/bin/python3
""" Unit test BaseModel """

import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for class BaseModel"""

    def test_init_BaseModel(self):
        """test if an object is an type BaseModel"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_id(self):
        """ test that id is unique """
        my_objectId = BaseModel()
        my_objectId1 = BaseModel()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_strobject = BaseModel()
        _dict = my_strobject.__dict__
        string1 = "[BaseModel] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = BaseModel()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)


if __name__ == '__main__':
    unittest.main()
