
#输入三个正整数倒叙输出
# l = []
# for t in range(3):
#     i = int(input('integer:\n'))
#     l.append(i)
# l.sort()
# print(l)
# #斐波那契就是从第三个数开始等于前两个数之和
# def fib(n):
# 	if n==1 or n==2:
# 		return 1
# 	return fib(n-1)+fib(n-2)
# print(fib(6))

#阶乘1*2*3*4*5*6
from datetime import time


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))

num = 5
r = 1
for i in range(2, num+1):
    r *= i
print(r)


#斐波那切数列又称为黄金分割数
def test(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        print(a,b)
    return a
test(8)

#将一个列表复制到另一个列表
a = [3,1,5,32,59]
b = []
b = a[:]
print(b)

#99乘法表
#!/usr/bin/python # -*- coding: UTF-8 -*-
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print ("%d*%d=%d" % (j, i, i*j),end="")
#
# #迭代字典并延时一秒输出结果(这个原始的sleep不能用)
# d = {1:'aa',2:'bb'}
# for i in dict.items(d):
#     print(i)
#     time.sleep(1)
for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)

for i in range(100,1000):
    o = i%1000
    j = i%100
    k = i%10
    if i == o**3 + j**3 + k**3:
        print("______________________")
        print(i)

print(213%1000)
print(213%100)
print(213%10)

# i = int(input("请输入大于0的整数:"))
# arr = [1000000,600000,400000,200000,100000,0]
# air = [0.01,0.015,0.03,0.05,0.075,0.1]
# num = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         num+=(i-arr[idx]) * air[idx]
#         i = arr[idx]
#         print(num)


# import math
#
# B = 10000000
#
# for a in range(B):
#     num = int(math.sqrt(a+100))
#     num2 = int(math.sqrt(a+268))
#
#     if (num*num == a+100) and ( num2*num2 == a+268):
#         print(a)

