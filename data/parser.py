from bs4 import BeautifulSoup as bs
import requests

for i in range(26):
	print(f"Начинаю парсить задание № {i + 1}")
	with open(f"task_{i + 1}.html") as file:
		src = file.read()
	f = open(f"task_{i + 1}.txt", "w")
	soup = bs(src, "lxml")
	text_tasks = soup.find_all(class_="prob_nums")
	num = 0
	for j in text_tasks:
		num += 1
		print(f"Начинаю парсить ссылку! № {num}")
		url = j.find("a").get("href")
		print(url)
		page = requests.get(url)
		soup_page = bs(page.text, "lxml")
		answer = soup_page.find(class_="answer").get_text()
		text = soup_page.find(class_="pbody").get_text()
		f.write(text + "\n" + "#\n")
		f.write(answer + "\n" + "&\n")
		print("Спарсил! Иду дальше!")
	f.close()
#title = soup.title
#print(title.text)