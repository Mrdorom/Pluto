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
from app.models import Project
from app.schema import ProjectSchema
from utils.format_response import format_response
from utils.log import logger

logger = logger()


class ProjectAll(Resource):

    def __init__(self):
        self.parse = reqparse.RequestParser()

    @jwt_required()
    def post(self, *args, **kwargs):
        """
        创建项目
        :return:
        """
        self.parse.add_argument("project_name", type=str, required=True, help="项目名称必填")
        self.parse.add_argument("project_desc", type=str, help="项目描述")
        args = self.parse.parse_args()
        project_name = args.get("project_name")
        project_desc = args.get("project_desc")
        # 获取当前用户ID
        user_id = get_jwt_identity().get("user_id")
        project_obj = Project.objects(project_name=project_name).first()
        if project_obj:
            res = {"code": 1000, "message": "项目已存在", "data": {}}
            return format_response(res)
        project = Project(project_name=project_name, project_desc=project_desc, owner=user_id,
                               create_time=datetime.utcnow().strftime("%Y-%m%d %H:%M:%S"))
        project.save()
        res = {"code": 0, "message": "success",
               "data": {"project_id": project.project_id, "project_name": project_name, "project_desc": project_desc,
                        "owner": user_id}}
        return format_response(res)

    @jwt_required()
    def get(self):
        """
        获取所有项目
        :return: project obbject
        """
        self.parse.add_argument("page",type=int,default=1,help="页码")
        self.parse.add_argument("per_page",type=int,default=10,help="每页显示数量")
        args = self.parse.parse_args()
        page = args.get('page')
        per_page = args.get('per_page')
        try:
            pagination = Project.objects().paginate(page=page, per_page=per_page, error_out=True)
            articles = pagination.items
            article_schema = ProjectSchema(many=True)
            data = article_schema.dump(articles)
        except:
            data = []
        res = {"code": 0, "message": "success", "data": data}
        return format_response(res)


class ProjectHolder(Resource):

    def __init__(self):
        self.parse = reqparse.RequestParser()

    @jwt_required()
    def get(self,project_id):
        """
        获取单个项目ID
        :param project_id:  项目id
        :return:
        """
        logger.error("logger-------------------")
        project_obj = Project.objects(project_id=project_id).first()
        if project_obj:
            data = {"project_id": project_id, "project_name": project_obj.project_name,
                    "project_desc": project_obj.project_desc, "owner": project_obj.owner}
            res = {"code": 200, "message": "success", "data": data}
            return format_response(res)
        res = {"code": 1000, "message": "项目不存在", "data": {}}
        return format_response(res)