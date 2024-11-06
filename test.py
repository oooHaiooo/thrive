from  urllib3 import *
from re import *
http = PoolManager()
disable_warnings()
def download(url):
    result = http.request('GET',url)
    htmlStr = result.data.decode('utf-8')
    print(htmlStr)
    return htmlStr

def analyse(htmlStr):
    aList = findall('<a[^>]*>',htmlStr)
    result = []
    for a in aList:
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
        if g != None:
            url = g.group(1)
            url = 'http://172.31.27.133:9999/' + url
            result.append(url)
    return result
def crawler(url):
    print(url)
    html = download(url)
    urls = analyse(html)
    for url in urls:
        crawler(url)
crawler('http://172.31.27.133:9999')
