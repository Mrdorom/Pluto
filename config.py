"""
-------------------------------------------------
File Name：   config
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'
import os


class DefaultConfig(object):
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = 'super-secret'  # Change this!

    MONGODB_SETTINGS = {
        'db': 'flask',
        'host': '127.0.0.1',
        'port': 27017,
        'connect': True,
        'username': 'admin',
        'password': '123456',
        'authentication_source': 'admin'
    }

    MSG_MAP = {
        0: 'success',
        101: "can not find object",
        102: "save object error",
        200: "success",
        201: "数据错误",
        500: "服务器换异常"
    }
