import os
from pprint import pprint
from jsonpath import jsonpath
from pymysql.cursors import DictCursor
from common.mysql_handler import Mysqlhandler
from common import yaml_handler, excel_handler, logging_handler, requests_handler
from config import config


class MysqlHandlerMid(Mysqlhandler):
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

def login():
	"""登录测试账号"""
	res = requests_handler.visit(
		url = Handler.yaml["host"] + "/member/login",
		method = "post",
		headers = {"X-Lemonban-Media-Type": "lemonban.v2 "},
		json = Handler.yaml["user"]

		)
	return res


if __name__ == '__main__':
	# data_path = Handler.conf.DATA_PATH
	# pprint(Handler.yaml["excel"]["file"])
	# pprint(Handler.excel)
	# pprint(Handler.logger.info("haha"))
	# print(Handler.db_class().query("SELECT * FROM future.memb LIMIT 10;"))
	pprint(login())
