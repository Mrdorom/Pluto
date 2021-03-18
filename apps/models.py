"""
-------------------------------------------------
File Name：   models
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from apps.extend import mongo
from datetime import datetime


class User(mongo.Document):
    """
    用户模型类，记录用户基础信息
    password 加密 password_hash = generate_password_hash（hash）
    """
    user_id = mongo.SequenceField(primary_key=True)
    email = mongo.EmailField(required=True,max_length=128,unique=True)
    user_name = mongo.StringField(required=True,max_length=128,unique=True)
    password = mongo.StringField(required=True,max_length=128)
    source_password = mongo.StringField(max_length=128)
    create_time = mongo.DateTimeField(default=datetime.utcnow().strftime("%Y-%m%d %H:%M:%S"))

    def __repr__(self):
        return "User(username={0},email={1})".format(self.user_name,self.email)


class ProjectModel(mongo.Document):
    """
    项目模型类
    """
    project_id = mongo.SequenceField(primary_key=True)
    project_name = mongo.StringField(required=True,unique=True,max_length=128)
    project_desc = mongo.StringField()
    owner = mongo.StringField()
    create_time = mongo.DateTimeField(default=datetime.utcnow().strftime("%Y-%m%d %H:%M:%S"))

    def __repr__(self):
        return "Project(project_id={0},project_name={1})".format(self.project_id,self.project_name)