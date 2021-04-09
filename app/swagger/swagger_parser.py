"""
-------------------------------------------------
File Name：   swigger_content
Description :
Author :       shili
date：          2021/3/23
-------------------------------------------------
Change Activity: 2021/3/23:
-------------------------------------------------
"""
__author__ = 'shili'


import json
import re
import requests
from utils.log import logger
from app.models import InterfaceLibrary, InterfaceDataModel, InterfaceParamsModel, TagsDataModel

logger = logger()


class SwaggerParser(object):

    def __init__(self,url):
        self.url = url

    def _judge_path_or_url(self):
        """
        检查传入的地址是 path 还是 URL
        path: judge_status = True
        url: judge_status =False
        :param url:
        :return: judge_status
        """
        re_https = "https://"
        https_pattern = re.compile(re_https)
        re_http = "http://"
        http_pattern = re.compile(re_http)
        http_result = http_pattern.findall(self.url)
        # 默认 url 传入的是path， response_status = True
        judge_status = True
        if not http_result:
            https_result = https_pattern.findall(self.url)
            if https_result:
                judge_status = False
        else:
            judge_status = False
        return judge_status

    def _open_file(self):
        """
        :param url:
        :return:
        """
        with open(self.url,"r",encoding="UTF-8") as f:
            file_contents = f.read()
        return file_contents

    def _open_url(self):
        """
        :param url:
        :return:
        """
        url_contents = requests.get(self.url)
        return url_contents

    def _get_swagger_version(self,json_contents):
        """
        get swagger version
        :param json_contents:
        :return: version
        """
        swagger_version = json_contents.get("swagger",False)
        version = 1
        if swagger_version:
            version = 2
        openapi_version = json_contents.get("openapi",False)
        if openapi_version:
            version = 3
        return version

    def _get_swagger_info(self,json_contents):
        """
        get swagger info
        :param json_contents:
        :return:
        """
        swagger_info = json_contents.get("info",False)
        if swagger_info:
            return swagger_info

    def _get_base_path(self,json_contents):
        """
        get base path
        :param json_contents:
        :return:
        """
        base_path = json_contents.get("basePath")
        return base_path

    def _get_tags_list(self,json_contents):
        """
        get tags list
        :param json_contents:
        :return:
        """
        tags_list = json_contents.get("tags")
        return tags_list

    def _schemes(self,json_contents):
        """
        get schemes ---> https、http
        :param json_contents:
        :return:
        """
        schemes = json_contents.get("schemes")
        return schemes

    def _parser_ref(self,data):
        """
        解析内部关联数据 $ref
        :param data:
        :return:
        """
        ref1 = r"\$"
        paths_string = str(data)
        pattent = re.compile(ref1)
        paths_li = pattent.findall(paths_string)
        for li in paths_li:
            paths_string = re.sub(ref1, "", paths_string)
        paths_dict = eval(paths_string)
        return paths_dict

    def _parser_interface(self,project_id,json_contents):
        """
        解析 swagger 文档并将接口信息存储到 inteerface 库
        :param project_id:
        :param json_contents:
        """
        paths_dict = json_contents.get("paths")
        paths_dict = self._parser_ref(paths_dict)
        try:
            for interface_path,interface_values in paths_dict.items():
                interfacee_data_list = []
                tags_list = []
                for method, params_dict in interface_values.items():
                    tags_list_res = params_dict.get("tags",None)
                    summary = params_dict.get("summary",None)
                    description = params_dict.get("description",None)
                    consumes = params_dict.get("consumes",None)
                    parameters = params_dict.get("parameters",None)
                    responses = params_dict.get("responses",None)
                    logger.info(responses)
                    interfacee_data_object = InterfaceDataModel(path=interface_path,method=method,summary=summary,description=description,consumes=consumes)
                    parameters_list = []
                    if parameters:
                        for item in parameters:
                            name = item.get("name")
                            params_location = item.get("in")
                            required = item.get("required")
                            params_type = item.get("params_type")
                            description = item.get("description")
                            parameters_list.append(InterfaceParamsModel(name=name,params_location=params_location,required=required,params_type=params_type,description=description))
                            interfacee_data_object.parameters = parameters_list
                    else:
                        parameters_list.append(InterfaceParamsModel(name=None, params_location=None,required=None, params_type=None))
                        interfacee_data_object.parameters = parameters_list

                    interfacee_data_object.responses = responses
                    interfacee_data_list.append(interfacee_data_object)
                    if tags_list_res:
                        for tags in tags_list_res:
                            tags_objects = TagsDataModel(tags=tags)
                            tags_objects.interface_data = interfacee_data_list
                            tags_list.append(tags_objects)
                    else:
                        tags_objects = TagsDataModel(tags="未分类")
                        tags_objects.interface_data = interfacee_data_list
                        tags_list.append(tags_objects)
                interface_object = InterfaceLibrary(project_id=project_id)
                interface_object.interface = tags_list
                interface_object.save()
        except Exception as e:
            raise Exception("解析文档数据错误: {0}".format(e))

    def get_json_contents_holder(self):
        judge_status = self._judge_path_or_url()
        if judge_status:
            json_contents = self._open_file()
        else:
            json_contents = self._open_url()
        return json_contents

    def parser_interface(self,project_id,json_contents):
        json_contents = json.loads(json_contents,strict=False)
        self._parser_interface(project_id,json_contents)


if __name__ == '__main__':
    url = "/Users/shili/Downloads/swaggerApi.json"
    s = SwaggerParser(url)
    # res = s.main_func(url)


