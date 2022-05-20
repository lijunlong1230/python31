#try 要运行的有可能发生问题的代码段
#except 异常：出现异常时候要运行的代码段，记录日志
lst = ['lijia']
try:
	print(lst[2])
	print('如果报错这段代码不会执行')

except:
	print("记录错误日志")
print('running......运行之后的代码')