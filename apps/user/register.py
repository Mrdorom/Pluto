"""
-------------------------------------------------
File Name：   register
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from datetime import datetime

from flask_restful import Resource,reqparse
from werkzeug.security import generate_password_hash

from apps.models import User
from utils.format_response import format_response
from utils.serialize_type_func import validate_email


class Register(Resource):

    def __init__(self):
        self.parse = reqparse.RequestParser()

    def post(self):
        self.parse.add_argument("email",type=validate_email,required=True,help="用户邮箱必填")
        self.parse.add_argument("user_name",type=str,required=True,help="用户名称必填")
        self.parse.add_argument("password",type=str,required=True,help="用户名密码必填")
        agrs = self.parse.parse_args()
        email = agrs.get("email")
        user_name = agrs.get("user_name")
        password = agrs.get("password")
        password_hash = generate_password_hash(password)
        # 检查用户名邮箱是否已存在
        user_obj = User.objects(user_name=user_name).first() or User.objects(email=email).first()
        if user_obj:
            data = {"user_name": user_obj.user_name,"email":user_obj.email}
            res = {"data": data,"code":1000,"message":"用户名或邮箱已存在"}
            return format_response(res)
        user = User(user_name=user_name,password=password_hash,source_password=password,email=email,create_time=datetime.utcnow().strftime("%Y-%m%d %H:%M:%S"))
        user.save()
        data = {"user_id":user.user_id,"email":email,"user_name":user_name}
        res = {"data":data}
        return format_response(res)


