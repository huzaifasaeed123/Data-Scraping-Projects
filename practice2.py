from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup=BeautifulSoup(response.text,"html.parser")
heading=soup.find_all(class_="listicleItem_listicle-item__title__BfenH")
heading.reverse()
with open("movie.txt","w") as file:
    for movie in heading:
        print(movie.getText())
        file.write(movie.getText()+"\n")
#print(soup)