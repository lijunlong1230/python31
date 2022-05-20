import os

from jsonpath import jsonpath
from pymysql.cursors import DictCursor

from class_test.common import yaml_handler, excel_handler, logger_handler, mysql_handler, requests_handler
from class_test.config import config

class MysqlHandlerMid(mysql_handler):
	def init(self):
		db = Handler.yaml["db"]
		super().__init(
			host=db["host"],
			port=db["port"],
			user=db["user"],
			passwor=db["password"],
			charset=db["charset"],
			cursorclass=DictCursor
		)



class Handler():
	conn = config
	yaml = yaml_handler.read_yaml(os.path.join(conn.CONFIG_PATH,"config.yml"))
	__excel = conn.DATA_PATH
	__excel_file = yaml["excel"]["file"]
	excel = excel_handler.Excel_Hander(
		os.path.join(__excel,__excel_file)
	)
	logger = yaml["logger"]
	__logger_config = logger_handler.get_logger(
		name=logger["name"],
		file=logger["file"],
		logger_level=logger["logger_level"],
		stream_level=logger["stream_level"],
		file_level=logger["file_level"]
	)

	db_class = MysqlHandlerMid

	@property
	def token(self):
		return login()["token"]

	@property
	def member_id(self):
		return login()["member_id"]

def login(self):
	req = requests_handler.visit(
		url=Handler.yaml["host"],
		method='post',
		json=Handler.yaml["user"],
		headers={"X-Lemonban-Media-Type": "lemonban.v2"},
	)

	token_str = jsonpath(req, "$..token")[0]
	token_type = jsonpath(req, "$..token_type")[0]
	member_id = jsonpath(req, "$..id")[0]

	token = "".join([token_str,token_type])
	return {"token":token,"member_id":member_id}

