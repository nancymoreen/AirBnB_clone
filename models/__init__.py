#!/usr/bin/python3
"""Intializing magic method for models dir"""
from .file_storage import FileStorage


storage = FileStorage()
storage.reload()
