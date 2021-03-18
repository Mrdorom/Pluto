"""
-------------------------------------------------
File Name：   format_response
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask import jsonify
from config import DefaultConfig


def format_response(res):
    res_key = res.keys()
    if "code" not in res_key:
        res["code"] = 0
    if "message" not in res_key:
        res["message"] = DefaultConfig.MSG_MAP.get(res['code'],'')
    if "data" not in res_key:
        res["data"] = []
    return jsonify(res)
