import json
import unittest
import ddt
from common import requests_handler
from middleware.handler import Handler

# 初始化
logger = Handler.logger
test_data = Handler.excel.read_data("add")
env_data = Handler()


@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = env_data.token
        cls.member_id = env_data.member_id
        cls.loan_id = env_data.loan_id
        env_data.audit_loan()
        env_data.recharge()

    def setUp(self) -> None:
        self.db = env_data.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_invest(self, test_info):
        data = test_info["data"]

        data = env_data.replace_data(data)

        data = eval(data)
        headers = test_info["headers"]
        headers = env_data.replace_data(headers)
        headers = json.loads(headers)

        # 查询之前的余额

        resp = requests_handler.visit(
            url=env_data.yaml["host"] + test_info["url"],
            method=test_info["method"],
            headers=headers,
            json=data
        )

        expected = json.loads(test_info["expected"])
        self.assertEqual(expected["code"], resp["code"])
        self.assertEqual(expected["msg"], resp["msg"])

        # if resp["code"] == 0:
        #     after_loan = self.db.query(
        #         "SELECT * FROM futureloan.loan WHERE member_id={}".format(self.member_id),
        #         one=False
        #     )
        #     self.assertEqual(len(before_loan) + 1, len(after_loan))




