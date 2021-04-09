"""
-------------------------------------------------
File Name：   schema
Description :
Author :       shili
date：          2021/3/22
-------------------------------------------------
Change Activity: 2021/3/22:
-------------------------------------------------
"""
__author__ = 'shili'
from app.extend import ma


class ProjectSchema(ma.Schema):

    class Meta:
        fields = ("project_id", "project_name", "project_desc", "owner","create_time")


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)