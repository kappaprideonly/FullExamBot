FROM python:3.10.2

RUN mkdir -p /usr/src/ege_bot/

WORKDIR /usr/src/ege_bot/

COPY . /usr/src/ege_bot/

ARG KEY_TG=production
ENV KEY_TG="${KEY_TG}"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]