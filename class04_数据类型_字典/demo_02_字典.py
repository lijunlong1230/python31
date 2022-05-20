# 字典： 也是存储多个数据的

my_songs = ['晴天', '月亮之上', '老男孩', '彩云之南', '义勇军进行曲',
            '分手快乐']

print(my_songs[3])
print(my_songs[4])
# 列表的存储多个数据的时候，不知道元素具体表达的含义。
# 字典能够表示出每个元素具体的意思

# 字典的表示方法 {key: value, key1: value1, key2: value2}
# my_songs = ['晴天', '月亮之上', '老男孩', '彩云之南', '义勇军进行曲',
#             '分手快乐']
my_songs = {"favor": "晴天", "hated":" 月亮之上", "listen_night": "老男孩"}

# 字典的key 是有要求的，不能重复
# my_songs = {"favor": "晴天", "favor":"月亮之上", "listen_night": "老男孩"}
# print(my_songs["favor"])


# 字典的key 应该是能够 hash 哈希
my_songs = {"favor": "晴天", "favor":"月亮之上", "listen_night": "老男孩"}


# 字典的长度
print(len(my_songs))

# 字典的没有索引的， 同样是没有切片的
# 有索引就代表有顺序，列表是有序的
# 字典是什么？ 字典的无序的。
# print(my_songs[0])
print(my_songs)

# IndexError
# ValueError
# KeyError: 字典的key有问题


# 字典可不可以进行修改  ==》字典是可变类型吗？？
my_songs['favor'] = '薇薇'
print(my_songs)




# 删除
# my_songs.pop("favor")
# print(my_songs)




print(my_songs.keys())
print(my_songs.values())
print(my_songs.items())

# 添加 如果 key 不在原来的字典当中，就是添加
# 如果在，就是修改
my_songs["twice"] = 'value'
my_songs["song"] = 'song2'
print(my_songs)
my_songs.pop("song")
print(my_songs.items())

