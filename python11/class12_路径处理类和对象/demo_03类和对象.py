'''
class 类名：
	类的组成部分。。。。
什么是类class，类是一个群体
什么是对象，对象是类的成员，个体
'''
import time
#表示方法1：
class Man:
	gender = '男'
	power = '强'

print(Man.power)#Man类的power属性
print(Man.gender)


new_man = Man
print(new_man)
a = Man
b = Man
#is判断两个变量的值,是否是同一个对象
print(a is b)
#进一步确定是不是同一个对象
print(id(a))
time.sleep(5)
print(id(b))#应该不是一个id才对，对此运行会显示出两个不同的id
