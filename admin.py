import os



def on_test():
    # sudo docker build -t bot_ege_russian .
    # sudo docker run --name=bot_ege_russian --rm bot_ege_russian &
    TOKEN_TEST = "5189421362:AAEhngIQqBuOvXkYP5xd0Bc9zOA1K25_i9A"
    os.system(f"sudo docker build -t bot_ege_russian --build-arg TOKEN={TOKEN_TEST} .")
    os.system("sudo docker run --name=bot_ege_russian --rm bot_ege_russian &")
    return 0

def on_main():
    # sudo docker build -t bot_ege_russian .
    # sudo docker run --name=bot_ege_russian --rm bot_ege_russian &
    TOKEN_MAIN = "5106503513:AAG1oAVILvpRlALr6y8jqdGk0HvVAzhYL1s"
    os.system(f"sudo docker build -t bot_ege_russian --build-arg TOKEN={TOKEN_MAIN} .")
    os.system("sudo docker run --name=bot_ege_russian --rm bot_ege_russian &")
    return 0

def kill():
    os.system("sudo docker kill bot_ege_russian")
    return 0

def main():
    print("1 - запустить бота на полигоне, 2 - запустить бота на основе, 3 - выключить бота")
    match input():
        case "1":
            on_test()
        case "2":
            on_main()
        case "3":
            kill()


if __name__ == "__main__":
    main()