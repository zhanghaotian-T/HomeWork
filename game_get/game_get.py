from bs4 import BeautifulSoup
import requests


html = requests.get('https://cf.qq.com/main.shtml?ADTAG=EventBlackTop.button.btnav.ecter').content
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

print(soup.p)