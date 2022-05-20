from pprint import pprint
import ddt
import openpyxl
'''option+enter快速导入模块'''

class ExcelHandler:

	def __init__(self,file_path):
		'''初始化K'''
		self.file_path = file_path
		self.workbook = None

	def open_file(self):
		'''打开文件K'''
		print('打开文件{}'.format(self.file_path))
		workbook = openpyxl.load_workbook(self.file_path)
		self.workbook = workbook
		return workbook

	def get_sheet(self,name):
		'''获取表格K'''
		workbook = self.open_file()
		print('获取表格{}'.format(name))
		return workbook[name]

	def read_data(self,name):
		'''读取数据 存放到列表或者字典当中'''
		sheet = self.get_sheet(name)
		rows = list(sheet.rows)
		data = []
		headers = []
		for title in rows[0]:
			headers.append(title.value)
		for row in rows[1:]:
			row_data = {}
			for k,v in enumerate(row):
				row_data[headers[k]] = v.value
			print('******'+str(row_data))
			data.append(row_data)
		print('读取数据中......')
		return data

	def write(self,sheet_name,row,column,data):
		'''写入单元格数据'''
		sheet = self.get_sheet(sheet_name)
		sheet.cell(row,column).value = data
		self.save()
		self.close()

	def save(self):
		'''保存'''
		self.workbook.save(self.file_path)

	def close(self):
		print('关闭文件：{}'.format(self.file_path))
		self.workbook.close()

if __name__ == '__main__':
	excel = ExcelHandler('cases.xlsx')
	print(excel.get_sheet('Sheet1'))
	pprint(excel.read_data('Sheet1'))
	# print(excel.write('cases.xlsx','4','4','666'))
















