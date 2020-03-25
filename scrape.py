import requests,webbrowser
from bs4 import BeautifulSoup
from textblob import TextBlob
from pprint import pprint
import re
import pandas

titles=[]
linksArray=[]
user_input=input("Enter to search:")

google_search= requests.get("https://www.google.com/search?q="+user_input)
soup=BeautifulSoup(google_search.text,'lxml')



# print(soup.prettify())
headline_results = soup.findAll("div", {"class": "BNeawe vvjwJb AP7Wnd"})
for fields in headline_results[:6]:
    titles.append(fields.text)
# print((titles))



search_results=soup.select('.kCrYT a')
for link in search_results[:6]:
    mainLink=link.get('href')
    linksArray.append(mainLink)
# print(len(linksArray))








# FOR CSV
df = pandas.DataFrame(data={"Headline": titles, "Link": linksArray})
df.to_csv("./flightStatus.csv", sep=',',index=False)
print("CSV file created")






