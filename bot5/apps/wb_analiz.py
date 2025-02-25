import requests
import env as env
import apps.saveRead as saveRead
import apps.saveReadInBaza as saveReadInBaza



headers = {'Authorization': f'Bearer {env.API_KEY_ANALITIKA}', 'Content-Type': 'application/json'}
params = {'locale':'ru', 'groupBySa': True, 'groupBySize': True, 'groupByBrand':False, 'groupBySubject': False, 'groupByNm': False, 'groupByBarcode': False,'filterPics':1, 'filterVolume':1}
taskId = 0

print('!!!!!!!TOKEN = ', saveReadInBaza.get_wb_token('07d341e5efc040eea4a5384109919961'))

def startOst():
    print('__startOst__')
    url1 = 'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains' # Создаем отчет
    response = requests.get(url1, headers=headers, params=params)
    taskId = response.json()['data']['taskId']
    return taskId

def analizator(spisok, art):
    # lovaly_art = [ '262','382','463','542','567','755']

    danger =''


    if not isinstance(spisok, list):
        print('111spisok=', spisok)

        if spisok['title']=='too many requests': 
            print('too many requests')
            return 'WB: Слишком много запросов'
        if spisok['detail']=='not found': 
            print('not Found')
            return 'WB: Файл не найден'
    else :
        print('2222spisok=', spisok)
        # saveRead.saveFile(spisok)
        uuid = 'LINK_838383_9999'
        saveReadInBaza.wb_save_file(spisok, uuid)
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
    # file = saveRead.readFile()
    uuid = 'LINK_838383_9999'
    file = saveReadInBaza.wb_read_file(uuid)
    if file:  
        return analizator(file, art)
    else:    
        url3 = f'https://seller-analytics-api.wildberries.ru/api/v1/warehouse_remains/tasks/{taskId}/download'

        print('__startOst222222__')

        response2 = requests.get(url3, headers=headers)
        newfile = response2.json()
        return analizator(newfile, art)   


def getTaskId():    
    taskId = startOst()
    # saveRead.save(taskId)
    uuid = 'LINK_838383_9999'
    saveReadInBaza.wb_save_Link(taskId, uuid)
    print('Создан новый файл анализа')
    return 'Создан новый файл анализа'
    

def getAnaliz(txt):
    # taskId = saveRead.read()
    uuid = 'LINK_838383_9999'
    taskId = saveReadInBaza.wb_read_Link(uuid)
    if taskId and txt != '0':
        print('БУДУ анализировать')
        return getOst(taskId, txt)        
    else: 
        print('БУДУ создавать новый Файл анализа')
        getTaskId()
        return 'Создан новый файл отчета.'        
        
# getAnaliz('')