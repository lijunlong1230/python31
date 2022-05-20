"""测试登录功能（函数）"""
import unittest
import ddt

from class17_excel封装.excel_handler import ExcelHandler


def login(username=None, password=None):
    """登录"""
    if (not username) or (not password):
        # 用户名或者密码为空
        return {"msg": "empty"}

    if username == 'lili' and password == '123':
        # 正确的用户名和密码
        return {"msg": "login success"}

    return {"msg": "error"}


# def login(username=None, password=None):
#     """登录"""
#     if username != None and password != None:
#         if username == 'yuz' and password == '123456':
#             return {"msg": "login success"}
#         else:
#             return {"msg": "username or password error"}
#     else:
#         return {"msg": "username or password is empty"}

# cases = [
# {"username":"lili","password":"123","expected":{"msg": "login sccess"}},
# {"username":"lili1","password":"123","expected":{"msg": "error"}},
# {"username":"","password":"123","expected":{"msg": "empty"}}
# ]
cases = ExcelHandler("cases.xlsx").read_data('Sheet1')

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("一个测试类只执行一次的前置")

    @classmethod
    def tearDownClass(cls):
        print("一个测试类只执行一次的后置")

    # 固定的名称，不改
    def setUp(self):
        """前置"""
        print("连接数据库")

    def tearDown(self):
        """后置"""
        print("断开数据库")

    # 测试用例的方法
    # 这里的*并不是不定长参数，在函数定义时候*是不定长参数，在函数调用时候*就是解包，元祖列表用一个*，字典用两个*
    @ddt.data(*cases)#@装饰器
    def test_login(self,case_info):
        """登录成功用例"""
        print(case_info)
        data = eval(case_info['data'])#去掉两边的'引号"双引号后取结果值
        username = data["username"]
        password = data["password"]
        expected_response = case_info["expected"]
        # 调用被测试的单元，
        actual_response = login(username, password)
        self.assertTrue(expected_response == actual_response["msg"])

if __name__ == '__main__':
    # 使用 python 运行这个模块里面的测试用例
    unittest.main()



