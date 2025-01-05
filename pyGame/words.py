import json
import text_1

# сохранение переменной
data = {'learned':[1,2,3], 'needRepeat':[]}
print(data)
with open('data.json', 'w', encoding='utf-8') as f:    
    json.dump(data, f, ensure_ascii=False, indent=4)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
    print(loaded_data['learned'])
    print(loaded_data['learned'][0])
    print(loaded_data['needRepeat'])

# получаем список слов случайным образом из списка 998 вариантов часто использщуемых 
def getWords():
    # print(len(text_1.text.split('\n')))
    # print('===',range(len(text_1.text.split('\n'))))
    return [ 
      text_1.text.split('\n')[2].split('—'),
      text_1.text.split('\n')[22].split('—'),
      text_1.text.split('\n')[332].split('—'),
      text_1.text.split('\n')[42].split('—'),
      text_1.text.split('\n')[23].split('—')
    ]

print(getWords())