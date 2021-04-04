from os import environ
from db import Db_Connector
from datetime import datetime

class Event:
    id=0
    date_hour=0
    title=''
    user=''
    guild_id=''
    def __init__(self, id,date,title,user,guild_id=''):
        super().__init__()
        self.id=id
        self.date_hour=date
        self.title=title
        self.user=user
        self.guild_id=guild_id
    def __str__(self):
        return "Evento: '{}', fecha: {}, Organizado por: {}".format(self.title,self.date_hour.strftime('%d-%m-%Y %H:%M'),self.user)

class EventService:

    db_connector=None

    def __init__(self):
       self.db_connector= Db_Connector()
    
    def add_event(self,date,title,user):
        self.db_connector.add_event(date,title,user)
    
    def getTodayEvents(self):
        rows=self.db_connector.get_next_events()
        events=list(map(lambda row: Event(rows[0],datetime.fromtimestamp(row[1]),row[2],row[3]),rows))
        return events
    

