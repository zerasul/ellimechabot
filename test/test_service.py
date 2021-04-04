from bot.events import EventService,Event
from datetime import datetime

class test_service:

    service=EventService()

    def test_addEvent(self):
        self.service.add_event(datetime.now(),'tests','user1')
    
    def test_getEvents(self):
        lista=self.service.getTodayEvents()
        assert len(lista) >0
