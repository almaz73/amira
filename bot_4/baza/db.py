import sqlite3
from datetime import datetime

# счетчик посетителей
def visit(name, tgId):
    db = sqlite3.connect('wb.db')
    t = db.cursor()
   
    t.execute(''' CREATE TABLE IF NOT EXISTS user_visits (
      user_id INTEGER PRIMARY KEY,
      name TEXT,    
      count INTEGER DEFAULT 0,
      dtime TEXT
    )''')

    t.execute(f"""INSERT INTO user_visits (user_id, name, count, dtime) 
        VALUES (?,?,1,datetime('now'))
        ON CONFLICT(user_id) DO UPDATE SET count=count+1, dtime=datetime('now')
        """,(tgId, name))

    db.commit()
    db.close()

# Добавление магазинов пользователя
def wb_add_store(tgId, store_key):
    db = sqlite3.connect('wb.db')
    t = db.cursor()
   
    t.execute('''CREATE TABLE IF NOT EXISTS wb_stores (
      key_store_id TEXT PRIMARY KEY,
      user_id INTEGER,
      dtime TEXT)''')
    
    t.execute(f"""INSERT INTO wb_stores (key_store_id, user_id, dtime) 
              VALUES(?,?,?)
              ON CONFLICT(key_store_id) DO UPDATE SET dtime=datetime('now')"""
              ,(store_key,tgId,datetime.now()))

    
    t.execute("SELECT * FROM wb_stores")
    for el in t.fetchall():
        print(el)

    db.commit()
    db.close()

# получить токены магазина по пользователю
def wb_get_store(tgId):
    
    db = sqlite3.connect('wb.db')
    t = db.cursor()
    t.execute(f"SELECT key_store_id FROM wb_stores WHERE user_id={tgId}")
    ans =  t.fetchall()
    db.commit()
    db.close()
    return ans
  
print('811111182 = ',wb_get_store(953446309))


# добавить артикул для пользователя по магазину