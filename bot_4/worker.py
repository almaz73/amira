import utils.saveRead as saveRead
import utils.wb_analiz as wb_analiz

# def getTaskId():    
#     taskId = wb_analiz.startOst()
#     saveRead.save(taskId)
#     print('Создан новый файл анализа')
#     return 'Создан новый файл анализа'
    

# def getAnaliz(txt):
#     taskId = saveRead.read()
#     if taskId:
#         print('БУДУ анализировать')
#         wb_analiz.getOst(taskId, txt)        
#     else: 
#         print('БУДУ создавать новый Файл анализа')
#         getTaskId()
#         return 'Создан новый файл отчета.'        
        
# wb_analiz.getAnaliz('463')
# zzz = saveRead.readFile()
# print('zzz=', zzz)

ans = wb_analiz.getAnaliz('')
print(ans)

  
# data = {
#      'a': [1, 2.0, 3, 4+6j],
#      'b': ("character string", b"byte string"),
#      'c': {None, True, False}
# }
# saveRead.saveFile(data)
# saveRead.saveFile('')
# zzz = saveRead.readFile()
# print('zzz=', zzz)