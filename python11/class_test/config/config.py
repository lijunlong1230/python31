# 配置文件路径
import os

CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))

# 项目路径
ROOT_PATH = os.path.dirname(CONFIG_PATH)

# 测试用例路径
CASE_PATH = os.path.join(ROOT_PATH, 'tests')

# 测试报告路径
REPORTS_PATH = os.path.join(ROOT_PATH, "reports")

# 测试数据路径
DATA_PATH = os.path.join(ROOT_PATH, "data")

# LOG 数据路径
LOG_PATH = os.path.join(ROOT_PATH, "logs")

HOST = "http://api.lemonban.com/futureloan"
