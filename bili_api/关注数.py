import requests

uid='393396916' #贾布加布

url = 'https://api.bilibili.com/x/relation/stat?vmid='+uid+'&jsonp=jsonp'
params = {'vmid':uid,
          'jsonp':'jsonp'}
r = requests.get(url,params=params)
print(r.text)
