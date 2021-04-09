"""
-------------------------------------------------
File Name：   log
Description :
Author :       shili
date：          2021/3/22
-------------------------------------------------
Change Activity: 2021/3/22:
-------------------------------------------------
"""
__author__ = 'shili'


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/11/17 10:02
# @Author : dorom
# @File : log.py
# @Software: PyCharm

import logging,os,time


base_path = os.path.abspath('.')
log_path = base_path+"/log"
if not os.path.exists(log_path):
    os.mkdir(log_path)


# 单例模式
class Log(object):
    __flag = None

    def __new__(cls, *args, **kwargs):
        if not cls.__flag:
            cls.__flag = super().__new__(cls)
        return cls.__flag

    def __init__(self,file):
        if 'logger' not in self.__dict__:
            logger = logging.getLogger()
            logger.setLevel(level=logging.INFO)
            timestamp = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            log_file = log_path + "/" +file+"_"+str(timestamp) + ".log"
            filehandle = logging.FileHandler(log_file, encoding='utf-8')
            streamhandle = logging.StreamHandler()
            logger.addHandler(filehandle)
            logger.addHandler(streamhandle)
            format = logging.Formatter('%(asctime)s:%(levelname)s:%(lineno)s:%(message)s:%(pathname)s:%(funcName)s')
            filehandle.setFormatter(format)
            streamhandle.setFormatter(format)
            self.logger = logger

    def return_logger(self):
        return self.logger


def logger(file="L"):
    return Log(file).return_logger()