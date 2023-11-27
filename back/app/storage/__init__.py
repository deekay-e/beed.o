#!/usr/bin/python3
''' Initialize the models package '''
from os import getenv


storage_t = settings.
if storage_t == 'db':
    from storage.db import DBStorage
    storage = DBStorage()
else:
    from storage.file import FileStorage
    storage = FileStorage()

storage.reload()
