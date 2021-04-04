FROM python:3.9.2

WORKDIR /opt/ellibot
COPY . /opt/ellibot
RUN pip install discord.py
ENV DISCORD_TOKEN="mydiscordtoken"
CMD ["python","bot/ellibot.py"]