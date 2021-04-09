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

from app.extend import mongo


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
    create_time = mongo.StringField(required=True)

    def __repr__(self):
        return "User(username={0},email={1})".format(self.user_name,self.email)


class Project(mongo.Document):
    """
    项目模型类
    """
    project_id = mongo.SequenceField(primary_key=True)
    project_name = mongo.StringField(required=True,unique=True,max_length=128)
    project_desc = mongo.StringField()
    owner = mongo.IntField()
    create_time = mongo.StringField(required=True)

    def __repr__(self):
        return "Project(project_id={0},project_name={1})".format(self.project_id,self.project_name)


class Swagger(mongo.Document):
    """
    项目swigger数据
    """
    project_id = mongo.IntField()
    swagger_content = mongo.StringField()


class InterfaceParamsModel(mongo.EmbeddedDocument):
    """
    Interface params 接口参数实体信息
    """
    name = mongo.StringField()
    params_location = mongo.StringField()
    required = mongo.BooleanField()
    params_type = mongo.StringField()
    description = mongo.StringField()


class InterfaceDataModel(mongo.EmbeddedDocument):
    """
    Interface Data 接口实体信息
    """
    path = mongo.StringField(required=True)   #APi请求路径
    summary = mongo.StringField()   # Api简介
    description = mongo.StringField()  # Api 说明文档
    consumes = mongo.ListField() # 消费
    method = mongo.StringField(required=True)   #api 请求方式
    parameters = mongo.EmbeddedDocumentListField(InterfaceParamsModel)  # 请求参数
    responses = mongo.DictField()  # 请求参数


class TagsDataModel(mongo.EmbeddedDocument):
    """
    Tags Data swagger Tags 实体信息
    """
    tags = mongo.StringField(max_length=128,required=True)
    interface_data = mongo.EmbeddedDocumentListField(InterfaceDataModel)


class InterfaceLibrary(mongo.Document):
    """
    接口项目库信息
    """
    project_id = mongo.IntField()
    interface = mongo.EmbeddedDocumentListField(TagsDataModel)