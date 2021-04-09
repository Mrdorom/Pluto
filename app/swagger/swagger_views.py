"""
-------------------------------------------------
File Name：   swigger_views
Description :
Author :       shili
date：          2021/3/23
-------------------------------------------------
Change Activity: 2021/3/23:
-------------------------------------------------
"""
__author__ = 'shili'


from flask_restful import Resource,reqparse
from app.models import Swagger
from utils.format_response import format_response
from utils.log import logger
from .swagger_parser import SwaggerParser

logger = logger()


class SwaggerHolder(Resource):

    def __init__(self):
        self.parse = reqparse.RequestParser()

    def post(self):
        self.parse.add_argument("path",type=str,required=True)
        self.parse.add_argument("project_id",type=int,required=True)
        agrs = self.parse.parse_args()
        path = agrs.get("path")
        project_id = agrs.get("project_id")
        obj = Swagger.objects(project_id=project_id).first()
        if obj:
            return format_response({"code":1000,"data":"项目数据已存在","message":"fail"})
        try:
            #  添加项目 swigger 数据
            swagger_parser = SwaggerParser(path)
            json_contents = swagger_parser.get_json_contents_holder()
            logger.info(type(json_contents))
            swigger = Swagger(project_id=project_id, swagger_content=json_contents)
            swigger.save()
        except Exception as e:
            logger.error("项目保存 swagger 数据失败 {0}".format(str(e)))
            response = {"code": 1000, "data": "项目保存 swagger 数据失败", "message": "fail"}
            return format_response(response)
        try:
            # 将解析好的 api 存储到 interfaceLibrary
            swagger_parser.parser_interface(project_id,json_contents)
            response = {"code":200,"data":{"project_id":project_id},"message":"success"}
        except Exception as save_interfaceLibrary_error:
            swigger.delete(project_id=project_id)
            response = {"code":1000,"data":save_interfaceLibrary_error,"message":"fail"}
        return format_response(response)

    # def put(self):
    #     self.parse.add_argument("path", type=str, required=True,help="项目 path swigger 必填")
    #     self.parse.add_argument("project_id", type=int, required=True,help="项目 project_id 必填")
    #     agrs = self.parse.parse_args()
    #     path = agrs.get("path")
    #     project_id = agrs.get("project_id")
    #     swigger_parser = SwiggerParser(path)
    #     swigger_parser.main()
    #     obj = SwiggerModel.objects(project_id=project_id).first()
    #     if obj:
    #         obj.update(swigger_content=swigger_parser.contents)
    #         tags_list = json.loads(swigger_parser.contents).get("tags", [])
    #         for tags in tags_list:
    #             pass
    #         return format_response({})
    #     return format_response({"code": 201, "message": "项目swigger数据不存在"})