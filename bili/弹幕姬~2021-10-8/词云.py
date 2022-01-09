import win32ui
import jieba
import re
from wordcloud import WordCloud,ImageColorGenerator
from imageio import imread
import matplotlib.pyplot as plt
import os

def select_file():
    dlg= win32ui.CreateFileDialog(1)# 1表示打开文件对话框
    dlg.SetOFNInitialDir('C://Users//月上庭//Desktop')# 设置打开文件对话框中的初始显示目录
    num = dlg.DoModal()
    if num==2:
            os._exit()

    return dlg.GetPathName()# 获取选择的文件名称

def replword(s):
    m=re.split(' ',s.replace('\n',''),1)
    return m[0],m[1] if len(m)>1 else ''


USER_DICT = 'user_dict.txt'# 自定义词库 user_dict.txt
ONEWORD = '单字.txt'       #单字 单字.txt
DELWORD = '屏蔽词.txt'     #屏蔽词 屏蔽词.txt 正则表达式
FIMG = '贝拉.jpg'          #图片遮罩
SAVEPATH = './jpg'

jieba.load_userdict(USER_DICT) 
fn=select_file() # 文本
if fn.endswith('.txt'):
    pass
else:
    print('文档格式错误')
    os.exit(1)
#----------------------------------------
#文本处理
text=open(fn,'r',encoding='utf-8').read()
oneword=open(ONEWORD,'r',encoding="utf-8").read() #单字
delword=open(DELWORD,'r',encoding="utf-8").readlines() #屏蔽词 正则表达式
txt =''

for s in delword: #屏蔽词 屏蔽词.txt
    s1,s2 = replword(s)
    text = re.sub(s1,s2,text)

for ch in "：“”‘’，。！；…\n\t《》": #删除标点符号
    text=text.replace(ch,"") 
words=jieba.lcut(text)
for w in words:
    if len(w)>1 or w in oneword: #防止删除部分单字 单字.txt
        txt=txt+w+' '
#----------------------------------------- 
fimg=FIMG# 图片遮罩
c_mask=imread(fimg)
wc=WordCloud(
    font_path=r'C:\Windows\Fonts\SIMYOU.TTF',
    mask=c_mask, 
    background_color='white', 
    mode="RGB", 
    max_font_size=40,
    min_font_size=8,
    max_words=500, 
    random_state=None, 
    prefer_horizontal=1,
    scale = 5,
    #colormap="hot"
    relative_scaling = 0.5,
    collocations=False,
    )

wt=wc.generate(txt) 
im_color=ImageColorGenerator(c_mask)
wc_img=wt.recolor(color_func=im_color)
plt.imshow(wt, interpolation='bilinear')
plt.show()


wcimg=wc.to_image()
wcimg.save(os.path.join(SAVEPATH,os.path.splitext(os.path.basename(fn))[0])+'.jpg')

