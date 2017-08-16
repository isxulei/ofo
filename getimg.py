#!/usr/bin/env python
import urllib
from urllib.request import urlopen,Request
from urllib.parse import urlparse,urlencode
from bs4 import BeautifulSoup
import json
import http.cookiejar
import re
import chardet
import time
def load(start):
    req = Request('https://movie.douban.com/top250?start=' + start)
    data = urlopen(req).read().decode('utf-8')
    imgUrls = re.findall(r'<img alt="(.*)?" src="(.*)?" ',data)
    for i in imgUrls:
        img=urlopen(i[1]).read()
        print ('download %s.jpg from %s....' % (i[0],i[1]))
        with open('img/'+i[0]+'.jpg','wb') as f:
            f.write(img)
        
for i in range(0,250,25):
    if i == 0:
        print("开始下载。。。。") 
    load(str(i))
    time.sleep(1)
    if i == 225:
        print("全部下载完成")
