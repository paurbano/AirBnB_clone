#!/usr/bin/python3
""" module models """

from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel'}
storage = FileStorage()
storage.reload()
