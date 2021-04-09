"""
-------------------------------------------------
File Name：   demo
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import jsonify
from app.swagger.swagger_parser import SwaggerParser


class Demo(Resource):

    # @jwt_required()
    def get(self):
        # current_user = get_jwt_identity()
        # print(current_user.get("user_id"))
        swagger_holder = SwaggerParser("/Users/shili/Downloads/swaggerApi.json")
        json_contents = swagger_holder.get_json_contents_holder()
        swagger_holder.parser_interface(1,json_contents)
        return jsonify({"data":111})