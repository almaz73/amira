import sqlite3
from datetime import date

def visit(name, tgId):
    db = sqlite3.connect('wb.db')
    t = db.cursor()

    t.execute(''' CREATE TABLE IF NOT EXISTS user_visits (
      id INTEGER PRIMARY KEY,
      name TEXT,    
      count INTEGER DEFAULT 0,
      dtime TEXT
    )''')

    t.execute(f"""INSERT INTO user_visits (id, name, count, dtime) 
            VALUES (?,?,1,datetime('now'))
            ON CONFLICT(id) DO UPDATE SET count=count+1, dtime=datetime('now')
            """,(tgId, name))

    t.execute("SELECT * FROM user_visits")
    for el in t.fetchall():
        print(el)

    db.commit()
    db.close()

visit('Шапито', 999999)