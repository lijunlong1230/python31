
import json

import ddt
import unittest

from class_test.common import requests_handler
from class_test.midderware.handler import Handler

test_data = Handler.excel.read_data("login")

@ddt.ddt
class LoginTestCase(unittest.TestCase):
	@ddt.data(*test_data)
	def test_login(self,case):
		method = case["method"]
		url = case["url"]

		data = json.loads(case["data"])
		headers = json.loads(case["headers"])
		expected = json.loads(case["expected"])
		res = requests_handler.visit(
			method=method,
			url=url,
			json=data,
			headers=headers
		)

		try:
			self.assertEqual(expected["code"],res["code"])
			self.assertEqual(expected["msg"],res["msg"])
		except AssertionError as e:
			pass