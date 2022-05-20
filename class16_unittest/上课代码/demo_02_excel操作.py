
"""excel.

第二个库： openpyxl,  专门处理excel 表格的。 只支持 xlsx 格式（2003以后）， xls
xlrd, xlwt :


安装： pip install openpyxl
"""

# 导入 openpyxl
from pprint import pprint

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

# 第一步：打开文件


workbook = openpyxl.load_workbook('cases.xlsx')
print(workbook)

# workbook.worksheets

# 第二步：获取表单
sheet: Worksheet = workbook['Sheet1']
print(sheet)

# 获取某一行，某一列的单元格
# cell() 方法得到的是一个单元格对象，不是 case_id 值
cell = sheet.cell(row=2, column=3)
print(cell)
# 获取单元格的数据
print(cell.value)


# 获取所有的行
# 今天的作业：：： 标题不要
[ [1, '登录', '登录失败', '{"username:...}'], [] , []        ]
[ {"case_id": 1, "module": "登录"}, {}, {} , {}]

rows = list(sheet.rows)
pprint(rows)
for row in rows:
    # row: 一行数据 （）
    for cell in row:
        print(cell.value)


