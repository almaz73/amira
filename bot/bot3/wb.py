import requests
from bot_4 import env
from datetime import datetime
import time




API_KEY = env.WB_KEY


def getSimpleDate(text):
    days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")   
    day = date_object.weekday()
    formatted_date = date_object.strftime("%d.%m.%y") +' ['+days[day]+']'
    return formatted_date

def prepare_items(response):
    text = ''
    for i in response:   
        if i['allowUnload'] and i['coefficient']>-1 and i['boxTypeName'] == 'Короба':
            dt = getSimpleDate(i['date']) 
            if i['coefficient'] == 0:                
                text += dt +'  \n 👉'+ i['warehouseName']+'  '+ 'Бесплатно '+'\n 🌷🌷🌷\n\n'
            elif i['coefficient']>0 and i['coefficient'] <= 3:                
                text += dt  +'  \n ✋'+ i['warehouseName'] +'  '+ '✕' + str(i['coefficient']) + '  😫🌷😫\n\n'
            elif i['coefficient']>3 and i['coefficient'] <= 6:                
                text += dt  +'  \n ☝'+ i['warehouseName'] +'  '+ '✕' + str(i['coefficient']) + '  😫\n\n'                
            else: 
                text += dt  +'  \n🖕'+ i['warehouseName'] +'  '+ '✕' + str(i['coefficient']) + '  😡😡😡\n\n'              
    if not text:
        text = 'Нет свободных слотов 🤔😡\n\n'
    return text

# Склад   Коэффициенты приёмки
url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients'
headers = {'Authorization': f'Bearer {API_KEY}','Content-Type': 'application/json'}
params = {'warehouseIDs': [117986]}  # ID склада, (117986 - Казань)

def getWB():
    response = requests.get(url, headers=headers, params=params)

    # # # Проверьте статус ответа
    if response.status_code == 200:
        return prepare_items( response.json())
    else:
        return 'ОШИБКА доступа к ВБ'
    
    time.sleep(3)