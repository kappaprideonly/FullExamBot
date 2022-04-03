f1 = open("words.txt", "r")
f2 = open("blackWords.txt", "w")
vowels = "а,у,о,ы,э,я,ю,ё,и,е".split(",")
vowelsBig = [x.upper() for x in vowels]
words = f1.read().split("\n")
for word in words:
    main_index = -1
    for letter in word:
        if letter in vowelsBig:  # нахождение ударного гласного
            main_index = word.index(letter)
            break
    if main_index != -1:
        count = 0
        for letter in word:  # создание неправильных слов
            if letter in vowels:  # создаем слово, но ударной гласной будет текущая гласная
                badWord = list(word)
                badWord[main_index] = badWord[main_index].lower()
                if badWord[main_index] == "ё":
                    badWord[main_index] = "е"
                badWord[count] = badWord[count].upper()
                f2.write("".join(badWord) + "\n")
            count += 1
    else:
        print(word)
f1.close()
f2.close()
print(len(words))
