import requests
from bot_4 import env
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Russian')  # Русификация

API_KEY = env.WB_KEY
TG_KEY = env.TELEGRAM_TOKEN
TG_CHAT = env.TELEGRAM_CHAT

def getSimpleDate(text):
    date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_object.strftime("%d %B %Y") 
    return formatted_date


def sendMessageToTelegram(text):
    # text += ':::::::::::::::::::::'
    urlTG = 'https://api.telegram.org/bot'+TG_KEY+'/sendMessage?chat_id='+TG_CHAT+'&parse_mode=HTML&text='+text
    resp = requests.get(urlTG)
    if resp.status_code == 200:
        print ('Телеграмм отправлен. Всё OK!')

def prepare_items(response):
    text = ''
    for i in response:    
        if i['allowUnload'] and i['coefficient']>-1 and i['boxTypeName'] == 'Короба':
            if i['coefficient'] == 0: 
                dt = getSimpleDate(i['date'])
                text += dt +'  \n\n'+ i['warehouseName']+'  '+ 'Бесплатно '+'\n\n 🌷🌷🌷'
                print(i['date'] , i['warehouseName'],  'Бесплатно')
            else: 
                text += dt +'  \n\n'+ i['warehouseName']+'  '+ '✕'+i['coefficient']+'  😫🌷😫'
                print(i['date'] , i['warehouseName'], 'коэф = ', i['coefficient'])
    if not text:
        text = 'Нет свободных слотов 🤔😡'
    sendMessageToTelegram(text)

#  😫 🌷 😡

# Склад 
# Коэффициенты приёмки
url = 'http://supplies-api.wildberries.ru/api/v1/acceptance/coefficients'

# Список складов
# url = "https://supplies-api.wildberries.ru/api/v1/warehouses"

headers = {'Authorization': f'Bearer {API_KEY}','Content-Type': 'application/json'}

# Определите параметры запроса 
params = {
    'warehouseIDs': [117986]             # ID склада, (117986 - Казань)
}

response = requests.get(url, headers=headers, params=params)
print('response', response)

# # Проверьте статус ответа
if response.status_code == 200:
    # Если запрос успешен, обработайте данные
    # print('response = ', response)
    data = response.json()
    # print('Ж Ж Ж Ж Ж  data = ',data)
    prepare_items(data)
    # print("Коэффициенты приемки::::: ", json.loads(json.dumps(data, indent=2)))
else:
    # Если произошла ошибка, выведите сообщение об ошибке
    print(f"Ошибка {response.status_code}: {response.text}")




