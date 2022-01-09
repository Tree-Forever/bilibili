import json
import requests

avid = '763015513'#av号
num = str(0)#页数

url = 'https://api.bilibili.com/x/v2/reply/main'
params = {
       'jsonp':'jsonp',
       'next': num,
       'type': '1',
       'oid': avid,
       'mode': '3',
       'plat': '1'
}
r = requests.get(url, params=params)

with open(num+'.json','w',encoding='utf-8') as f:
       f.write(r.text)
