import wikipediaapi
from hanziconv import HanziConv
import requests
import hashlib

wiki = wikipediaapi.Wikipedia('zh')
# pages = ['热敏电阻']
url = "http://localhost:8983/solr/test/update/json/docs"
pages = ['感測器', '無線感測網路', '自動調溫器', '智能感測器', '胎壓偵測系統', '電流感測器', '穩壓器', '電信號', '热敏电阻', '变频器', '同步電動機', '异步电动机']
for page in pages:
    page_content = wiki.page(page)
    data = {
        'id': hashlib.sha224(page_content.title.encode('utf-8')).hexdigest(),
        'title': page_content.title,
        'summary_txt_cjk': HanziConv.toSimplified(page_content.summary),
        'text_txt_cjk': HanziConv.toSimplified(page_content.text),
    }
    #print(data)
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.text)
print("Done.")