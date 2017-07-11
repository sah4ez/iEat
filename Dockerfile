FROM python:3.6.1

RUN mkdir -p /home/bot

COPY bot.py /home/bot/bot.py
COPY config.py /home/bot/config.py
COPY requirements.txt /home/bot/requirements.txt
COPY entrypoint.sh /home/bot/entrypoint.sh

RUN chmod 775 /home/bot/entrypoint.sh &&\
 pip install -r /home/bot/requirements.txt

ENTRYPOINT ["/home/bot/entrypoint.sh"]
