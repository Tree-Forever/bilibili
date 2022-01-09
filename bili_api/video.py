import requests
from bs4 import BeautifulSoup
import re

url='https://www.bilibili.com/video/BV1M64y1a7zh'
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': "_uuid=22E4F3E2-655A-09F1-3FF9-5D93289332A122944infoc; buvid3=4BC649D2-77E9-4886-865D-39C98E18DB1034786infoc; buvid_fp=4BC649D2-77E9-4886-865D-39C98E18DB1034786infoc; LIVE_BUVID=AUTO9716253233965083; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u|JlmuY~)k0J'uYklJkJR~); fingerprint_s=63a385be76e77ef926d1ce8dd5110cad; CURRENT_BLACKGAP=1; fingerprint3=aacaa71630e4e408aef717bacc473c6a; fingerprint=afd7f8f35cb2efc2e27bc2c40916d51e; buvid_fp_plain=3C618630-4CAD-4F07-AD2C-53FB78F57DDB184985infoc; SESSDATA=158a6b25%2C1645715486%2Ce6499%2A81; bili_jct=4838e003038443abec563258dea1aedc; DedeUserID=16642032; DedeUserID__ckMd5=740a58b144166afe; sid=jyecbvqz; bp_video_offset_16642032=574301921355642130; CURRENT_QUALITY=80; bp_t_offset_16642032=574305194127033027; _dfcaptcha=8e8ace3fb44b1d7a2bb8726254544daf; innersign=1; bfe_id=5112800f2e3d3cf17a473918472e345c; PVID=6",
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV1K64y1q7Ua/?spm_id_from=333.788.recommend_more_video.4',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
r = requests.get(url,headers=headers)

html = r.text
soup = BeautifulSoup(html,'html.parser')
targets = soup.find_all(attrs={'class':'tag'})


channel=[] #频道
partition=[] #分区
topic=[] #话题
for target in targets:
       if target.find('img') != None:
              channel.append(target.text)
       elif target.a.attrs['href'][0:19] == "//www.bilibili.com/":
              partition.append(target.text.strip())
       elif target.a.attrs['href'][0:22] == "//search.bilibili.com/":
              topic.append(target.text.strip())

print('channel',channel)
print('partition',partition)
print('topic',topic)
