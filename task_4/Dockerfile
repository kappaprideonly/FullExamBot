FROM python:latest

RUN mkdir -p /usr/src/ege_bot_4/

WORKDIR /usr/src/ege_bot_4/

COPY . /usr/src/ege_bot_4/

ENV TOKEN4="5166064226:AAGpPcf0Xwhp3a8KAv_uebYF2zoD_PI_JIw"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot4.py"]