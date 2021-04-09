"""
-------------------------------------------------
File Name：   request_comm
Description :
Author :       shili
date：          2021/3/22
-------------------------------------------------
Change Activity: 2021/3/22:
-------------------------------------------------
"""
__author__ = 'shili'

import requests
import abc


class BaseRequst(metaclass = abc.ABCMeta):

    def __init__(self,host,path,headers,body):
        self.host = host
        self.path = path
        self.headers = headers
        self.body = body

    @abc.abstractmethod
    def curl(self):
        pass


class Get(BaseRequst):

    def curl(self):
        pass

