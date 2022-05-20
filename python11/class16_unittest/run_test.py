import os
import unittest
from class16_unittest.tests import test_login,test_register
from libs.HTMLTestRunnerNew import HTMLTestRunner#也可以用beautifulreport

#获取测试用例的目录路径
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path,'tests')

loader = unittest.TestLoader()
#使用loader收集所有的测试数据
test_suit = loader.discover(case_path)

#执行测试用例
runner = unittest.TextTestRunner()
runner.run(test_suit)

#只加载登录和注册的case
t_login = loader.loadTestsFromModule(test_login)
t_reg = loader.loadTestsFromModule(test_register)

#初始化suite
suit_total = unittest.TestSuite()
suit_total.addTests([t_login,t_reg])

#生成报告
with open('test_reports.html','wb') as f:
	runner = HTMLTestRunner(
		f,#f就是as f:代表写入到这个文件中
		title = '我的报告',
		description = '测试报告的描述',
		tester = 'lili'
	)
	runner.run(suit_total)

