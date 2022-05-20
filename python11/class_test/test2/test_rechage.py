import json
from ddt import ddt
import unittest
from class_test.midderware.handler import Handler

env_data = Handler()
test_data = env_data.excel

@ddt.ddt
class TestRechage(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.token = env_data.token
		cls.member_id = env_data.member_id

	def setUp(self) -> None:
		self.db = env_data.db_class()

	def tearDown(self) -> None:
		self.db.close()

	@ddt.data(*test_data)
	def test_rechage(self,test_info):

		data = test_info["data"]
		if "#memeber_id#" in data:
			data = data.replace("#member_id#", str(self.member_id))
		headers = test_info["headers"]
		if "#token#" in headers:
			headers = headers.replace("#token#",self.token)

		data = json.loads(data)
		headers = json.loads(headers)







