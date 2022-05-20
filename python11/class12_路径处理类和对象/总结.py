'''总结'''
class Man:
	name = '男人'
	def __init__(self,name):
		self.name = name

print(Man.name)
print(Man('lijia').name)
print(Man('a').name)

'''建立一个demo.py文件
获取该文件的绝对路径
在同一个目录下建立一个data文件夹
在data文件夹下建立一个cases.txt文件'''

import os
with open('demo.py','a') as f:
	pass
file_path = os.path.abspath(__file__)
d_path = os.path.dirname(file_path)
os.path.join(d_path,'demo.txt')

data_dir = os.path.join(d_path,'data')
if not os.path.exists(data_dir):
	os.mkdir(data_dir)
demo_txt_path = os.path.join(data_dir,'cases.txt')


'''封装学生类 自行定义雷属性和实例属性
属性：身份 姓名 年龄 性别 英语成绩 数学成绩 语文成绩 职责
如果是类属性请提前定义
如果是实例属性请初始化以后偶添加这个属性的值
'''




