"""
-------------------------------------------------
File Name：   project
Description :
Author :       shili
date：          2021/3/18
-------------------------------------------------
Change Activity: 2021/3/18:
-------------------------------------------------
"""
__author__ = 'shili'

from datetime import datetime

from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource,reqparse
from apps.models import ProjectModel
from utils.format_response import format_response


class Project(Resource):

    def __init__(self):
        self.parse = reqparse.RequestParser()

    @jwt_required()
    def post(self):
        """"""
        self.parse.add_argument("project_name",type=str,required=True,help="项目名称必填")
        self.parse.add_argument("project_desc",type=str,help="项目描述")
        args = self.parse.parse_args()
        project_name = args.get("project_name")
        project_desc = args.get("project_desc")
        # 获取当前用户ID
        user_id = get_jwt_identity().get("user_id")
        project_obj = ProjectModel.objects(project_name=project_name).first()
        if project_obj:
            res = {"code":1000,"message":"项目已存在","data":{}}
            return format_response(res)
        project = ProjectModel(project_name=project_name,project_desc=project_desc,owner=user_id,create_time=datetime.utcnow().strftime("%Y-%m%d %H:%M:%S"))
        project.save()
        res = {"code": 0, "message": "success", "data": {"project_id":project.project_id,"project_name":project_name,"project_desc":project_desc}}
        return format_response(res)


