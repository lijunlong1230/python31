import requests

#发送post请求
url = 'http://api.keyou.site:8000/user/login/'

#发送参数的方式
#URL：query string:查询字符串。get基本上就是用的query string
#body：form/json
#header

#form表单格式数据
data = {
	"username":"lemon1",
	"password":"123456"
}
#data 表示form表单格式数据
res = requests.post(url,json=data)
print(res)
print(res.text)
print(res.json())

#获取token
res_data = res.json()
token = res_data['token']
print('我是token：'+token)

#访问interface接口
url = "http://api.keyou.site:8000/interfaces/"

headers = {
    "Authorization": "JWT {}".format(token)#JWT后面必须有空格
}

res = requests.get(url,headers = headers)
print('我是response'+str(res.json()))

