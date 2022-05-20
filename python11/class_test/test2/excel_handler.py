import openpyxl


class ExcelHandler():

	def __init__(self,file_path):
		self.file_path = file_path

	def open_file(self):
		workbook = openpyxl.workbook(self.file_path)
		self.workbook = workbook
		return workbook

	def get_sheet(self,name):
		workbook = self.open_file()
		return workbook[name]

	def read_data(self,name):
		row = self.get_sheet(name)
		rows = list(row.rows)
		headers = []
		data = []
		for title in rows(0):
			headers.append(title.value)

		for row in rows[1:]:
			row_data={}
			for k,v in enumerate(row):
				row_data[headers[k]] = v.value
			data.append(row_data)
		self.close()
		return data

	def write(self,sheet_name,row,column,data):
		sheet = self.get_sheet(sheet_name)
		sheet.cell(row,column).value = data
		self.save()
		self.close()

	def save(self):
		self.workbook.save(self.file_path)


	def close(self):
		self.workbook.close()




