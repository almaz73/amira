import requests
from bot_4 import env

API_KEY = env.WB_KEY
API_KEY_ANALITIKA = env.API_KEY_ANALITIKA
SELLER_ID = env.SELLER_ID


def prepare_items(response):
    text = ''
    print(' > > >response=', response)



    if not text:
        text = 'Нет свободных слотов 🤔😡\n\n'
    print('text', text)
    return text


# Склад   Коэффициенты приёмки
# url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients'
# url = 'https://suppliers-api.wildberries.ru/api/v3/warehouses'
# url = "https://suppliers-api.wildberries.ru/api/v1/stocks"
# url = 'https://seller-weekly-report.wildberries.ru/ns/balances/analytics-back/api/v1/balances?limit=2&offset=0'
# url = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/downloads'
# url = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/downloads'
# url = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains'  # Отчёт об остатках на складах
url  = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/00c44885-3f10-4c27-9d7d-33bdb30ca75c/download'
# 'taskId': '409e12d7-f107-47f4-8615-5d7a6dbea576'
# url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients' - склады
headers = {'Authorization': f'Bearer {API_KEY_ANALITIKA}','Content-Type': 'application/json'}
params = {'limit':2, 'groupBySa': True, 'groupBySize': True, 'groupByBrand':False, 'groupBySubject': False, 'groupByNm': False, 'groupByBarcode': False,'filterPics':0, 'filterVolume':0}
# https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains?locale=ru&groupByBrand=false&groupBySubject=false&groupBySa=true&groupByNm=false&groupByBarcode=false&groupBySize=true&filterPics=0&filterVolume=0

def getWB():
    print(' 0 0 0 0 старт>>')

    response = requests.get(url, headers=headers, params=params)
    # response = requests.post(url)

    # print('>>>response',response)

    # # # Проверьте статус ответа
    if response.status_code == 200:
        return prepare_items( response.json())
    else:
        return 'ОШИБКА доступа к ВБ'
    
    
getWB()

