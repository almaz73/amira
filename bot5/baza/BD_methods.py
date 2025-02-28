import sqlite3
from datetime import datetime
import uuid


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
    print('PRINT')
    t.execute(f"""SELECT * FROM stores""")
    for i in t.fetchall():
        print('===', i)

## создание нового уникального ключа
def getNewUUID():
    return uuid.uuid4().hex

## создание/редактирование магазинов
def editOstatki(token, tgId, name, arts, uuid):
    db=sqlite3.connect('baza.db')
    t=db.cursor()
    ifNoExist(t)

    if not name:
        name = 'Магазин_'+datetime.now().strftime('%d.%m.%Y %H:%M')

    if not uuid:
        t.execute(f"""INSERT INTO stores (store_token, tg_id, dtime, store_name, arts, uuid)
                      VALUES(?,?,?,?,?,?)
                      ON CONFLICT(store_token) DO UPDATE SET
                      store_name=EXCLUDED.store_name,
                      arts=EXCLUDED.arts,
                      dtime=datetime('now')"""
                 , (token, tgId, str(datetime.now()), name, arts, getNewUUID()))
    else:
        t.execute(f"""UPDATE stores SET dtime=?, store_name=?, arts=? 
                    WHERE uuid=?""", (str(datetime.now()), name, arts, uuid))

    db.commit()
    db.close()

# editOstatki('token12111212', 567222, 'МА_4', '11,44, 99')
# editOstatki('token333', 3333, 'МАГАЗИН_1', '1,11')
# editOstatki('token3333', 555, 'МА_4', '1,2,3,4,5')
# editOstatki('token1212121212', 1234512, 'M_3', '')

## даление магазина по uuid
def deleteAllStores(uuid):
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"DELETE FROM stores WHERE uuid='{uuid}'")
    db.commit()
    db.close()

## deleteAllStores('a58c2b94535947389340d53e6e5dc2d9')

## получить все магазины и uuid и назманиямагазинов по tgId
def wb_get_store(tgId):
    # print('tgId', tgId)
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    # printTable(t)
    t.execute(f"SELECT store_name, arts, uuid FROM stores WHERE tg_id={tgId}")
    ans = t.fetchall()
    db.commit()
    db.close()
    # print(' a n s = ', ans)
    return ans
# print('>>> ',wb_get_store(567222))

## получить все uuid по tgId
def wb_get_uuid(tgId):
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"SELECT uuid FROM stores WHERE tg_id={tgId}")
    ans = t.fetchall()
    db.commit()
    db.close()
    # print(' a n s = ', ans)
    return ans

## получить все остатки по пользователю
def wb_get_arts(tgId):
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    t.execute(f"SELECT store_name, arts, uuid FROM stores WHERE tg_id={tgId}")
    ans = t.fetchall()
    db.commit()
    db.close()
    # print(' a n s ', ans)
    return ans


def saveDatasFromMiniApp(tgId, datas):
    ## получаем все uuid пользователя
    ## обновляем данные существующих uuid
    ## Если пришел запись без uuid но с токеном заводим новый магазин
    ## не существующие в ответе uuid удаляем из базы (магазин удален)

    myUuids = [] #получаем все uuid пользователя
    for i in  wb_get_uuid(tgId): myUuids.append(i[0])

    stores = {}
    arrStores = datas.split('🐷')
    ind = 0
    for el in arrStores:
        arrEl = el.split('🌞')
        if arrEl[0]:
            ind += 1
            stores[ind] = {'name': arrEl[0], 'art': arrEl[1], 'tokenUuid': arrEl[2]}
    myNewUuids = []
    for i in stores:
        isExist = False
        for u in myUuids:
            if u == stores[i]['tokenUuid']:
                myUuids.remove(u)
                editOstatki(u, tgId, stores[i]['name'], stores[i]['art'], u)
                isExist = True
                # print('EXIST')
        if not isExist:
            myNewUuids.append(stores[i]['tokenUuid'])
            editOstatki(stores[i]['tokenUuid'], tgId, stores[i]['name'], stores[i]['art'], None)
    ## удаляю

    print('НА УДАЛЕНИЕ ', myUuids)
    return False
    for i in myUuids:
        if  not myNewUuids.__contains__(i): deleteAllStores(i)


# saveDatasFromMiniApp(3333, """SHOP_0🌞7, 72, 56,🌞3b876a62eea14a44a5b9775aca0b09fb🐷SHOP_1🌞4, 545🌞7f83378e8a3b4a3ab72a4918bd9e5b99🐷SHOP_2🌞1,🌞111111111111111111111🐷SHOP_22🌞34🌞9-9-9-9-9-9🐷SHOP_88🌞88,17🌞8-8-88🐷""")



# создаем линк для полученния данных из базы
def getSavedStoresBeforeEdit(tgId):
    list = wb_get_store(tgId)
    # print('???list', list)
    link=''
    for i in list:
        link+=i[0]+'🌞'+i[1]+'🌞'+i[2]+'🐷'
    return link
# print('!! ',getSavedStoresBeforeEdit(3333),'!!!!')

def getToken(uuid):
    db = sqlite3.connect('baza.db')
    t = db.cursor()
    ifNoExist(t)
    printTable(t)
    t.execute(f"SELECT store_token FROM stores WHERE uuid='{uuid}'")
    ans = t.fetchone()
    db.commit()
    db.close()
    return ans