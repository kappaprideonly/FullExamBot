#!/bin/bash
sudo docker build -t bot4 .
sudo docker run --name=bot4 --rm bot4 &