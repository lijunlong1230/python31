#异常捕获 hi明出席拿的异常类型
#对每一种异常分开处理 ，进行不同的处理
#raise 手动抛出异常 主动报错
lst = ['lijia']
try:
	print(4/0)
	lst[3]
except IndexError as e:
	print("出现异常：{}".format(e))
except ZeroDivisionError as e:
	print('出现触发错误：{}'.format(e))
finally:
	#不管有没有报错，finnally都会执行
	print('我每次都会执行')
def join_girf_team(age,gender):
	if age>22:
		raise ValueError("age must be <22岁")#手动触发异常
	print('可以加入女子足球队')
join_girf_team(21,'女')


