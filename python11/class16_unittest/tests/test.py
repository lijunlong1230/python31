import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

workbook = openpyxl.load_workbook('cases.xlsx')
sheet:Worksheet = workbook['Sheet1']
rows = list(sheet.rows)


header = []
for row in rows[0]:
	header.append(row.value)
print(header)
sj = []
for sy in rows[1:]:
	zd = {}
	for k,v in enumerate(sy):
		zd[header[k]] = v.value
	sj.append(zd)
print(sj)