import requests
import xml.etree.ElementTree as et

url = "https://www.fsc.gov.tw/RSS/Messages?serno=201202290009&language=chinese"

text = requests.get(url).text

xroot = et.fromstring(text)

for item in xroot.findall("./channel/item"):
    print(item.find("title").text)