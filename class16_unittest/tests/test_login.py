"""测试登录功能（函数）"""
import unittest

def login(username=None, password=None):
    """登录"""
    if (not username) or (not password):
        # 用户名或者密码为空
        return {"msg": "empty"}

    if username == 'yuz' and password == '123456':
        # 正确的用户名和密码
        return {"msg": "success"}

    return {"msg": "error"}


def login(username=None, password=None):
    """登录"""
    if username != None and password != None:
        if username == 'yuz' and password == '123456':
            return {"msg": "login success"}
        else:
            return {"msg": "username or password error"}
    else:
        return {"msg": "username or password is empty"}




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
        print("链接数据库")

    def tearDown(self):
        """后置"""
        print("断开数据库")

    # 测试用例的方法
    def test_login_01_success(self):
        """登录成功用例"""
        username = 'yuz'
        password = '123456'
        expected_response = {"msg": "login success"}
        # 调用被测试的单元，
        actual_response = login(username, password)

        self.assertTrue( expected_response == actual_response )

        # if expected_response == actual_response:
        #     print("测试用例")
        # else:
        #     print("测试用例")

    def test_login_02_error(self):
        username = ''
        password = ''
        expected_response = {"msg": "username or password error"}
        actual_response = login(username, password)
        self.assertTrue(expected_response == actual_response)


if __name__ == '__main__':
    # 使用 python 运行这个模块里面的测试用例
    unittest.main()
