from random import randint

def return_task(tasks):
    num = randint(0, len(tasks) - 1)
    string = ""
    for i in range(len(tasks[num][0])):
        string += '\n' + str(tasks[num][0][i])
    return string, tasks[num][1]