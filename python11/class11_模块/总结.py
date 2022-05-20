#文件的写入操作
#方法1.
f = open ('filename.txt','w')
f.write('data')
f.close()

#方法2
with open('test.txt','w') as f:#(如果没有test文件则创建文件,有文件则写入:'with open(test.txt,w)')
	f.write('with open(test.txt,w)')
with open('test.txt','r') as f:#读取test文件
	fo = f.read()
	print(fo)


#编写如下程序 创建一个txt文件 第一行写入name, age gender hoobby 从第二行开始加入具体用户信息
#列入：yuze,18,男，读书，具体信息要求来自于一个嵌套字典的列表person_info
#将所有用户信息写入TXT文件中，并读取出来。
person_info=[{'name':'yuze','age':18,'gender':'男','hobby':'读书'},
			 {'name':'wanke','age':19,'gender':'女','hobby':'化学'}]

#把persion列表转化成字符串
# def convert_dict_to_str():
# 	'''把字典转换成字符串用，隔开'''


def get_value_lines(info):
	lines = ''
	for persion in info:
		#person={'name':'yuze','age':18,'gender':'男','hobby':'读书'}
		line=[]
		print(persion)
		for e in persion.values():
			line.append(str(e))
		print(line)
		#列表转化成字符串用join，字符串转换成列表用split
		line_str = ','.join(line)+"\n"#前面的'，'代表每次添加一个元素后用逗号隔开，下面有ab试列
		lines +=line_str
	return lines
# a = ['sk','22','kll','op']
# b = ''
# b = ','.join(a)
# print(b)

def main():
	'''添加标题的函数'''
	with open('info.txt','w+') as f:
		f.write('name,age,gender,hoobby\n')#因为还有第234行 所以加换行符
	data = get_value_lines(person_info)
	with open('info.txt','a',encoding='utf-8') as f:
		f.write(data)

#字典添加keyvalue 并且输出所有key
dict = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
dict['sex'] = '女'
for i in dict:
	dict
	print(i[0:])
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])