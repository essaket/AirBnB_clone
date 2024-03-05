#!/usr/bin/python3
"""__init__ imports modules and packages """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
