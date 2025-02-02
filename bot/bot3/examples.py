
# mes = 'ost3453'
# lovaly_art = ['262','382','463','542','567','755']
# text = 'fhfgsh-382'


# for i in lovaly_art:
#     if text.find(i)>-1:
#         print("Эти слова есть в тексте", text)
#     else: print('НЕТ')


# if isinstance(mes, list):
#     print("person является экземпляром класса object")
# else:
#     print("person не является экземпляром класса object")


# zzz = 'ost'

# if len(zzz[3:])>0:
#     print('zzz = ', zzz)


import pickle
data = {
     'a': [1, 2.0, 3, 4+6j],
     'b': ("character string", b"byte string"),
     'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
     pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
     data_new = pickle.load(f)
    

print(data_new)
print(type(data_new))