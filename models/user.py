#!/usr/bin/python3
"""Defining User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represeneting The User Class
    Attributes:
    email: User's email
    password: User's password
    first_name: User's First name
    last_name: User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
