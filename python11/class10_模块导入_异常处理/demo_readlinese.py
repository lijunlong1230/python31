#readlines()读取每一行，会存放到列表的当中每一行的内容就是列表的元素。
#每行末尾会多处\n 换行
#read得到的是一行字符串

f = open('demo.txt')
lines = f.readlines()
print(lines)
#分行打印
for line in lines:
	print(line.strip())#去掉末尾换行
for line,data in enumerate(lines):
	print(line)
	print(len(lines))
	if line == len(lines)-1:#这句就是判断他是不是末尾行 如果是直接打印出来 不是else去掉末尾\n
		print(data)
	else:
		print(data[:-1])

#with 语句可以节省关闭文件的操作

f = open('demo.txt')
f.read()
f.close()

#with 打开文件 用f接收 上下文表达式
print('------------------')
with open('demo.txt') as f:
	print(f.read())


