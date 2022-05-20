import logging

#得到root收集器
root_logger = logging.getLogger('python30')
root_logger.setLevel('DEBUG')

# #handler输出处理器，
# stream_handler = logging.FileHandler()
# stream_handler.setLevel('DEBUG')

file_handler = logging.FileHandler('log.txt',encoding = 'utf-8')
file_handler.setLevel('INFO')
fmt = logging.Formatter('%(asctime)s--%(filename)s--line:%(lineno)d--%(levelname)s:%(message)s')
file_handler.setFormatter(fmt)

root_logger.addHandler(file_handler)


root_logger.debug("debuglog")
root_logger.error("error")
root_logger.warning("warning")
root_logger.critical("critical")




