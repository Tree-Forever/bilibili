import requests

uid='393396916'
cookie="_uuid=22E4F3E2-655A-09F1-3FF9-5D93289332A122944infoc; buvid3=4BC649D2-77E9-4886-865D-39C98E18DB1034786infoc; buvid_fp=4BC649D2-77E9-4886-865D-39C98E18DB1034786infoc; LIVE_BUVID=AUTO9716253233965083; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u|JlmuY~)k0J'uYklJkJR~); fingerprint_s=63a385be76e77ef926d1ce8dd5110cad; CURRENT_BLACKGAP=1; fingerprint3=aacaa71630e4e408aef717bacc473c6a; fingerprint=afd7f8f35cb2efc2e27bc2c40916d51e; buvid_fp_plain=3C618630-4CAD-4F07-AD2C-53FB78F57DDB184985infoc; SESSDATA=158a6b25%2C1645715486%2Ce6499%2A81; bili_jct=4838e003038443abec563258dea1aedc; DedeUserID=16642032; DedeUserID__ckMd5=740a58b144166afe; sid=jyecbvqz; CURRENT_QUALITY=64; bp_video_offset_16642032=573574044657170258; PVID=5; innersign=0; bp_t_offset_16642032=573582888001174917; bfe_id=1bad38f44e358ca77469025e0405c4a6"

url = 'https://api.bilibili.com/x/space/acc/relation'
params = {'mid':uid}
headers = {
       'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
       'Cookie':cookie,
       'Upgrade-Insecure-Requests':'1',
       'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
       'sec-ch-ua':'Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
       'sec-ch-ua-mobile':'?0',
       'sec-ch-ua-platform':'"Windows"',
}

r = requests.get(url,params=params,headers=headers)

print(r.text)
