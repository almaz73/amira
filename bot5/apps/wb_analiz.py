import requests
import env as env
import apps.saveRead as saveRead



params = {'locale':'ru', 'groupBySa': True, 'groupBySize': True, 'groupByBrand':False, 'groupBySubject': False, 'groupByNm': False, 'groupByBarcode': False,'filterPics':1, 'filterVolume':1}
taskId = 0

current_storeUUID = 888

def startOst():
    headers = {'Authorization': f'Bearer {API_KEY_ANALITIKA}', 'Content-Type': 'application/json'}
    url1 = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains' # Создаем отчет
    response = requests.get(url1, headers=headers, params=params)
    taskId = response.json()['data']['taskId']
    return taskId

def analizator(spisok, art):
    # lovaly_art = [ '262','382','463','542','567','755']

    danger =''

    if not isinstance(spisok, list):
        if spisok['title']=='too many requests': 
            print('too many requests')
            return 'WB: Слишком много запросов'
        if spisok['detail']=='not found':
            print('not Found')
            return 'WB: Файл не найден'
        if spisok['detail'].find('Указанный файл не существует'):
            print('not Found')
            return 'WB: Указанный файл не существует'
    else : 
        saveRead.saveFile(spisok, current_storeUUID)
        print('000art ::: ', art)
        for i in spisok:
            found = False

            # поиск по введенному названию артикула
            if len(art)>0 and i['vendorCode'] and i['vendorCode'].find(art)>-1:
                if i['quantityWarehousesFull']<5:
                    found = True

            # if not len(art):
            #     # ищем среди топ товаров
            #     for art2 in lovaly_art:
            #         if i['vendorCode'].find(art2)>-1:
            #             if i['quantityWarehousesFull']<5:
            #                 found = True

            if found:
                txt = '▸'+str(i['quantityWarehousesFull']) + ' 👉 '+i['techSize']+ ' 🌻 ' + i['vendorCode'] +'\n' 
                danger+=txt

    # print('danger:::', danger)
    if not danger: danger=' 👻 Ничего не нейдено'
    return danger


def getOst(taskId, art):
    file = saveRead.readFile(current_storeUUID)
    if file:  
        return analizator(file, art)
    else:
        headers = {'Authorization': f'Bearer {API_KEY_ANALITIKA}', 'Content-Type': 'application/json'}
        url3 = f'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/{taskId}/download'
        response2 = requests.get(url3, headers=headers)
        newfile = response2.json()
        return analizator(newfile, art)


def getTaskId():    
    taskId = startOst()
    saveRead.save(taskId, current_storeUUID)
    print('Создан новый файл анализа')
    return 'Создан новый файл анализа'



def getAnaliz(txt, UUID, token):
    global current_storeUUID
    global API_KEY_ANALITIKA
    API_KEY_ANALITIKA = token
    current_storeUUID = UUID

    taskId = saveRead.read(current_storeUUID)
    if taskId and txt != '0':
        print('БУДУ анализировать')
        return getOst(taskId, txt)        
    else: 
        print('БУДУ создавать новый Файл анализа')
        getTaskId()
        return 'Создан новый файл отчета.'        
        
# getAnaliz('')