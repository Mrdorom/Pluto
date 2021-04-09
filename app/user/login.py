"""
-------------------------------------------------
File Name：   login
Description : 用户登录
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.models import User
from utils.format_response import format_response
from utils.serialize_type_func import validate_email


class Login(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()

    def post(self):
        self.parse.add_argument("email", type=validate_email, required=True, help="用户邮箱必填")
        self.parse.add_argument("password", type=str, required=True, help="用户名密码必填")

        agrs = self.parse.parse_args()
        email = agrs.get("email")
        password = agrs.get("password")
        user_obj = User.objects(email=email).first()
        if user_obj:
            password_status = check_password_hash(user_obj.password,password)
            if password_status:
                user_name = user_obj.user_name
                # access_token = create_access_token(identity="{0}+{1}+{2}".format(user_obj.user_id,user_obj.user_name,email))
                access_token = create_access_token(identity={"user_id":user_obj.user_id,"user_name":user_obj.user_name,"email":email})
                data = {"user":{"user_id":user_obj.user_id,"user_name":user_name,"acceess_token":access_token}}
                return format_response({"code": 0, "message": "success", "data": data})
            return format_response({"code":1000,"message":"账号密码错误","data":email})
        else:
            return format_response({"code":1000,"message":"用户不存在","data":email})