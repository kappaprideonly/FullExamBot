FROM python:latest

RUN mkdir -p /usr/src/bot_ege_russian/

WORKDIR /usr/src/bot_ege_russian/

COPY . /usr/src/bot_ege_russian/

ENV TOKEN="5106503513:AAG1oAVILvpRlALr6y8jqdGk0HvVAzhYL1s"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]