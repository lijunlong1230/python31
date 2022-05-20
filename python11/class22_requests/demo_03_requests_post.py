from pprint import pprint

import requests

#发送post请求
url = 'http://api.keyou.site:8000/user/login/'

#发送参数的方式
#URL：query string:查询字符串。get基本上就是用的query string
#body：form/json
#header

#form表单格式数据
user = {
	"username":"lemon1",
	"password":"123456"
}
#data 表示form表单格式数据
res = requests.post(url,data=user)

#json表单格式数据 json关键字
res = requests.post(url,json=user)

#有的接口只支持form表单 有的只支持json，这个是由后端程序员定义的

print(res)
print(res.text)
pprint(res.content)
pprint(res.json())


