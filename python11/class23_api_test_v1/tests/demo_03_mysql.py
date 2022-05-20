from pprint import pprint
import pymysql
from pymysql.cursors import DictCursor


conn = pymysql.connect(
	host="127.0.0.1",
	port=3306,
	user="root",
	password="li19871230",
	charset="utf8",
	cursorclass = DictCursor

)
print(conn)
#初始化游标
cursor = conn.cursor()
print(cursor)
#执行sql语句
#cursor.execute("insert into future.member values (3,'register','POST','手机号长度13位','http://api.lemonban.com/futureloan/member/register',"{mobile_phone:155000000001,pwd:12345678,type:1}","{X-Lemonban-Media-Type:lemonban.v2}","{code:2,msg:无效的手机格式}";)")
cursor.execute("select * from future.member LIMIT 10;")

#得到查询数据
members = cursor.fetchall()
pprint(members)

#得到一条记录
#每次都要获取游标
# cursor2 = conn.cursor()
# cursor2.execute("select * from future.member LIMIT 10:")
# member = cursor2.fetchone()
# print(member)

#游标对象关闭
cursor.close()
#链接对象关闭
conn.close()
