import logging

def get_logger(
		name = "root",
		file = None,
		logger_level = "DEBUG",
		stream_level="DEBUG",
		file_level ="INFO",
		fmt = '%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s'
):
	#获取日志收集器
	logger = logging.getLogger(name)
	#设置级别
	logger.setLevel(logger_level)
	#获取输出管理器
	stream_handler = logging.StreamHandler()
	#设置级别
	stream_handler.setLevel(stream_level)
	logger.addHandler(stream_handler)
	#格式
	fmt = logging.Formatter(fmt)
	stream_handler.setFormatter(fmt)

	# 判断file是否为空，输入文件就付给level并且给fmt没有则不执行这段。
	if file :
		file_handler = logging.FileHandler(file,encoding='utf8')
		file_handler.setLevel(file_level)
		logger.addHandler(file_handler)
		file_handler.setFormatter(fmt)

	return logger
if __name__ == '__main__':
	logger = get_logger('log.txt')
	logger.info("hello")


