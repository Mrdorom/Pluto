"""
-------------------------------------------------
File Name：   extend
Description : 本文件主要使用一些扩展
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'


from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

mongo = MongoEngine()
jwt = JWTManager()
ma = Marshmallow()