import logging


def get_logger(
	name='root',
	file=None,
	logger_level='DEBUG',
	stream_level='DEBUG',
	file_level='INFO',
	fmt='%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s',
):
	logger = logging.getLogger(name)
	logger.setLevel(logger_level)
	stream_handler = logging.StreamHandler()
	stream_handler.setLevel(stream_level)
	logger.addHandler(stream_handler)

	fmt = logging.Formatter(fmt)
	stream_handler.setFormatter(fmt)

	if file:
		file_handler = logging.FileHandler(file,encoding='utf-8')
		file_handler.setLevel(file_level)
		logger.addHandler(file_handler)
		file_handler.setFormatter(fmt)

	return logger


