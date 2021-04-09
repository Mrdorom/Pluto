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
from app.demo import Demo
from app.user.register import Register
from app.user.login import Login
from app.project.project_views import ProjectHolder, ProjectAll
from app.swagger.swagger_views import SwaggerHolder

apis = Api(api)

apis.add_resource(Demo,"/demo")
apis.add_resource(Register,"/user/register")
apis.add_resource(Login,"/user/login")
apis.add_resource(ProjectAll,"/project")
apis.add_resource(ProjectHolder,"/project/<int:project_id>")
apis.add_resource(SwaggerHolder,"/swigger")