from bs4 import BeautifulSoup
import lxml
with open("./website.html", "r", encoding="utf-8") as file:
    data = file.read()
# print(data)
soup = BeautifulSoup(data, "html.parser")
# print(soup.p)
# print(soup.a("href"))
# all_angchor_tags = soup.find_all(name="a")
# print(all_angchor_tags)
# for tag in all_angchor_tags:
#     print(tag.get("href"))
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
company_url = soup.select_one(selector="#name")
print(company_url.text)



    