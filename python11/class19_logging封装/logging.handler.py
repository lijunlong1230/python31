import logging
from class19_logging封装 import yaml_handler


conf = yaml_handler.read_yaml("config.yaml")
log_conf = conf['log']

def get_logger(
			name=log_conf['name'],
			logger_level=log_conf['logger_level'],
			stream_level=log_conf['stream_level'],
			file_level = log_conf['file_level'],
			file = log_conf['file'],
			fmt='%(asctime)s--%(filename)s--line:%(lineno)d--%(levelname)s:%(message)s'
		):
		# 获取日志收集器K
		logger = logging.getLogger(name)
		logger.setLevel(logger_level)
		# 获取控制台输出器
		stream_handler = logging.StreamHandler()
		stream_handler.setLevel(stream_level)
		logger.addHandler(stream_handler)

		if file:
			file_handler = logging.FileHandler(file,encoding='utf-8')
			file_handler.setLevel(file_level)
			logger.addHandler(file_handler)
		#设置输出格式
		fomt = logging.Formatter(fmt)
		stream_handler.setFormatter(fomt)
		file_handler.setFormatter(fomt)

		return logger

if __name__ == '__main__':
	logger = get_logger()
	logger.error('woshi :error')