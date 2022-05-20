class ExcelHandler:

	def __init__(self, file_path):
		'''初始化K'''
		self.file_path = file_path

	def open_file(self):
		'''打开文件K'''
		print('打开文件{}'.format(self.file_path))

	def get_sheet(self, name):
		'''获取表格K'''
		self.open_file()
		print('获取表格{}'.format(name))

	def read_data(self, name):
		'''读取数据K'''
		self.get_sheet(name)
		print('读取数据')

	def clase(self):
		print('关闭文件：{}'.format(self.file_path))
