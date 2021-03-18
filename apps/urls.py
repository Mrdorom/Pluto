"""
-------------------------------------------------
File Name：   urls
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask_restful import Api
from . import api
from apps.demo import Demo
from apps.user.register import Register
from apps.user.login import Login
from apps.project.project import Project

apis = Api(api)

apis.add_resource(Demo,"/demo")
apis.add_resource(Register,"/user/register")
apis.add_resource(Login,"/user/login")
apis.add_resource(Project,"/project/add")