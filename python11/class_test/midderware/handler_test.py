import os

from pymysql.cursors import DictCursor

from class_test.common.mysql_handler import Mysql_Handler
from class_test.config import config
from class_test.common import yaml_handler, excel_handler, logger_handler


class MysqlHandlerMid(Mysql_Handler):
	def __init__(self):
		db = Handler.yaml["db"]
		super().__init__(
			host=db["host"],
			port=db["port"],
			user=db["user"],
			password=db["password"],
			charset=db["charset"],
			cursourclass=DictCursor
		)



class Handler():

	conf = config
	yaml = yaml_handler.read_yaml(os.path.join(conf.CONFIG_PATH,'config.yml'))

	__excel_path = conf.DATA_PATH
	__excel_file = yaml["excel"]["file"]
	excel = excel_handler.excel_hander(os.path.join())
	__logger_config = yaml["logger"]
	logger = logger_handler.get_logger(
		name=__logger_config["name"],
		file=__logger_config["file"],
		logger_level=__logger_config["logger_level"],
		stream_level=__logger_config["stream_level"],
		file_level=__logger_config["file_level"]
	)

	db_class = MysqlHandlerMid
