from flask import Flask, request, render_template,send_from_directory
import threading
from concurrent.futures import ThreadPoolExecutor
from livetool import get_liveStatus,Danmu
from get_data import load_json,save_json,get_save
import time
import requests
import os
import re

app = Flask(__name__)
executor =ThreadPoolExecutor(10)

fp='livetool_status.json'

'''
#自定义过滤器
def del_none(s):
    return re.sub('\s','',s)

app.add_template_filter(del_none,'del_none')
'''

#主页
@app.route('/', methods=['GET'])
def hello():
    user_info = load_json(fp)
    user_data = user_info['data']
    #uid - name - live_status - live_tool_status
    inform = [(mid, user_data[mid], get_liveStatus(mid)) for mid in user_data.keys()]
    return render_template('index.html',inform=inform)

#删除UID
@app.route('/a/live/deluid', methods=['GET','POST'])
def deluid():
    if request.method == 'POST':
        user_info = request.form.to_dict()
        mid = user_info.get('del_mid')
        key = user_info.get('key')
        rightkey = '810975'#验证
        if rightkey==key:
            executor.submit(del_uid,mid,fp)
            return "UID:%s 删除成功"%mid
        else:
            return 'KEY ERROR!!'
def del_uid(mid,fp):
    user_info = load_json(fp)
    try:
        user_info['data'].pop(mid)
    except KeyError as e:
        pass
        
    save_json(user_info,fp)
    

#查看文件列表
@app.route('/file/', methods=['GET'])
def file():
    rootpath = os.path.join(os.getcwd(),'static','txt')
    lst = os.listdir(rootpath)
    filesize = ["%.2fKB"%(os.path.getsize(os.path.join(rootpath,i))/1024) for i in lst]
    filedata = zip(lst,filesize)
    filedata=sorted(filedata,key=lambda x:x[0],reverse=True)#(文件名，大小)
    return render_template('file.html',locatepath=rootpath,filedata=filedata)

#查看文件内容
@app.route('/file/<string:filename>/show', methods=['GET'])
def show(filename):
    filepath = os.path.join(os.getcwd(),'static','txt',filename)
    with open(filepath,encoding='utf-8') as f:
        content = [i.split('\t') for i in f.readlines()] #时间 用户 弹幕
    return render_template('file-content.html',content=content)
#下载文件
@app.route('/download/<path:path>', methods=['GET'])
def download(path):
    filename = path
    dirpath = os.path.join(os.getcwd(),'static','txt')

    if os.path.isfile(os.path.join(dirpath,filename)):
        return send_from_directory(dirpath,filename,as_attachment=True)

#启动爬取程序
@app.route('/a/live/startrecord', methods=['POST'])
def startrecord():
    if request.method == 'POST':
        user_info = request.form.to_dict()
        mid = user_info.get('mid')
        key = user_info.get('key')
        rightkey = '810975'
        if rightkey==key:
            if get_liveStatus(mid)==0:
                return "uid:%s 直播间未开播"%mid
            else:
                executor.submit(record,mid)
                return "uid:%s 开始爬取"%mid
        else:
            return 'KEY ERROR!!'

def record(mid):
    user_info = load_json(fp) #判断json是否存有uid ,没有则添加
    if mid not in user_info['data'].keys():
        get_save(mid)
        user_info = load_json(fp)
    
    info = load_json(fp)
    info['data'][mid]['livetool_status']=1
    save_json(info,fp)

    UPNAME=user_info['data'][mid]['name']
    ROOMID=user_info['data'][mid]['roomid']
    danmu = Danmu(UPNAME,ROOMID)
    try:
        while get_liveStatus(mid)==1:
            savepath = danmu.savepath
            changesavepath = os.path.splitext(savepath)[0]+'.txt'
            for i in range(30):
                danmu.get_danmu()
                time.sleep(0.7)  #刷新频率
    finally:
        os.rename(savepath, changesavepath)
        
        info = load_json(fp)
        info['data'][mid]['livetool_status']=0
        save_json(info,fp)


@app.route('/thread', methods=['GET'])
def showthread():
    thread_list = threading.enumerate()
    print(thread_list)
    thread_num = len(threading.enumerate())#线程数量
    s=''
    s += '<h3><b>线程数量:'+str(thread_num)+'</b></h3>'
    for thread in threading.enumerate():
        s += "<p>"+ re.sub('[<>]','',str(thread)) +"</p>"

    return s
    

if __name__ == '__main__':
    app.run()
