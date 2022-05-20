#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import os
from jsonpath import jsonpath
from pymysql.cursors import DictCursor

from common import yaml_handler, excel_handler, logging_handler, requests_handler
from common.mysql_handler import MysqlHandler
from config import config


class MysqlHandlerMid(MysqlHandler):
    """读取配置文件的选项， MysqlHandler"""
    def __init__(self):
        """初始化所有的配置项，从yaml当中读取
        db:
          host: "120.78.128.25"
          port: 3306
          user: "future"
          password: "123456"
          charset: 'utf8'
        """
        db_config = Handler.yaml["db"]

        super().__init__(
                host=db_config["host"],
                port=db_config["port"],
                user=db_config["user"],
                password=db_config["password"],
                charset=db_config["charset"],
                cursorclass=DictCursor
        )




class Handler:
    """初始化所有的数据。
    在其他的模块当中重复使用。
    是从 common 当中实例化对象。
    """
    # 加载 python 配置项
    conf = config

    # YAML 数据
    yaml = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH, "config.yml"))

    # excel 数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml["excel"]["file"]
    excel = excel_handler.ExcelHandler(os.path.join(__excel_path, __excel_file))

    # logger
    __logger_config = yaml["logger"]
    logger = logging_handler.get_logger(
        name=__logger_config["name"],
        file=os.path.join(config.LOG_PATH, __logger_config["file"]),
        logger_level=__logger_config["logger_level"],
        stream_level=__logger_config["stream_level"],
        file_level=__logger_config["file_level"]
    )
    # mysql 应不应该放到Handler, 不行。 db 对象。
    # 不存储对象，我存储类. TODO: 没有听明白的可以不用这一行，使用的时候直接导入
    # MysqlHandlerMid
    db_class = MysqlHandlerMid

    @property
    def token(self):
        return self.login(self.yaml["user"])["token"]

    @property
    def member_id(self):
        return self.login(self.yaml["user"])["member_id"]

    @property
    def admin_token(self):
        return self.login(self.yaml["admin_user"])["token"]

    @property
    def loan_id(self):
        return self.add_loan()

    def login(self, user):
        """登录测试账号"""
        res = requests_handler.visit(
            url=Handler.yaml["host"] + "/member/login",
            method="post",
            headers={"X-Lemonban-Media-Type": "lemonban.v2"},
            # json=Handler.yaml["user"]
            json=user
        )

        # 提取 token
        # jsonpath
        token_str = jsonpath(res, "$..token")[0]
        token_type = jsonpath(res, "$..token_type")[0]
        member_id = jsonpath(res, "$..id")[0]
        token = " ".join([token_type, token_str])
        # 提取 member_id
        return {"token": token, "member_id": member_id}

    # def login_admin(self):
    #     """登录admin测试账号"""
    #     res = requests_handler.visit(
    #         url=Handler.yaml["host"] + "/member/login",
    #         method="post",
    #         headers={"X-Lemonban-Media-Type": "lemonban.v2"},
    #         json=Handler.yaml["admin_user"]
    #     )
    #
    #     # 提取 token
    #     # jsonpath
    #     token_str = jsonpath(res, "$..token")[0]
    #     token_type = jsonpath(res, "$..token_type")[0]
    #     token = " ".join([token_type, token_str])
    #     # 提取 member_id
    #     return token

    def add_loan(self):
        data = {"member_id": self.member_id,
                "title": "木森借钱买飞机",
                "amount": 2000,
                "loan_rate": 12.0,
                "loan_term": 3,
                "loan_date_type": 1,
                "bidding_days": 5}
        # 发送请求，添加项目
        res = requests_handler.visit(
            url=Handler.yaml["host"] + "/loan/add",
            method="post",
            headers={"X-Lemonban-Media-Type": "lemonban.v2",  "Authorization": self.token},
            json=data
        )

        # 提取项目的id给审核的用例使用
        return jsonpath(res, "$..id")[0]


    def audit_loan(self):

        data = {"loan_id":self.loan_id,"approved_or_not": True}

        resp = requests_handler.visit(
            url=Handler.yaml["host"] + "/loan/audit",
            method="post",
            headers={"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": self.admin_token},
            json=data
        )
        # return self.loan_id

    def recharge(self):

        data = {"member_id": self.member_id,"amount":500000}

        resp = requests_handler.visit(
            url=Handler.yaml["host"] + "/member/recharge",
            method="post",
            headers={"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": self.token},
            json=data
        )

    def replace_data(self, data):
        import re
        patten = r"#(.*?)#"
        while re.search(patten, data):
            key = re.search(patten, data).group(1)
            value = getattr(self, key, "")
            data = re.sub(patten, str(value) , data, 1)
        return data


if __name__ == '__main__':
    h = Handler()
    m_str = '{"member_id": #member_id#,"token":"#token#", "loan_id": #loan_id#, "admin_token": #admin_token#, "random_prop":"#random#"}'
    a = h.replace_data(m_str)
    print(a)



    # data_path = Handler.conf.DATA_PATH
    # print(Handler.yaml["excel"]["file"])
    #
    # # print(Handler.__excel_path)
    # # print(Handler.__excel_path)
    # print(Handler.logger)

    # 模块本来就是对象。
    # config.DATA_PATH
    # # 变量赋值
    # conf = config
    # db = MysqlHandlerMid()
    # data = db.query("SELECT * FROM futureloan.member LIMIT 10;")
    # print(data)

    # print(Handler.db_class)
    # print(Handler.db_class().query("SELECT * FROM futureloan.member LIMIT 10;"))

    # 测试login 函数
    # print(login())

    # print(Handler().admin_token())

    # h = Handler()
    # data = '{"loan_id": "#loan_id#", "member_id": "#member_id#"}'
    # new = h.replace_data(data)
    # print(new)
