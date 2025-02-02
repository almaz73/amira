import requests
import env



headers = {'Authorization': f'Bearer {env.API_KEY_ANALITIKA}','Content-Type': 'application/json'}
params = {'locale':'ru', 'groupBySa': True, 'groupBySize': True, 'groupByBrand':False, 'groupBySubject': False, 'groupByNm': False, 'groupByBarcode': False,'filterPics':1, 'filterVolume':1}
taskId = 0

def startOst():
    url1 = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains' # Создаем отчет
    response = requests.get(url1, headers=headers, params=params)
    taskId = response.json()['data']['taskId']
    print('00 taskId', taskId)
    return taskId

def getOst(taskId, art):
    # taskId = 'cf6fd81d-82cc-486c-a4c6-86c0cacc1c41'
    taskId = 'e080495e-8050-4210-bbf2-d5f6688e7da2'
    print('0000 taskId', taskId)
    print('art', art)
    url3 = f'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/{taskId}/download'
    # url3 = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/722eaeba-cc53-4c49-8562-dedb3833244f/download'
    # url3  = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/00c44885-3f10-4c27-9d7d-33bdb30ca75c/download'
    
    print('u r l 3', url3)

    response2 = requests.get(url3, headers=headers)

    spisok = response2.json()

    # lovaly_art = [ '262','382','463','542','567','755']
    lovaly_art = ['463','382']
    # message.text.upper().find('OST')

    danger =''


    if not isinstance(spisok, list):
        print(' ДА Это НЕ список ')
        if spisok['title']=='too many requests': 
            print('too many requests')
            return 'too many requests'
        if spisok['detail']=='not found': 
            print('not Found')
            return 'not Found'
    else : 
        print('99999999999 ЭТО СПИСОК')
        for i in spisok:  
            fond = False

            # поиск по введенному назхванию артикула
            if len(art)>0 and i['vendorCode'] and i['vendorCode'].find(art)>-1:
                if i['quantityWarehousesFull']<5:
                    fond = True

            # ищем среди топ товаров
            for art2 in lovaly_art:
                if i['vendorCode'].find(art2)>-1:
                    if i['quantityWarehousesFull']<5:
                        fond = True

            if fond:
                txt = str(i['quantityWarehousesFull']) + ' ▷'+i['techSize']+ '👉' + i['vendorCode'] +'\n' 
                danger+=txt

    print('danger', danger)
    return danger
   
    
getOst('2323','32')

# startOst()