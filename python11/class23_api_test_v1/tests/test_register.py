import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

logger = Handler.logger
test_data = Handler.excel.read_data("register_v0")

@ddt.ddt
class TestRegister(unittest.TestCase):

	@ddt.data(*test_data)
	def test_register(self, test_info):
		# 判断测试用来数据有没有#phone# 如果有 就要替换成动态生成的手机号码
		if "#phone#" in test_info["data"]:
			phone = self.random_phone()
			test_info["data"] = test_info["data"].replace("#phone#", phone)

		# 访问接口,loads是字符串转换字典，dumps是字典转换为字符串。
		data = json.loads(test_info["data"])
		resp = requests_handler.visit(
			url=test_info["url"],
			method=test_info["method"],
			json=data,
			headers=json.loads(test_info["headers"])
		)
		expected_dict = json.loads(test_info["expected"])

		try:
			for key, value in expected_dict.items():
				self.assertEqual(value, resp[key])

			if resp["code"] == 0:

				db = Handler.db_class()
				sql_code = "select * from future.memb where mobile_phone={};".format(data["mobile_phone"])
				user = db.query(sql_code)
				self.assertTrue(user)
				# if not user:
				# 	db.close()
				# 	return phone
				# db.close()
				# pass

			logger.info("测试用例通过")
		except AssertionError as e:
			logger.error("测试用例无法通过:{}".format(e))
			raise e

	def random_phone(self):
		"""随机生成一个动态的手机号码。
		注册成功的用例当中，需要一个没有被注册过的手机号。需要查询数据库。
		"""
		# 第一步，随机生成手机号
		# 前面 2 位  13
		import random
		while True:
			phone = "13"
			for i in range(9):
				num = random.randint(0, 9)
				phone += str(num)
			print(phone)


			db = Handler.db_class()
			sql_code = "select * from future.memb where mobile_phone={};".format(phone)
			phone_record = db.query(sql_code)
			if not phone_record:
				db.close()
				return phone
			db.close()
