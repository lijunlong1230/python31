import json
import random

import ddt
import unittest
from class_test.midderware.handler import Handler

test_info = Handler.excel.read_data("register_V0")
logger = Handler.logger

@ddt.ddt
class TestRegister(unittest.TestCase):

	@ddt.data(*test_info)
	def  test_register(self,test_info):

		if "#phone#" in test_info:
			phone = self.random_phone
			test_info["data"] = test_info["data"].replace("#phone#",phone)

		data = json.loads(test_info["data"])
		resq = request_handler.visit(
			url=test_info["url"],
			method=test_info["method"],
			json=data,
			headers=json.loads(test_info["headeers"])
		)
		expected_dict = json.loads(test_info["expected"])
		try:
			for k,v in expected_dict.items():
				self.assertEqual(v,resq[k])

			if resq["code"] == 0:
				sql_code = "select * from futurreloan.member where mobile_phone={};".format(data["mobile_phone"])
				user = self.db.query(sql_code)
				#assert在调试期间用来检查我的猜测或者决不允许出现的情况有没有发生吧，一旦发生就表明我的程序很可能有BUG
				#而if就是我理所应当处理的各种情况，且这些情况如果发生并不代表程序发生BUG，所以这里不用if用assert
				self.assertTrue(user)

			logger.info("测试通过")
		except AssertionError as e:
			logger.error("无法通过{}".format(e))
			raise e



	def random_phone(self):
		while True:
			phone = "13"
			for i in range(9):
				num = random.randint(0,9)
				phone += str(num)
			print(phone)

			db = Handler.mysqlhandler()
			sql_code = "SELECT * FROM futureloan.member WHERE mobile_phone={};".format(phone)
			phone_record = db.query(sql_code)
			if not phone_record:
				db.close()
				return phone
			db.close()