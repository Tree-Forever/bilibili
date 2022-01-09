import json
import requests

avid = '763015513'#av号

url = 'https://api.bilibili.com/x/web-interface/tag/top'
params = {
       'pn' : '1', #页数
       'ps' : '20',#视频数
       'tid' : '1712619' #标签id
}
r = requests.get(url, params=params)

with open('标签.json','w',encoding='utf-8') as f:
       f.write(r.text)
