#!/bin/bash
echo -e "Введите API-KEY-TG!"
read KEY
sudo docker build -t ege_bot --build-arg KEY_TG=$KEY .
sudo docker run --name=ege_bot --rm -e KEY_TG=$KEY ege_bot &