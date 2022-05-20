import json
import os

import requests
from jsonpath import jsonpath
from pymysql.cursors import DictCursor

from class_test.common import yaml_handler, excel_handler, logger_handler, requests_handler
from class_test.config import config
from common.mysql_handler import Mysqlhandler

class MysqlHandlermid(Mysqlhandler):
	def __init__(self):
		db = Handler.yaml("db")
		super().__init__(

			host=db["host"],
			port=db["port"],
			user=db["user"],
			password=db["password"],
			charset=db["charset"],
			cursorclass=DictCursor
		)



class Handler():
	conn = config
	yaml = yaml_handler.read_yaml(os.path.join(conn.CONFIG_PATH,"config.yml"))
	__excel_path = conn.DATA_PATH
	__excel_file = yaml["excel"]["file"]
	excel = excel_handler.excel_hander(os.path.join(__excel_path,__excel_file))
	__logger_config = yaml["logger"]
	logger = logger_handler.get_logger(
		name=__logger_config["name"],
		file=os.path.join(conn.LOG_PATH,__logger_config["file"]),
		logger_level=__logger_config["logger_level"],
		stream_level=__logger_config["stream_level"],
		file_level=__logger_config["file_level"]
	)
	db_class = MysqlHandlermid

	@property
	def token_type(self):
		return login()["token"]
		#这句应该是拿到user用户中的token值，yaml["user"]是拿到了这个用户的返回值
		#return self.login(self.yaml["user"]["token"])


	@property
	def member_id(self):
		return login()["member_id"]
		#return self.login(self.yaml["user"]["member_id"])

def login():
    """登录测试账号"""
    res = requests_handler.visit(
        url = Handler.yaml["host"] + "/member/login",
        method= "post",
        headers= {"X-Lemonban-Media-Type": "lemonban.v2"},
        json= Handler.yaml["user"]
    )

    token_str = jsonpath(res, "$..token")[0]
    token_type = jsonpath(res, "$..token_type")[0]
    member_id = jsonpath(res, "$..id")[0]


    token = " ".join([token_type, token_str])
    # 提取 member_id
    return {"token": token, "member_id": member_id}

if __name__ == '__main__':
	print(login())
	print(Handler.yaml)



