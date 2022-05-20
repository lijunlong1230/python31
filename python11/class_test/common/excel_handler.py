import openpyxl


class Excel_Hander():

	def __init__(self,file_path):
		self.file_path = file_path

	def open_file(self):
		workbook = openpyxl.load_workbook(self.file_path)
		self.workbook = workbook
		return workbook

	def get_sheet(self,name):
		sheet = self.open_file()
		return sheet[name]

	def read_data(self,name):
		sheet = self.get_sheet(name)
		rows = list(sheet.rows)
		headers = []
		data = []
		for title in rows[0]:
			headers.append(title.value)

		for row in rows[1:]:
			row_data = {}
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



