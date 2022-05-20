"""运行程序。

收集所有的测试用例，
执行。
生成测试报告。
"""

import unittest
import os


# 初始化一个加载器， test_loader
from HTMLTestRunnerNew import HTMLTestRunner

from class16_unittest.tests import test_login, test_register

loader = unittest.TestLoader()

# 获取测试用例目录的路径
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'tests')

# 使用 loader 收集所有的测试用例
test_suit = loader.discover(case_path)
print(test_suit)

# 只加载注册的和登录的用例
suite_login = loader.loadTestsFromModule(test_login)
suite_register = loader.loadTestsFromModule(test_register)
# 初始化一个 suite
suit_total = unittest.TestSuite()
suit_total.addTests([suite_login, suite_register])




# # 执行测试用例
# runner = unittest.TextTestRunner()
# runner.run(test_suit)

# 生成测试报告
# with open("test_reports.txt", 'w', encoding='utf-8') as f:
#     runner = unittest.TextTestRunner(f)
#     runner.run(test_suit)

# HTML 测试报告 不是内置。是需要自己准备的。
with open("test_reports.html", 'wb') as f:
    runner = HTMLTestRunner(
        f,
        title='python29期第一次测试报告',
        description="测试报告的描述",
        tester='yuz'
    )
    runner.run(suit_total)











