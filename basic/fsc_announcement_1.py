import requests
import xml.etree.ElementTree as et
import jieba
import jieba.analyse
from bs4 import BeautifulSoup

url = "https://www.fsc.gov.tw/RSS/Messages?serno=201202290009&language=chinese"

text = requests.get(url).text

xroot = et.fromstring(text)

for item in xroot.findall("./channel/item"):
    title = item.find("title").text
    description = BeautifulSoup(item.find("description").text).get_text()
    link = item.find("link").text
    pubDate = item.find("pubDate").text
    print(title)
    for x, w in jieba.analyse.extract_tags(description, withWeight=True):
        print('%s %s' % (x, w))
