#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import os
import unittest
import ddt
import json


from common.excel_handler import ExcelHandler
from common import requests_handler, yaml_handler, logging_handler
from config import config

# 读取配置文件的 Excel 文件名。
yaml_data = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH, "config.yml"))
case_file = yaml_data["excel"]["file"]


# 初始化 loggger
logger_config = yaml_data["logger"]
logger = logging_handler.get_logger(
    name=logger_config["name"],
    file= os.path.join(config.LOG_PATH, logger_config["file"]),
    logger_level=logger_config["logger_level"],
    stream_level=logger_config["stream_level"],
    file_level=logger_config["file_level"]
)

# 获取Excel
excel_file = os.path.join(config.DATA_PATH, case_file)
xls = ExcelHandler(excel_file)
test_data = xls.read_data("register_v0")
logger.info("正在读取excel测试用例")


@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*test_data)
    def test_register(self, test_info):
        # 访问接口
        resp = requests_handler.visit(
            url=test_info["url"],
            method=test_info["method"],
            json=json.loads(test_info["data"]),
            headers=json.loads(test_info["headers"])
        )
        expected_dict = json.loads(test_info["expected"])

        try:
            for key, value in expected_dict.items():
                self.assertTrue(value, resp[key])


            if resp["code"] == 0:
                # 如果是注册成功，数据库当中需要有这个手机号码的记录
                # "SELECT * FROM futureloan.member WHERE mobile_phone = {}".format();
                # data =
                pass


            logger.info("测试用例通过")
        except AssertionError as e:
            logger.error("测试用例无法通过:{}".format(e))
            raise e
