import requests
import json
import time
import os
'''
UPNAME='贝拉'
MID = '672353429'#uid
ROOMID = '22632424'#roomid
'''

UPNAME='阿梓'
MID = '7706705'#uid
ROOMID = '80397'#roomid


'''
UPNAME='向晚'
MID = '672346917'#uid
ROOMID = '22625025'#roomid
'''
'''
UPNAME='两仪滚'
MID = '183430'#uid
ROOMID = '5096'#roomid
'''

def get_liveStatus():
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
    def __init__(self):
        self.url = 'https://api.live.bilibili.com/ajax/msg'
        self.data = {
            'roomid' : ROOMID, #roomid
            'csrf_token' : '',
            'csrf' : '',
            'visit_id' : ''
        }
        self.savepath = time.strftime("%Y-%m-%d-"+UPNAME+".txt", time.localtime())
        self.startime = ['', 0] #0表示未记录
        self.endtime = ''
    
    def get_danmu(self):
        try:
            html = requests.post(self.url,data=self.data, timeout=5)
        except requests.exceptions.RequestException as e:
            print(e)
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
                        
                        print(data['timeline'],data['nickname'],data['text'],sep='\t')
                        with open(self.savepath,'a+') as f:
                            s = ''if data['text']=='dk'or data['text']=='1'or '打卡'in data['text']else data['text']
                            if s!='':
                                f.write(s+'\n')#写入弹幕
                    except:
                        pass

            old_list = temp_list[:]



if __name__ == '__main__':
    url = 'https://api.bilibili.com/x/space/acc/info'
    params = {
        'mid' : MID, #uid
        'jsonp' : 'jsonp'
    }
    js = requests.get(url,params=params, timeout=5).json()
    print('UP主:',js['data']['name'])
    print('直播间状态:',js['data']['live_room']['liveStatus'])
    
    danmu = Danmu()
    while get_liveStatus()==1:
        for i in range(30):
            f = open('0or1.txt','r')
            try:
                if f.read() == '1':
                    danmu.get_danmu()
                    time.sleep(0.5)  #刷新频率
                else:
                    f.close()
                    print('记录时间 %s ——> %s'%(danmu.startime[0], danmu.endtime))
                    os._exit(0)
            except:
                pass
