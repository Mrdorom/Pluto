"""
-------------------------------------------------
File Name：   interface_tags
Description :
Author :       shili
date：          2021/3/23
-------------------------------------------------
Change Activity: 2021/3/23:
-------------------------------------------------
"""
__author__ = 'shili'

from flask_restful import Resource,reqparse
from utils.log import logger


class Interface(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.logger = logger()