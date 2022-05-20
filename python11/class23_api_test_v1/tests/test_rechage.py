import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

test_data = Handler.excel.read_data("recharge")

@ddt.ddt
class TestRecharge(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		#登录
		requests_handler.visit()

	@ddt.data(*test_data)
	def test_recharge(self,test_info):
		#


		pass

