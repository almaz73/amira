import sqlite3
from datetime import datetime


def visit(name, tgId):
    db = sqlite3.connect('baza.db')
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
        """, (tgId, name))

    db.commit()
    db.close()

visit('8888_ИВАН', 567222)
visit('МАША', 7777)

# print(datetime.now())
# print(datetime.strptime('2025-10-10T12:12:12Z', "%Y-%m-%dT%H:%M:%SZ").date())
print(datetime.strptime('12/15/2021', '%m/%d/%Y').date())


def ifNoExist(t):
    t.execute('''CREATE TABLE IF NOT EXISTS stores (
         store_token TEXT PRIMARY KEY,
         tg_id INTEGER,
         dtime TEXT,
         store_name TEXT,
         arts TEXT)''')

def printTable(t):
    t.execute(f"""SELECT * FROM stores""")
    for i in t.fetchall():
        print('===', i)



def editOstatki(token, tgId, name, arts):
    db=sqlite3.connect('baza.db')
    t=db.cursor()
    ifNoExist(t)

    if not name:
        name = 'Магазин_'+datetime.now().strftime('%d.%m.%Y %H:%M')

    print(name)

    t.execute(f"""INSERT INTO stores (store_token, tg_id, dtime, store_name, arts)
                  VALUES(?,?,?,?,?)
                  ON CONFLICT(store_token) DO UPDATE SET 
                  store_name=EXCLUDED.store_name,
                  arts=EXCLUDED.arts,
                  dtime=datetime('now')"""
             , (token, tgId, str(datetime.now()), name, arts))

    printTable(t)
    db.commit()
    db.close()

# editOstatki('token12111212', 567222, 'МАГАЗИН_1_333', '11,44')
# editOstatki('token77777777', 3333, 'МАГАЗИН_2', '22')
# editOstatki('token3333', 555, 'МА_4', '1,2,3,4,5')
# editOstatki('token1212121212', 1234512, 'M_3', '')


# получить все токены магазинов по пользователю
def wb_get_store(tgId):
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"SELECT store_token FROM stores WHERE tg_id={tgId}")
    ans = t.fetchall()
    db.commit()
    db.close()
    return ans


# print('==',wb_get_store(777))