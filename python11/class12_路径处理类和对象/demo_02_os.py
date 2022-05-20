import os.path
#os.path主要处理系统路径相关的操作 ******下面获取三种路径方式必须掌握


#第一种 abspath 获取现在的文件绝对路径
file_path= os.path.abspath((__file__))
print('filepath：',file_path)

#第二种 dirname 获取上一级路径
dir_name = os.path.dirname(file_path)

#第三种 join 路径拼接 文件/文件
#所有获取到的路径，只是一个路径的表示，并不代表这个文件家或者丼真的存在
#说白了 ：路径得到的是一个福吹安，这个字符串是一个路径格式'\'
txt_path = os.path.join(dir_name,'demo.txt')#后面可以拼接多个文件都是在同一级目录下

with open(txt_path,'w') as f:
	f.write('new file')
with open(txt_path,'r') as f:
	print(f.read())

#以下是扩展 可以不掌握
#获取当前的工作目录
print('当前的工作目录是：'+os.getcwd())

#在当前目录下创建一个新的工作目录（文件夹）
if not os.path.exists(('subdir')):#判断subdir是否存在，不存在在创建一个文件
	print(os.mkdir('subdir'))

#判断一个路径是否存在
#print(os.path.exists(("d:/lol")))

#判断路径是否是一个文件
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

#判断路径是否是一个目录

print(os.mkdir('总结'))#创建的文件夹
with open('总结.py','w') as f:
	pass