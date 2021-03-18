"""
-------------------------------------------------
File Name：   __init__.py
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask import Blueprint

api = Blueprint('app',__name__)

from apps import urls
