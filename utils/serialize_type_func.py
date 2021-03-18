"""
-------------------------------------------------
File Name：   serialize_type_func
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

import re
from utils.error_except import EmailError


def validate_email(email):
    """
    邮箱格式校验
    :param email:
    :return:
    """
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
        return email
    else:
        raise EmailError("邮箱:{}格式不正确".format(email))