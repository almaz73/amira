# УСТАРЕЛО, МЕХАНИЗМ ПЕРЕВЕЛ НА РАБОТУ С БАЗОЙ
# сохраняем и читаем id созданого файла аналитики
# Если id не сегодняшний, отдаем пустой
import json
import pickle
from datetime import date

# запоминаем id и время файла аналитики
def save(val):
    with open('wb_ost.json', 'w', encoding='utf-8') as f:
        text = val + ':||:' + str(date.today())
        saveFile('') # Чистим файл 
        f.write(text)        
        f.close()


# with open('data.pickle', 'wb') as f:
#      pickle.dump(data, f)

# with open('data.pickle', 'rb') as f:
#      data_new = pickle.load(f)

# файл аналитики
def saveFile(val):
    with open('wb_File.pickle', 'wb') as f:
        pickle.dump(val, f)  
        f.close()

# файл аналитики
def readFile():
    try:
        with open('wb_File.pickle', 'rb') as f:
            list = pickle.load(f)
            f.close()
            return  list
    except FileNotFoundError:
        'Файл аналитики не существует'
        return None
    
# не нужно ли обновлять данные
def read():
    today = date.today()
    try:
        with open('wb_ost.json', 'r', encoding='utf-8') as f:           
            datas = f.read().split(':||:')
            f.close()
            if str(today) != datas[1]: return ''
            else : return datas[0]
    except FileNotFoundError:
        return 'Указанный файл не существует'


# save('4eb6b100-c9b2-4f2b-9ce2-0cf0f7321ee2')
# print('read()=',read())
# save('')

    