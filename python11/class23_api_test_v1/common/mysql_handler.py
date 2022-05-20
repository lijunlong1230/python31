import pymysql
from pymysql.cursors import DictCursor


class Mysqlhandler():
	def __init__(
			self,
			host=None,
			port=3306,
			user=None,
			password=None,
			charset='utf8',
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
		self.cursor.execute(sql)
		if one:
			return self.cursor.fetchone()
		return self.cursor.fetchall()

	def close(self):
		self.cursor.close()
		self.conn.close()

if __name__ == '__main__':
	db = Mysqlhandler(
		host="127.0.0.1",
		port=3306,
		user="root",
		password="li19871230",
		charset="utf8",
		cursorclass = DictCursor
					  )
	# data = db.query("select * from future.member WHERE mobile_phone={} LIMIT 10;".format(155000011111))
	data = db.query("SELECT * FROM future.memb WHERE mobile_phone={} LIMIT 10;".format(13366655500))
	print(data)