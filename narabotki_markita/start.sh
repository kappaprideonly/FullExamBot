#!/bin/bash
sudo docker build -t bot_ege_russian .
sudo docker run --name=bot_ege_russian --rm bot_ege_russian &