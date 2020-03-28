import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from pprint import pprint
import re
import pandas

user_input=input("Enter to search:")

google_search= requests.get("https://www.google.com/search?q="+user_input)
soup=BeautifulSoup(google_search.text,'html.parser')
# print(soup.prettify())

mydiv = soup.find("div", {"class":"BNeawe deIvCb AP7Wnd"})
print(mydiv.text)

mydiv2 = soup.select("span", {"class":"BNeawe tAd8D AP7Wnd"})
for t in mydiv2:
    print(t.text)
