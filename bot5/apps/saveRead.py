# сохраняем и читаем id созданого файла аналитики
# Если id не сегодняшний, отдаем пустой
import json
import pickle
from datetime import date
import wbAnalizFile_methods as bd_file


# запоминаем id и время файла аналитики
def save(val, current_storeUUID):
    print('### uuid + date сохраняем, чтобы узнать, устарело или нет')

    print('???? SAVE val=',val)
    print('????? DAVE current_storeUUID=', current_storeUUID)

    bd_file.save(val, current_storeUUID)

    with open(current_storeUUID+'.json', 'w', encoding='utf-8') as f:
        text = val + ':||:' + str(date.today())
        print('???? text=', text)
        saveFile('', None) # Чистим файл
        f.write(text)
        f.close()

save('1212', '9999999')

# with open('data.pickle', 'wb') as f:
#      pickle.dump(data, f)

# with open('data.pickle', 'rb') as f:
#      data_new = pickle.load(f)

# файл аналитики
def saveFile(val, storeUUID):

    print('### Сохраняем полученный из WИ данные по магазщину')

    with open(storeUUID+'.pickle', 'wb') as f:
        pickle.dump(val, f)  
        f.close()

# файл аналитики
def readFile(storeUUID):
    print('### Пытаемся прочитать, есть ли больщой фа1йл с данными')
    try:
        print(' БУДУ ЧИТАТЬ ФАЙЛ')
        with open(storeUUID+'.pickle', 'rb') as f:
            list = pickle.load(f)
            f.close()
            return  list
    except FileNotFoundError:
        'Файл аналитики не существует'
        return None
    
# не нужно ли обновлять данные
def read(current_storeUUID):
    print('#### Проверка нет ли необзодимости обновить большой файл')
    print('current_storeUUID', current_storeUUID)
    today = date.today()
    try:
        with open(current_storeUUID+'.json', 'r', encoding='utf-8') as f:
            datas = f.read().split(':||:')
            print('? ?? ?? ?? datas', datas)
            f.close()
            if str(today) != datas[1]: return ''
            else : return datas[0]
    except FileNotFoundError:
        return 'Указанный файл не существует'


# save('4eb6b100-c9b2-4f2b-9ce2-0cf0f7321ee2')
# print('read()=',read())
# save('')

    