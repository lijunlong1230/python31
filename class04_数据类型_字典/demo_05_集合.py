"""集合


"""

# 集合表示方法： {}
# 和字典相比，是没有 key 的

my_set = {"yuz", 'caroline', 'zhangjianhua'}
print(my_set)
print(len(my_set))

# 可变  ==》 不可变？？
# 添加，删除
#

# 有没有顺序:::NO!!! 没有顺序的
# 能不能去获取某一个值
# print(my_set[1])
# print(my_set)

# 集合主要的作用
# 是为了去除重复元素
my_set = {"yuz", 'caroline', 'zhangjianhua', 'yuz', 'caroline'}
print(my_set)

# 面试题：：：
# for循环也可以
my_list = ["yuz", 'caroline', 'zhangjianhua', 'yuz', 'caroline']
print( list(set(my_list) ))







