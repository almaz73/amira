import requests
# import env
from datetime import datetime


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
                print(' = = =')
                 
                dt = getSimpleDate(i['date']) 
                # text += dt +'  \n ✋'+ i['warehouseName']+'  '+ 'Бесплатно '+'\n 🌷🌷🌷\n\n'
                text += dt +'  \n ✋'+ i['warehouseName']+'  '+ 'Бесплатно '+'\n 🌷🌷🌷\n\n'
                print(i['date'] , i['warehouseName'],  'Бесплатно')
            else: 
                dt = getSimpleDate(i['date']) 
                text += dt  +'  \n ☝'+ i['warehouseName'] +'  '+ '✕'
                text += str(i['coefficient']) + '  😫🌷😫\n\n'
               
    if not text:
        text = 'Нет свободных слотов 🤔😡\n\n'
    return text

# Склад   Коэффициенты приёмки
url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients'
params = {'warehouseIDs': [117986]}  # ID склада, (117986 - Казань)

def getWB(key):
    headers = {'Authorization': f'Bearer {key}','Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, params=params)

    # # Проверьте статус ответа
    if response.status_code == 200:
        return prepare_items( response.json())
    else:
        return 'ОШИБКА доступа к ВБ'

