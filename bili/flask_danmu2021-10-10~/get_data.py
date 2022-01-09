import requests
import json

fp='livetool_status.json'

def load_json(filepath):
    with open(filepath,'r',encoding='utf-8') as fp:
        return json.loads(fp.read())

def save_json(data,filepath):
    with open(filepath,'w',encoding='utf-8') as fp:
        fp.write(json.dumps(data, indent=4,ensure_ascii=False))


def get_save(MID):
       url ='https://api.bilibili.com/x/space/acc/info'
       params = {
              'mid':MID,
              'jsonp':'jsonp',
       }
       r=requests.get(url,params)
       up_info = json.loads(r.text)
       upname = up_info['data']['name']
       roomid = up_info['data']['live_room']['roomid']

       dic = {
              MID:{
                     "name": upname,
                     "roomid": roomid,
                     "livetool_status": 0
              }
       }
       
       info = load_json(fp)
       info['data'][MID]=dic[MID]
       save_json(info,fp)
