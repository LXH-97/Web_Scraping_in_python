#试试跨链接批量爬取网页
#用BeautifulSoup

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import wkhtmltopdf

def check_link(url):
    #try to link the destination web.
    try:
        urlopen("http://www.w3school.com.cn/css/index.asp")
        return "Success Link!"
    except:
        return "404 Error"

def get_link(url):
    #单独页面的爬取
    content = requests.get(url)
    soup = BeautifulSoup(content.content, "html5lib")
    body = soup.find_all(id="course")[0]
    html = str(body)
    with open("text.html", "wb") as f:
        f.write(html)

def get_next_link(url):
    #Get all url-list directory.
    reponse = requests.get("http://www.w3school.com.cn/css/index.asp")
    soup = BeautifulSoup(reponse.content, "html5lib")[1]
    menu_tag = soup.find_all()
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.w3school.com.cn" + li.a.get('href')
        urls.append(url)
    return urls

def save_pdf(htmls):
    # Turn html file to pdf file.
    option = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'custom-header':[
            ('Accept-Encoding','gzip')
        ]
    }
    pdfkit.from_file(htmls,file_name, options=options)

save_pdf(htmls)

#写入文本