'''安装pip install openpyxl'''

import openpyxl
from pprint import pprint
from openpyxl.worksheet.worksheet import Worksheet

#第一步打开文件
workbook = openpyxl.load_workbook('cases.xlsx')
#第二部获取表单
sheet: Worksheet = workbook['Sheet1']
#获取某一行或者某一列的参数
cell = sheet.cell(row=2,column=3)
#获取所有的行
rows = list(sheet.rows)
#把rows中的值以列表的形式存放在列表中
data = []
for row in  rows[1:]:
	row_data = []
	for cell in row:
		print(cell.value)
		row_data.append(cell.value)
	data.append(row_data)

#把rows中的值 列表套字典的形式存放在列表中
lb = []
new = []
for head in rows[0]:
	lb.append(head.value)
print(lb)

zd = {}
for qt in rows[1:]:
	for k,v in enumerate(qt):
		zd[lb[k]] = v.value
	new.append(zd)
pprint(new)