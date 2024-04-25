import sqlite3

class Database() : 

    def __init__(self,db) -> None:
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Pack (id integer PRIMARY KEY , name text
                         ,family text , packname text ,password text)""")
        self.con.commit()

    def insert(self,name,family,packname,password):
        self.cur.execute("""INSERT INTO Pack VALUES (NULL,?,?,?,?)""",(name,family,packname,password))
        self.con.commit()

    def fetch(self):
        self.cur.execute("""SELECT * FROM Pack """)
        fetch = self.cur.fetchall()
        return fetch

    def remove(self,id):
        self.cur.execute("""DELETE FROM Pack WHERE id = ? """,(id,))
        self.con.commit()

    def system_password(self,password):
        self.cur.execute(''' SELECT * FROM Pack WHERE password = ? ''',(password,))
        fetch = self.cur.fetchall()
        return fetch

                        # shafiei



