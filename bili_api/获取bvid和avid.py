import requests
import re

bvid = 'BV1M64y1a7zh'

url = 'https://www.bilibili.com/video/'+bvid
r = requests.get(url)
html = r.text
data = re.search("window.__INITIAL_STATE__=(.*?\"face\":\".*?})", html)
print(data.group(1))










