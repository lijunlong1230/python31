import logging

import requests



def visit(url='None',params='None',data='None',json='None',method='get',**kwargs):
	req = requests.request(url=url,params=params,json=json,data=data,method=method,**kwargs)
	try:
		return req.json()
	except Exception as e:
		logging.error("返回错误的数据")
	return None


if __name__ == '__main__':
	url1 = 'http://api.keyou.site:8000/user/login/'
	url = 'http://api.keyou.site:8000/interfaces/'
	user = {
		"username": "lemon1",
		"password": "123456"
	}
	login = visit(url=url1,method='post',data=user)
	print(login)
	token = login['token']
	user_id = login['user_id']
	username = login['username']
	print('***',token,user_id,username)
	headers = {
		"Authorization":"JWT {}".format(token)
	}
	inter = visit(url,method='get',headers=headers)
	print(inter)
