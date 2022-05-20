"""运行所有的用例"""
import os
import unittest
from config import config
from datetime import datetime
from libs.HTMLTestRunnerNew import HTMLTestRunner

# 加载用例
loader = unittest.TestLoader()
suites = loader.discover(config.CASE_PATH)

# 测试报告的路径
ts = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
reports_filename = "reports-{}.html".format(ts)
reports_path = os.path.join(config.REPORTS_PATH, reports_filename)

# 运行用例
with open(reports_path, mode='ab+') as f:
	runner = HTMLTestRunner(
		f,
		title="lili的测试报告",
		description="自动化测试报告",
		tester="lili"
	)
	runner.run(suites)
