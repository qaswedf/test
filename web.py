import requests
from bs4 import BeautifulSoup

res = requests.get("https://zh.wikipedia.org/wiki/2018%E5%B9%B4%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E7%9B%B4%E8%BD%84%E5%B8%82%E9%95%B7%E5%8F%8A%E7%B8%A3%E5%B8%82%E9%95%B7%E9%81%B8%E8%88%89#_%E8%87%BA%E5%8C%97%E5%B8%82")
# print(res.encoding)
soup = BeautifulSoup(res.text, "html.parser")
table = soup.select("#mw-content-text")
soup2 = table[0].select(".table.wikitable.mw-collapsible.mw-made-collapsible")
print(soup2)