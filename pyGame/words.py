import json
import text_1
import random

# сохранение переменной
data = {}
data = {'learned':[1,2,3], 'needRepeat':[]}
complexity = 5 # сложность (5 пар слов в ряд)
remainingWords = []


with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    # print(loaded_data)

    for z in range(len(text_1.text.split('\n'))):
        if z in loaded_data['learned']:
            True
        else:
            remainingWords.append(z)
    
    # print(z)

    # print(remainingWords)
    # print('remainingWords',remainingWords)

    # print(len(text_1.text.split('\n')))
    # print(loaded_data['learned'])
    # print(loaded_data['learned'][0])
    # print(loaded_data['needRepeat'])

def saveLevel():
    with open('data.json', 'w', encoding='utf-8') as f:    
        json.dump(data, f, ensure_ascii=False, indent=4)
    

# получаем список слов случайным образом из списка 998 вариантов часто использщуемых 
def getWords():
    arr = []
    for k in range(complexity):        
        rand = random.choice(remainingWords)
        remainingWords.remove(rand)
        # print('--', rand)
        arr.append( text_1.text.split('\n')[rand].split('—'),)
    return arr


# print(getWords())