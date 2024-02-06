from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
soup=BeautifulSoup(response.text,"html.parser")
points=soup.find_all("span",class_="score")
numberlist=[]
max_span={}
for span in points:
    split=span.text.split(" ")
    num=int(split[0])
    numberlist.append(num)

max_points=max(numberlist)
for span in points:
    split=span.text.split(" ")
    num=int(split[0])
    if(num==max_points):
        max_span=span

id=max_span.get("id")
span_id=id.split("_")
actual_id=span_id[1]
row=soup.find(id=actual_id) 
sp=row.select_one(".titleline a")
print("Title:Most Points::>>",sp.getText())
print("Link",sp.get("href"))
