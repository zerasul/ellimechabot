from bot.db import Db_Connector
from datetime import datetime
class Test_db:

    _connector = Db_Connector()


    def test_insert(self):
        self._connector.add_event(datetime.now(),"test","testa")

    def test_Select(self):
        rows=self._connector.get_next_events()
        
        assert rows is not None or len(rows) >0 