import requests

url = "https://www.fsc.gov.tw/RSS/Messages?serno=201202290009&language=chinese"

text = requests.get(url).text

print(text)