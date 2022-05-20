import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(
	host="127.0.0.1",
	port=3306,
	user="root",
	password="li19871230",
	charset="utf8",
	cursorclass=DictCursor
					   )
cursor = conn.cursor()
cursor.execute("select * from future.member;")
member = cursor.fetchone()
print(member)