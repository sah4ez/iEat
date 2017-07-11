FROM python:3.6.1

RUN mkdir -p -m 750 /home/bot /home/bot/token

ADD requirements.txt /home/bot/requirements.txt
RUN pip install -r /home/bot/requirements.txt

ADD bot.py /home/bot/bot.py
ADD config.py /home/bot/config.py
ADD entrypoint.sh /home/bot/entrypoint.sh

RUN chmod 775 /home/bot/entrypoint.sh

ENTRYPOINT ["/home/bot/entrypoint.sh"]
