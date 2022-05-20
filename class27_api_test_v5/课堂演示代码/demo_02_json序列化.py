

# 为什么要把 json 格式的字符串转化成字典
json_data = '{"mobile_phone":true, "pwd":"12345678","type":1}'

import json

# 把 json 数据转化成python 字典
dict_data = json.loads(json_data)
print(dict_data)

# eval()

#1、json.dumps()和json.loads()是对json格式的数据进行处理的函数（可将json理解为字符串）
# 　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可理解为：json.dumps()函数是将字典转化为字符串）
# 　　(2)json.loads()函数是将json格式的数据转换为字典（可理解为：json.loads()函数是将字符串转化为字典）
#
# 2、json.load()和json.dump()主要用来读写json文件的函数
# ————————————————
# 版权声明：本文为CSDN博主「晨曦星语」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_21240643/article/details/96327190
# 把字典转化成 json 字符串
new_dict_data = {'username': 'yuz', 'password': None, 'female': False}
json_data = json.dumps(new_dict_data)
print(json_data)