import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

cls = "title"
response = requests.get(URL)
txt = response.text

soup = BeautifulSoup(txt, "html.parser")
titles = []
title_with_numbering = soup.select("h3 ")
# print(title_with_numbering)
for i in title_with_numbering:
    # print(i.text.split(")"))
    titles.append(i.text.split(")"))
titles.reverse()
print("Top 100 movies of all time")
titles[11] = ['12', " The Godfather Part II"]

# print(titles)
for i in titles:
    x = "".join(i[0] + ")"+i[1])
    print(x)