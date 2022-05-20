from pprint import pprint

import requests

url = 'http://api.keyou.site:8000/interfaces/'
headers = {
	"Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxlbW9uMSIsImV4cCI6MTYxMDk3OTQwMiwiZW1haWwiOiJsZW1vbjEwMEBxcS5jb20ifQ.zd_8m8ShLsSL4XtpR8B7eyMSaU8gLqiZOo7l7oOiHso"
}
res = requests.get(url,headers = headers)
pprint(res.json())