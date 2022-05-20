class A():
	bar = 1

	def func1(self):
		print('foo')

	@classmethod
	def func2(cls):
		print('func2')
		print(cls.bar)
		cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化
aa = A.bar = 4
#这个方法只是传值 不是对象不能xxx.方法或者属性
print(aa)

a = A()#是把类方法给了a对象 可以xxx.方法或者属性
setattr(a,"age",30)#如果类方法中不包含属性 可以创建属性age
setattr(a,"bar",5)
print(a.bar + a.age)

#圈住  commond+>收缩所有代码行





