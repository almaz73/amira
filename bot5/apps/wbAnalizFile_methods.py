# сохраняем в базе и читаем id созданого файла аналитики
# Если id не сегодняшний, отдаем пустой

import sqlite3
from datetime import date

def ifNoExistUUID(t):
    t.execute("""CREATE TABLE wb_uuid_date(
            store_token TEXT PRIMARY KEY,
            tg_id INTEGER,
            uuid TEXT,
            dtime TEXT,
            )""")

def ifNoExist(t):
    t.execute("""CREATE TABLE wb_analiz_file(
            store_token TEXT PRIMARY KEY,
            tg_id INTEGER,
            uuid TEXT,
            dtime TEXT,
            )""")

## разпечатка всего
def printTable(t):
    print('P R I N T ')
    t.execute(f"""SELECT * FROM stores""")
    for i in t.fetchall():
        print('===', i)



# запоминаем id и время файла аналитики
def save(val, vv):
    print('valvalval=',val )
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"INSERT INTO wb_analiz_file  WHERE uuid='{uuid}'")
    db.commit()
    db.close()

# файл аналитики
def saveFile(val):
    pass

# файл аналитики
def readFile():
    pass

# не нужно ли обновлять данные
def read():
    pass



