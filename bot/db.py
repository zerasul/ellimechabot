from sqlite3 import connect
from datetime import datetime

class Db_Connector:
    db_connection=None

    def __init__(self):
        self.db_connection=connect('eventDB.db')
        self._create_database()

    def _create_database(self):
        cursor_obj = self.db_connection.cursor()
        cursor_obj.execute("CREATE TABLE if not exists Events(id integer PRIMARY KEY, date long, title text, user text)")
        self.db_connection.commit()
    

    def get_next_events(self,date=None):
       cursor_obj = self.db_connection.cursor()
       if date is None:
           date = datetime.now()
       rdate=date.date()
       strdate = rdate.strftime('%Y-%m-%d')
       initialdate = datetime.strptime(strdate+' 00:00:00','%Y-%m-%d %H:%M:%S')
       finaldate= datetime.strptime(strdate+' 23:59:59','%Y-%m-%d %H:%M:%S')
       cursor_obj.execute('SELECT * FROM Events where date>? and date<?',(initialdate.timestamp(),finaldate.timestamp()))
       rows = cursor_obj.fetchall()
       return rows

    def add_event(self, date, title, author):
        cursor_obj = self.db_connection.cursor()
        cursor_obj.execute("Insert into Events(date,title,user)values(?,?,?)", (date.timestamp(),title,author))
        self.db_connection.commit()


        
