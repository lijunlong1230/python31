import pymysql
from pymysql.cursors import DictCursor


class Mysql_Handler():
	def __init__(self,
				 host=None,
				 port='3306',
				 user=None,
				 password=None,
				 charset='utf-8',
				 cursorclass=DictCursor
				 ):
		self.conn = pymysql.connect(
			host=host,
			port=port,
			user=user,
			password=password,
			charset=charset,
			cursorclass=cursorclass
		)
		self.cursor = self.conn.cursor()

	def query(self,sql,one=True):
		self.conn.commit()
		self.cursor.execute(sql)
		if one:
			return self.cursor.fetchone()
		return self.cursor.fetchall()

	def close(self):
		self.conn.close()
		self.cursor.close()
