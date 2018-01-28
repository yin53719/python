from bs4 import BeautifulSoup
import requests


html=requests.get("https://www.yinzhongchang.cn")

strs =html.text


soup=BeautifulSoup(strs,'lxml')
print(type(soup))
#print(soup.body)