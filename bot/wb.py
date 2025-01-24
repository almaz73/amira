import requests
import env
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Russian')  # Русификация

# https://openapi.wildberries.ru/supplies/api/ru/#tag/Informaciya-dlya-formirovaniya-postavok

API_KEY = env.WB_KEY


def getSimpleDate(text):
    days = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
    date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")   
    day = date_object.weekday()
    formatted_date = date_object.strftime("%d.%m.%y") +' ['+days[day]+']'
    return formatted_date

def prepare_items(response):
    text = ''
    for i in response:    
        if i['allowUnload'] and i['coefficient']>-1 and i['boxTypeName'] == 'Короба':
            if i['coefficient'] == 0: 
                dt = getSimpleDate(i['date']) 
                text += dt +'  \n ✋'+ i['warehouseName']+'  '+ 'Бесплатно '+'\n 🌷🌷🌷\n\n'
                print(i['date'] , i['warehouseName'],  'Бесплатно')
            else: 
                text += dt +'  \n ☝'+ i['warehouseName']+'  '+ '✕'+i['coefficient']+'  😫🌷😫\n\n'
                print(i['date'] , i['warehouseName'], 'коэф = ', i['coefficient'])
    if not text:
        text = 'Нет свободных слотов 🤔😡\n\n'
    print('retгкт text', text)
    return text

# Склад   Коэффициенты приёмки
url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients'
headers = {'Authorization': f'Bearer {API_KEY}','Content-Type': 'application/json'}
params = {'warehouseIDs': [117986]}  # ID склада, (117986 - Казань)

def getWB():
    response = requests.get(url, headers=headers, params=params)

    # # Проверьте статус ответа
    if response.status_code == 200:
        return prepare_items( response.json())
    else:
        return 'ОШИБКА доступа к ВБ'

