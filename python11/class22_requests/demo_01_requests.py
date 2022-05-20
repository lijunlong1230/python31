import requests

#发送get请求 需要传递参数
url = "http://www.baidu.com"
url = "http://api.keyou.site:8000/interfaces/"
# url = 'http://api.keyou.site:8000/user/login/'
res = requests.get(url)
res = requests.post(url)

#响应对象
print(res)
#响应状态码
print(res.status_code)
#获取返回文本的数据
print(res.text)
#获取返回的数据
print(res.content)
#获取返回字典的数据
print(res.json())

