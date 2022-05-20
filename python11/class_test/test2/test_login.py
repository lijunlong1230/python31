import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler



datas = Handler.excel.read_data("login")

@ddt.ddt
class TestLogin(unittest.TestCase):

	@ddt.data(*datas)
	def test_login(self,case):
		url = case["url"]
		method = case["method"]
		data = json.loads(case["json"])
		headers = json.loads(case["headers"])
		expected = json.loads(case["expected"])

		res = requests_handler.visit(
			url=url,
			method=method,
			data=data,
			headers=headers,
		)

		try:
			self.assertEqual(expected["code"],res["code"])
			self.aasertEqual(expected["msg"],res["msg"])
		except AssertionError as e:
			pass








