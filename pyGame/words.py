import json
import text_1
import random

import tempfile



# сохранение переменной
data = {'learned':[], 'needRepeat':[]}
complexity = 6 # сложность (5 пар слов в ряд)
remainingWords = []

def saveLevel():
    print(' S A V E data=')
    with open('data.json', 'w', encoding='utf-8') as f:    
        json.dump(data, f, ensure_ascii=False, indent=4)

chosenIndex = []

def clearJson():
    global data
    data = {'learned':[], 'needRepeat':[]}
    saveLevel()



with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    data = loaded_data


    for z in range(len(text_1.text.split('\n'))):
        if z in loaded_data['learned']:
            True
        else:
            remainingWords.append(z)

    

    # print(' ___ remainingWords', remainingWords)



def getChosenIndex():
    return chosenIndex

    
# def get

# получаем список слов случайным образом из списка 998 вариантов часто использщуемых 
def getWords():
    print('  СТАРТ #####  ')

    # добавляем то что нужно повторить
    for i in data['needRepeat']:
        if i not in remainingWords: 
            remainingWords.append(i)
    data['needRepeat']=[]
    

    arr = []
    global chosenIndex
    chosenIndex = []

    for k in range(complexity):        
        rand = random.choice(remainingWords)
        remainingWords.remove(rand)
        rrr = text_1.text.split('\n')[rand]
        if rrr:
            chosenIndex.append(rand)
            arr.append(rrr.split('—')) 
        else:
            clearJson()
    # print(' >>> remainingWords', remainingWords)

    return [arr, chosenIndex]


def backAfterFinish(res):
    print('e= == == == == == END == == == == ', res)
    for i in res['ready']:
        if chosenIndex[i] not in data['needRepeat']:
            data['learned'].append(chosenIndex[i])
        else:
            data['needRepeat'].remove(chosenIndex[i]) 
    for i in res['repeat']:
        if chosenIndex[i] not in data['needRepeat']:
            data['needRepeat'].append(chosenIndex[i])
    saveLevel()

    return {'Осталось': len(remainingWords)}

#
