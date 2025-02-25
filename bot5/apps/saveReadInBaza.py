import sqlite3
from datetime import date, datetime, timedelta
import uuid

'''
    get_wb_token(uuid)

    wb_save_Link(link, uuid)
    wb_read_Link(uuid)

    wb_save_file(file, uuid)
    wb_read_file(uuid)
'''
'''
1. Нужно сохранить ссылку на сформирвоанный файл 
    (link, date, uuid - примари) 
    - прочитать потом по uuid
2. Нужно сохранить скачанный файл по остаткам магазина
    (файл, uuid - примари)
    - прочитать по uuid
3. Нужен метод по uuid получить ТОКЕН

'''



def ifNoExistLink(t):
    t.execute('''CREATE TABLE IF NOT EXISTS links_to_wb_file (
         uuid TEXT PRIMARY KEY,
         link TEXT,
         dtime TEXT)''')


def ifNoExistFile(t):
    t.execute('''CREATE TABLE IF NOT EXISTS wb_file (
         uuid TEXT PRIMARY KEY,
         file TEXT)''')


## visit('МАША', 7777)
## print(datetime.now())
## print(datetime.strptime('2025-10-10T12:12:12Z', "%Y-%m-%dT%H:%M:%SZ").date())
## print(datetime.strptime('12/15/2021', '%m/%d/%Y').date())

## Если не существует создадим
def ifNoExist(t):
    t.execute('''CREATE TABLE IF NOT EXISTS stores (
         store_token TEXT PRIMARY KEY,
         tg_id INTEGER,
         uuid TEXT,
         dtime TEXT,
         store_name TEXT,
         arts TEXT)''')


## разпечатка всего
def printTable(t):
    print('PRINT stores')
    t.execute(f"""SELECT * FROM stores""")
    for i in t.fetchall():
        print('===', i)


## получаем njrty по uuid (uuid придуман чтобы не тащить с собой везде длинный токен)
def get_wb_token(uuid):
    db = sqlite3.connect('../baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"SELECT store_token FROM stores WHERE uuid='{uuid}'")
    # ans = t.fetchone()[0]
    ans = t.fetchone()
    if ans: ans = ans[0]
    print('ТОКЕН = ', ans)
    db.commit()
    db.close()
    return ans


# print( '>>> ',wb_token('07d341e5efc040eea4a5384109919961'))
# print('>>', wb_token('98b2ba1e62ed4d31b187d3c4dff3f0fa'))


def wb_save_Link(link, uuid):
    db = sqlite3.connect('../baza.db')
    t = db.cursor()
    ifNoExistLink(t)
    t.execute(f"""INSERT INTO links_to_wb_file (link, uuid, dtime) 
         VALUES (?,?,datetime('now'))
         ON CONFLICT(uuid) DO UPDATE SET link=EXCLUDED.link, dtime=datetime('now')
         """, (link, uuid))
    # t.execute("DELETE FROM links_to_wb_file ")
    db.commit()
    db.close()


# wb_save_Link('link1112233', '07d341e5efc040eea4a5384109919961')
# wb_save_Link('link11124443', '07d341e5efc040eea4a5384109919961')
# wb_save_Link('link11777', '07d341e5efc040eea4a5384109919961')


def wb_read_Link(uuid):
    db = sqlite3.connect('../baza.db')
    t = db.cursor()
    ifNoExistLink(t)
    t.execute(f"SELECT  dtime, link FROM links_to_wb_file WHERE uuid='{uuid}'")
    ans = t.fetchone()
    db.commit()
    db.close()
    today = date.today()

    if ans: ans = ans[0]
    # today = today - timedelta(days=1)
    if not ans or str(today) != ans[0][:10]: return 'Указанный файл не существует'
    else: return ans[1]

# print('>>>', wb_read_Link('07d341e5efc040eea4a5384109919961'))


def wb_save_file(file, uuid):
    db = sqlite3.connect('../baza.db')
    t = db.cursor()
    ifNoExistFile(t)
    t.execute(f"""INSERT INTO wb_file (uuid, file) 
         VALUES (?,?)
         ON CONFLICT(uuid) DO UPDATE SET file=EXCLUDED.file
         """, (uuid, file))
    # t.execute("DELETE FROM wb_file ")
    db.commit()
    db.close()

# wb_save_file("92929292929292", 'uuid1212-1212')
# wb_save_file('0293 2 2 23 3203923902309230--23-2 -23-23-23-23-23', '8877887link')

def wb_read_file(uuid):
    db = sqlite3.connect('../baza.db')
    t = db.cursor()
    ifNoExistFile(t)
    t.execute(f"SELECT file FROM wb_file WHERE uuid='{uuid}'")
    # t.execute("DELETE FROM wb_file ")
    ans = t.fetchone()
    if ans: ans = ans[0]
    db.commit()
    db.close()
    if ans:
        return ans
    else:
        # 'Файл аналитики не существует'
        return None

# print(wb_read_file('8877887link'))