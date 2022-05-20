import json

import ddt
import unittest

from class_test.common import requests_handler
from class_test.midderware.handler import Handler

test_register = Handler.excel.read_data("register_V0")
logger = Handler.logger
@ddt.ddt
class TESTREGISTER(unittest.TestCase):
	@ddt.data(*test_register)
	def test_register(self,info):

		if "#phone#" in info["data"]:
			phone = self.random_phone
			info["data"] = info["data"].replace("#phone#",phone)
			method = info["method"]
			url = info["url"]
			data = json.loads(info["data"])
			headers = json.loads(info["headers"])
			expected = json.loads(info["expected"])
			req = requests_handler.visit(
				url=url,
				method=method,
				json=data,
				headers=headers
			)
			try:
				for k,v in expected.items():
					self.assertEqual(v,req[k])
				if req["code"] == 0:
					db = Handler.mysqlhandler
					sql_code = "select * from futureloan.member where mobile_phone{};".format(data["mobile_phone"])
					user = db.query(sql_code)
					self.assertTrue(user)
				logger.info("tonguo")
			except AssertionError as e:
				logger.info("weitongguo")
				raise e



	def random_phone(self):
		import random
		while True:
			phone = "13"
			for i in range(9):
				num = random.randint(0,9)
				phone += str(num)

			db = Handler.mysqlhandler
			sql_code = "select * from futureloan.member where mobile_phone{};".format(phone)
			user = db.query(sql_code)
			if user:
				db.close()
				return phone
			db.close()


