from bs4 import BeautifulSoup as bs

with open("task_5.html") as file:
	page = file.read()

soup = bs(page, "lxml")

print(soup.find(class_="something_bred"))



