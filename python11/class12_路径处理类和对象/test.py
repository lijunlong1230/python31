class FooParent(object):
	def __init__(self):
		self.parent = 'I\'m the parent.'
		print('Parent')

	def bar(self, message):
		print("%s from Parent" % message)


class FooChild(FooParent):
	def __init__(self):
		# super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
		super(FooChild, self).__init__()
		print('Child')

	def bar(self, message):
		super(FooChild, self).bar(message)
		print('Child bar fuction')
		print(self.parent)


if __name__ == '__main__':
	fooChild = FooChild()
	fooChild.bar('HelloWorld')

# import os
# juedui_path = os.path.abspath('subdir')
# shagnji_path = os.path.dirname(juedui_path)
# if not os.path.exists('subdir'):
# 	print(os.mkdir('subdir'))
# else:
# 	print('yijingyole')

import os
juedui_path = os.path.abspath('subdir')
shagnji_path = os.path.dirname(juedui_path)
if not s.path.exists('subdir'):
	print(os.mkdir('subdir'))
else:
	print('yijingyole')

# with open('/Users/lijunlong/Pycharm/python11/class12_路径处理类和对象/subdir/test1.txt','a') as f:
# 	f.write('new file')
# with open('test1.txt','r') as r:
# 	print(r.read())