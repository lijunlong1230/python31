import random

'''
total=int (input("请输入购买的金额"))
if total<50:
	print("没法享受")
	print("需要支付{0}元".format((total)))
elif 50<=total<=100:
	print("享受10%折扣")
	print("需要支付{0}".format(total*(1-0.1)))
else:
	print("享受20%折扣")
	print("需要支付{0}".format(total*(1-0.2)))
'''


num1=random.randint(1,9)#包含19
print("随机数：{0}".format(num1))
inp=int(input("请输入数字:"))
if inp>=num1:
	print("bigger")
else:
	print("less")

