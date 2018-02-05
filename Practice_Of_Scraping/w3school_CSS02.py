# python3

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def printPages(articalUrl):
    html = urlopen("view-source:http://www.w3school.com.cn/")
    bsObj = BeautifulSoup(html)
    for links in bsObj.find("div", {"id":"course"}).findAll("a", href=re.compile("/css/css_*_*.asp")):
        if 'href' in links.attrs:
            print(links.attrs['href'])





