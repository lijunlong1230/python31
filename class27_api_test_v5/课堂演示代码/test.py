# import json
#
# str='{"name":["张三","李四","王二麻子"]}'
# load_dict=json.dumps(str)
# eval_dict=eval(str)
# print(load_dict,type(load_dict))
# print("--------------------------------")
# print(eval_dict,type(eval_dict))
#
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# tinydict2 = {"Name": 'Runoo', "Age": 7, "Class": "First"}
# print("tinydict['Name']: ", type(tinydict))
# print("tinydict2['Age']: ", type(tinydict2))


#!/usr/bin/python
# -*- coding: UTF-8 -*-
# i = '4'
# j = '5'
# k = '7'
#
# num = i+j+k
# print(num)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from decimal import Decimal

# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# num = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         num+=r
#         i=arr[idx]
#     print(r)
#     print ("总金额是："+str(num))


#
# i = int(input("净利润："))
#
# arr = [1000000,600000,400000,200000,100000,0]
# air = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# num = 0
# for idx in range(len(arr)):
#     if i > arr[idx]:
#         r += (i-arr[idx])*air[idx]
#         num += r
#         i = arr[idx]
#     print(r)

l = []
for t in range(3):
    i = int(input("qingshuru:"))
    l.append(i)
l.sort()
print(l)
from pprint import pprint

num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                print(i,j,k)
                num += 1
print(num)

user = "lili"
pwd = 123
if user=="lili" or pwd==123:
    print("duile")
else:
    print("cuole")

import math
for i in range(10000):

    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i+100) and (y*y == i+268):
        print(i)

#递归：可以理解递归就是个for循环 知道循环到最后一个临界值
def recur_fibo(n):
    '''u递归函数，输出斐波那契数列'''
    if n<=1:
        return n
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
recur_fibo(4)
#方法2：
def sum(n):
    if n<=1:
        return 0
    else:
        return n+sum(n-1)


#将一个列表复制到另一个列表
a = [1,3,4]
b = a[:]
print(b)

#阶乘 1*2*3*4*5 所以要从2开始乘，所以num要+1
num = 4
r = 1
for i in range(2, num+1):
    r *= i
print(r)

#黄金分割数兔子的生兔子的问题就是斐波那切数列
a,b = 1,1
for i in range(8):
    a,b = b,a+b
    print(a,b)

#99乘法表
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print ("%d*%d=%d " % (j, i, i*j),end="")

#水仙花数
# a//b，应该是对除以b的结果向负无穷方向取整后的数
n = 2134
#经过试验得知 //向后取整数几个零就去几位数%号后余数
print()
print(n//1000,n//100,n//10,n//1)
print(n//1000,n//100%10,n//10%10,n%10)
print(n%10000,n%1000,n%100,n%10,n%1)
for i in range(100,1000):
    o = i // 100
    j = i // 10 % 10
    k = i % 10
    if i == o**3 + j**3 + k**3:
        print("______________________")
        print(i)


# import string
# s = input('input a string:\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print ('char = %d,space = %d,digit = %d,others = %d'
#        % (letters,space,digit,others))

# #'2+22+222+2222+22222'
# a = int(input("循环几次："))
# b = str(input("要加的数字："))
# n = ""
# m = ""
# for i in range(a):
#     n += b
#     m += '+' + n
#
# pprint(m[1:])

#猴子吃桃反向推理-1应该是默认是递增 从9-0所以后面要加上-1变成递减
x2 = 1
for day in range(9,0,-1):
    x1 = (x2+1) * 2
    x2 = x1
print(x2)


# Python 100例
# 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
# 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，
# 需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

def age(n):
    if n == 1:
        c = 10
        print(c)
    else:
        #如果按照他的计算结果来看，age(n-1)先计算循环这里的的直到c=10,然后再n=5累加2得出18岁
        c = age(n - 1) + 2
        print(c)
    return c
print (age(5))

#递归方式输入的字符串倒序输出
# def output(s, l):
#     if l == 0:
#         return
#     print(s[l - 1])
#     output(s, l - 1)
# s = input('Input a string:')
# l = len(s)
# output(s, l)


#给出任意字符串 倒序输出值
a = 'asdfg'
print("****"+a[-4])
b = len(a)
print(b)
while b != 0:
    print(a[b-1])
    b -= 1
#分别输出字典中的键值 再查看第一个键的值
c = {'1': 2, '4': 5, '8': 3}
print(c.values(),c.keys())
print(c["1"])


n = 2134
print(n//1000,n//100,n//10)
print(n//1000,n//100%10,n//10%10)


#相反的方向输出列表的值 再用，分开各个值并输出
a = [3,2,5,23,554,22]
for i in a[::-1]:
    print(i)
num = ','.join(str(i) for i in a)
print(num)

#创建一个列表用循环加入三个10位元素的列表
n = []
for i in range(3):
    #这个for循环没循环一次都会赋值给前面的j，而不是都循环完后在给到j？
    n.append([i*10+j for j in range(10)])
pprint(n)


#菱形
# n = int(input("请输入菱形数:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")#end=' '意思是末尾不换行，加空格
#     for k in range(i+1):
#         print("* ",end="")
#     print()
# for j in range(n-1):
#     for i in range(j+1):
#         print(" ",end="")
#     for k in range(n-j-1):
#         print("* ",end="")
#     print()

