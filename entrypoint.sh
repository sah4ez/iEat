#!/bin/bash

BASE_DIR=/home/bot
TOKEN=token.txt

if [ -z $(cat ${BASE_DIR}/token/${TOKEN}) ]
then
  echo "Not found ~/token/${TOKEN} file"
else
  python3 ${BASE_DIR}/bot.py $(cat ${BASE_DIR}/token/${TOKEN})
fi