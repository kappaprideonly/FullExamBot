
for i in range(1, 27):
    f = open(f"data/task_{i}.txt", "r")
    text = f.read()

    sharp = False
    for char in range(len(text)):
        if text[char] == '#':
            if sharp:
                print(i)
            sharp = True
        elif text[char] == '&':
            if not sharp:
                print("&", i)
                print(text[char - 10:char + 10])
            sharp = False
print("\nend\n")
