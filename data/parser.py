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
		information = ""
		answer = soup_page.find(class_="answer")
		text = soup_page.find(class_="pbody")
		text_dop = soup_page.find(class_="probtext")
		if (text != None):
			p_text = text.find_all("p")
			for t in p_text:
				information += t.text + "\n"
		if (text_dop != None):
			p_text_dop = text_dop.find_all("p")
			for t in p_text_dop:
				information += t.text + "\n"
		information += "#\n"
		information += answer.get_text() + "\n" + "&\n"
		f.write(information)
		print("Спарсил! Иду дальше!")
	f.close()
#title = soup.title
#print(title.text)