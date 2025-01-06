import json
import text_1
import random



# сохранение переменной
data = {}
data = {'learned':[1,2,3], 'needRepeat':[]}
complexity = 3 # сложность (5 пар слов в ряд)
remainingWords = []


with open('data.json', 'r') as f:
    loaded_data = json.load(f)

    for z in range(len(text_1.text.split('\n'))):
        if z in loaded_data['learned']:
            True
        else:
            remainingWords.append(z)

def saveLevel():
    with open('data.json', 'w', encoding='utf-8') as f:    
        json.dump(data, f, ensure_ascii=False, indent=4)

chosenIndex = []

def getChosenIndex():
    return chosenIndex

    
# def get

# получаем список слов случайным образом из списка 998 вариантов часто использщуемых 
def getWords():
    print('  С Т А Р Т  ')
    arr = []
    global chosenIndex
    chosenIndex = []
    # print('remainingWords', remainingWords)

    for k in range(complexity):        
        rand = random.choice(remainingWords)
        remainingWords.remove(rand)
        print('--', rand)
        chosenIndex.append(rand)
        arr.append( text_1.text.split('\n')[rand].split('—'),)
    return [arr, chosenIndex]


def backAfterFinish():
    print('e= == == == == == w-d-d-d-ewe')