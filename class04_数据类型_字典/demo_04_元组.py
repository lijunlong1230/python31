"""元组。

"""

# 元组的表示：()
# names = ("yuz", "nobody")
# print(names)
#
# # 空元组
# names = ()
# print(type(names))
# print(len(names))

# 1 个元素的元组
# TODO: 1 个元素的元组，一定要在元素后面加逗号
# 如果不加逗号，数据类型这个元素的数据类型
names = ('yuz')  == 'yuz'

names = ('yuz', )
print(len(names))   # 1
print(type(names))   # tuple, str, 0

# 元组是不可以变的类型
# names[0] = 'wuming'

# 元组是有序的，可以通过索引和切片进行操作

# 元组：解包。 拆包
a, b, c = ('yuz', 'lucky', '阿东')
print(a)
print(b)
print(c)

# a, b = ('yuz', 'lucky', '阿东')
# print(a)
# print(b)

a, b, c = 3, 4, 5

# 什么时候用元组
# 元组（不可以修改的情况下。）
# 元组性能要强于列表
