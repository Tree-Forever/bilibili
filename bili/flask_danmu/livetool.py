import requests
import json
import time
import os
from get_data import load_json,save_json

fp='livetool_status.json'

def get_liveStatus(MID):
    url = 'https://api.bilibili.com/x/space/acc/info'
    params = {
        'mid' : MID, #uid
        'jsonp' : 'jsonp'
    }
    r = requests.get(url,params=params, timeout=5)
    js = r.json()
    return js['data']['live_room']['liveStatus']


old_list = []
class Danmu:
    def __init__(self,UPNAME,ROOMID):
        self.url = 'https://api.live.bilibili.com/ajax/msg'
        self.data = {
            'roomid' : ROOMID, #roomid
            'csrf_token' : '',
            'csrf' : '',
            'visit_id' : ''
        }
        self.savepath = os.path.join('static','txt',time.strftime("%Y-%m-%d-"+UPNAME+".getting", time.localtime()))
        self.startime = ['', 0] #0表示未记录
        self.endtime = ''
    
    def get_danmu(self):
        try:
            html = requests.post(self.url,data=self.data, timeout=5)
        except requests.exceptions.RequestException as e:
            pass
        html.json()
        self.text_danmu(eval(html.text))

    def text_danmu(self,html):
        if self.startime[1]==0:
            self.startime = [html['data']['room'][0]['timeline'],1]
        self.endtime = html['data']['room'][-1]['timeline']

        global old_list
        temp_list = []  #html['data']['room']

        for text in html['data']['room']:
            temp_list.append(text['text'])

            
        if temp_list == old_list:
            pass
        else:
            self.endtime = html['data']['room'][-1]['timeline']
            
            for text_number in range (1,11):
                if "".join(temp_list[:text_number]) in "".join(old_list):
                    pass
                else:
                    try:
                        data = html['data']['room'][text_number-1]
                        
                        #print(data['timeline'],data['nickname'],data['text'],sep='\t')
                        
                        with open(self.savepath,'a+') as f:
                            s = '\t'.join([data['timeline'],data['nickname'],data['text']])
                            f.write(s+'\n')
                    except:
                        pass

            old_list = temp_list[:]
