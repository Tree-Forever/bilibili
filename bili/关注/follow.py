from flask import Flask, template_rendered
import requests
import json

from requests.sessions import session

app = Flask(__name__)

@app.route('/1',methods=['GET'])
def index():
       MyUid=16642032
       Page = 1

       url  ='https://api.bilibili.com/x/relation/followings'
       params = {
              'vmid':MyUid, #uid
              'pn':Page,  #page
              'ps':20, # max=50
              'order_type':'attention', # 'attention' or '' 
       }
       headers = {
              'cookie':"b_ut=-1; i-wanna-go-back=1; _uuid=102F889D-9D3E-4B32-1DA4-ED9CEE415CA822888infoc; buvid3=15F06052-DCF8-4F33-9255-95F4458E5B96148794infoc; SESSDATA=0b6eca87%2C1649426443%2C49a5d%2Aa1; bili_jct=550302dd96ec4363364383a39f097b87; DedeUserID=16642032; DedeUserID__ckMd5=740a58b144166afe; sid=k1jbo94k; LIVE_BUVID=AUTO4216338747587335; blackside_state=1; rpdid=|(u|JlmuY~)k0J'uYJJ)~~)R~; CURRENT_BLACKGAP=1; fingerprint3=651b466cef23cb18c2fa0e61f617f6c4; fingerprint=522e24c3e2f8556d42f0dd8816a89eb9; fingerprint_s=b8659e180a6e3b97d0d689ff27cacf4c; buvid_fp=15F06052-DCF8-4F33-9255-95F4458E5B96148794infoc; buvid_fp_plain=15F06052-DCF8-4F33-9255-95F4458E5B96148794infoc; CURRENT_FNVAL=976; CURRENT_QUALITY=80; _dfcaptcha=25b8d44ae820c8e1f27360209bc2baca; innersign=1; bp_t_offset_16642032=582932181401783767; bp_video_offset_16642032=582931854977975582; PVID=12",
       }

       session = requests.Session()
       r = session.get(url,params=params,headers=headers)
       json_data = json.loads(r.text)["data"]

       follower_counts = json_data["total"]
       follower_data = json_data["list"]
       
       return json.dumps(follower_data,ensure_ascii=False)#template_rendered('',follower_data=follower_data)

if __name__ == '__main__':
    app.run()
    

