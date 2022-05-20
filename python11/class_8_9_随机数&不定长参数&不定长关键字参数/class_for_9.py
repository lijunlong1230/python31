import random

#for 循环语法:for item in 某个数据类型
range(1,9)
print(range)
#用例表形式输出显示
print(list(range(1,9)))
#遍历出l的素有值
l=[5,2,4,6,3]
for i in range(5):
	print(l[i])
#嵌套循环 请把列表中的所有值遍历出来
A=[['sl','kl','kls','lski'],['slk','sdfw','wrrd']]
for item in A:
	print(item)
	for item2 in item:
		print(item2)
print("---------------------------")
#嵌套输出
for i in range(5):
	for j in range(i):
		print('*', end='')
	print()
#简单输出
for i in range(10):
	print('*' * i)

#删除所有列表中的元素里面有坑
#坑1
black_list= ['卖鸡蛋','买面膜','买保险','买花生','买手机']
for name in black_list:
	black_list.remove(name)
print(black_list)
#坑2
for name in black_list:
	black_list[0]
print(black_list)
#坑3
for name in black_list:
	black_list.pop(0)
print(black_list)
#方法1 用长度删除
for i in range(len(black_list)):
	black_list.pop(i)
print(black_list)

#方法2复制列表 后删除
black_list_new = black_list[:]
for wx in black_list_new:
	black_list.remove(wx)
print(black_list)

#排序列表元素
a = [1,7,4,89,34,2]
print(len(a))
for index_one in range(len(a)-1):
	print(index_one)
	min_index = index_one
	print(a)
	for index_two in range(index_one+1,len(a)):
		if a[index_two] < a[min_index]:
			a[min_index],a[index_two] = a[index_two],a[min_index]#互换
			print(a[min_index],a[index_two],a[index_two],a[min_index])
			print("888"+str(a))
		print('min_index:',min_index)
		print("index_two:",index_two)
print("-------------------------------------")

#列表去重 定义一个函数去除重复元素
def remove_element(m_list):
	'''列表去重'''
	new_list=[]
	for i in m_list:
		if i not in new_list:
			new_list.append(i)
		else:
			new_list.remove(i)
	print(new_list)
	return new_list
hanshu=[1,4,2,2,5,3,4]
remove_element(hanshu)

#函数中包含：形参 实参 位置参数 关键字参数例如：middle（可以不按照顺序排列）get_name
#默认参数必须放到位置参数后面
#关键字参数必须要放到位置参数后面
def get_name(firstname,middle,lastname=""):
	'''拼接名字'''
	name=firstname+middle+lastname
	return name
name = get_name('李',lastname='漂亮',middle='佳')
print(name)

# *不定长位置参数
# def get_name(firstname,*names):
# 	'''获取名字'''
# 	print(firstname)
# 	print(*names)
# 	return firstname

#不定长关键字参数
def get_name3(*names,**kwargs):
	'''获取名字'''
	print(names)
	print("------")
	print(kwargs)
get_name3('yuz', 'wang' , middle='hello', yit='world',ye = 'yes')#middle yit ye是随便取名的 **代表关键字

#com+b查看函数的源代码
open()