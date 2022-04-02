
def create_list5(tasks):
    all = open("../tasks/task5.txt", "r")
    
    all.close()
    all = open("../tasks/task5.txt", "r")

    while True:
        line = all.readline()
        if line == '':
            return
        answer = ""

        if "№" in line:
            line = all.readline()
            for i in range(3):
                all.readline()
        
        sentences = []
        sentences.append(line)
        for i in range(5):
            line = all.readline()
            if line[:6] != "Ответ:":
                sentences.append(line)
                all.readline()
                continue
            answer = line.split()[1]
            
        if answer == "":
            line = all.readline()
            answer = line.split()[1]

        tasks.append([sentences, [answer]])
