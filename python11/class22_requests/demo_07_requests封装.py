import logging
from pprint import pprint
import requests

#在接口当中传递参数的三种方式：params就是表示url上面添加数据传输  data就是form表单方式提交传输 json就是json格式数据传输
def visit(url,params=None,data=None,json=None,method='get',**kwargs):
	req = requests.request(method,url=url,params=params,data=data,json=json,**kwargs)
	try:
		return req.json()
	except Exception as e:
		logging.error("返回的不是json数据{}".format(e))
		return None

if __name__ == '__main__':
	url1 = 'http://api.keyou.site:8000/user/login/'
	url = 'http://api.keyou.site:8000/interfaces/'
	user = {
		"username": "lemon1",
		"password": "123456"
	}
	login=visit(url1,method='post',json=user)
	print(login)
	token = login['token']
	headers = {
		"Authorization":"JWT {}".format(token)
	}
	data = visit(url,method='get',headers=headers)

