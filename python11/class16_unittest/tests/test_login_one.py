import unittest

def login(username=None, password=None):
    """登录"""
    if (not username) or (not password):
        # 用户名或者密码为空
        return {"msg": "empty"}

    if username == 'lijia' and password == 'li123':
        # 正确的用户名和密码
        return {"msg":"login success"}

    return {"msg": "error"}


def login(username=None, password=None):
    """登录"""
    if username != None and password != None:
        if username == 'lijia' and password == 'li123':
            return {"msg":"login success"}
        else:
            return {"msg": "username or password error"}
    else:
        return {"msg": "username or password is empty"}



class TestLogin(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("测试类只执行一次的前置")

	@classmethod
	def tearDownClass(cls):
		print("测试类只执行一次的后置")

	def setup(self):
		'''qianzhi'''
		print("链接数据库")

	def tearDown(self):
		'''houzhi'''
		print("断开数据库")

	#测试用例的方法
	def test_login_01_success(self):
		'''登录成功用例'''
		username = 'lijia'
		password = 'li123'
		expected_response = {"msg":"login success"}
		actual_reponse = login(username,password)
		self.assertTrue(expected_response == actual_reponse)
	# def test_login_02_error(self):
	# 	'''失败的测试用例'''
	# 	username = ''
	# 	password = ''
	# 	expected_response = {"msg":"login success"}
	# 	actual_reponse = login(username,password)
	# 	self.assertTrue(expected_response == actual_reponse)

	def test_demo(self):
		pass
	def tst_demo_1(self):
		pass