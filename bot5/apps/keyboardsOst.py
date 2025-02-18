# страница работы добавления и получения остатков привязанных к магазинам

import sqlite3 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def saveOst(store, art):
    path = store+':::'+art
    db = sqlite3.connect('../wb.db')
    t = db.cursor()
    
    # t.execute('DROP TABLE wb_ostatki')
    t.execute(''' CREATE TABLE IF NOT EXISTS wb_ostatki (
      path TEXT PRIMARY KEY,
      store TEXT,              
      article TEXT   
    )''')    
    t.execute("""INSERT INTO wb_ostatki (path,store, article) 
              VALUES (?,?,?)
              ON CONFLICT(path) DO UPDATE SET article = EXCLUDED.article
              """,(path, store, art))
    db.commit()
    db.close()

def deleteOst(store, art):
    path = store+':::'+art
    db = sqlite3.connect('../wb.db')
    t = db.cursor()

    t.execute(''' CREATE TABLE IF NOT EXISTS wb_ostatki (
          path TEXT PRIMARY KEY,
          store TEXT,              
          article TEXT   
        )''')

    t.execute(f"DELETE FROM wb_ostatki WHERE path='{path}'")
    db.commit()
    db.close()

def getOst(store):
    db = sqlite3.connect('../wb.db')
    t = db.cursor()

    t.execute(''' CREATE TABLE IF NOT EXISTS wb_ostatki (
          path TEXT PRIMARY KEY,
          store TEXT,              
          article TEXT   
        )''')

    t.execute(f"SELECT article FROM wb_ostatki WHERE store={store}")
    return t.fetchall()
        

# saveOst('strore111', 1)    
# saveOst('1', '2222')    
# saveOst('1', '9999')    
# saveOst('3', '112233') 

# for el in getOst('1'):
#     print(' = = = ',el[0])
   
# deleteOst('3', '112233')
# 1:::2222

# Создаем объекты инлайн-кнопок
# bt1 = InlineKeyboardButton(text='262',callback_data='262')
# bt2 = InlineKeyboardButton(text='382',callback_data='382')
# bt3 = InlineKeyboardButton(text='463',callback_data='463')
# bt4 = InlineKeyboardButton(text='542',callback_data='542')
# bt5 = InlineKeyboardButton(text='567',callback_data='567')
# bt6 = InlineKeyboardButton(text='755',callback_data='755')

# keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[[bt1, bt2, bt3, bt4, bt5, bt6]]
# )
bt_add = InlineKeyboardButton(text='Добавьте артикул +',callback_data='addOst')

def createOstButtons(lenStores):
    if lenStores == 1:
        osts = getOst(1)
        if len(osts) == 0 : return InlineKeyboardMarkup(inline_keyboard=[[bt_add]])
        else:
            arr = []
            for el in osts:
                ost = InlineKeyboardButton(text=f'{el[0]}',callback_data=f'{el[0]}')
                arr.append(ost)
            arr.append(InlineKeyboardButton(text='+', callback_data='addOst'))
            arr.append(InlineKeyboardButton(text='-', callback_data='delOst'))
            return InlineKeyboardMarkup(inline_keyboard=[arr])




def wb_buttons(store_id):
    return keyboard

def addBts(val):
    list = val[1:-1].split(',')
    for el in list:
        saveOst('1',  str(el).strip().lstrip())

def delBt(val):
    deleteOst('1', val[:-3])
