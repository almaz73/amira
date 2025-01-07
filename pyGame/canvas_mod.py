# тут работа со сценой
import pygame
import random

pygame.init()
font = pygame.font.SysFont('comicsansms', 32)
screen = pygame.display.set_mode((800, 500))  # размеры игрового поля

clock = pygame.time.Clock()
pygame.display.set_caption('Запоминаем 1000 часто используемых английских слов')  # заголовок
img = pygame.image.load('pyGame/icon.png')  # рисунок иконки
pygame.display.set_icon(img)  # закрепляем иконку
follow = font.render('      Найди пару      ', 1, 'wheat', (0, 110, 0))
screen.blit(follow, (150,20))


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 100)

coor=[]  # координаты слов
eng=[]
ru=[]
ruRand = []  # случайн

# расставит 4 пары слов
def setPlace(words):
    global ruRand
    global eng
    global ru
    ruRand = list(range(len(words)))
    random.shuffle(ruRand)  # перемешиваем
    
    for i in words:
        eng.append(font.render('    '+i[0]+'  ', 1, GREEN, BLUE))
        ru.append(font.render( i[1]+'  ', 1, GREEN, BLUE))

    print(' >> >> >> eng', eng)


    for r in range(len(words)):
        point = {'x1':300-eng[r].get_width(), 
                 'w1': 300,
                 'x2':370, 
                 'w2': 370 + ru[r].get_width(),
                 'y1':100+r*60,
                 'y2':100+r*60}
        coor.append(point)
        screen.blit(eng[r], (point['x1'],point['y1']))
        screen.blit(ru[r], (point['x2'],point['y2']+(ruRand[r]-r)*60))
        # тут сохраним координаты слов, чтобы понять что нажато
    # print(coor)
    # print('eng= ',eng)
    # print('ru = ',ru)

oldCol=None
oldR = None
arrResults=[]


def isFinishLevel():
    isFull = False
    for a in eng:
        if a != None:
            isFull = True
    return isFull


arrTrue = []
arrFalse = []

def winner(bool):
    global arrResults       

    firstRow = arrResults[0]%10-1
    if bool:
        arrTrue.append(firstRow)  
    else:
        arrFalse.append(firstRow)   

    for el in arrResults:
        row = el%10-1
        col = el//10
        if col == 1:
            r = pygame.Rect(0, 100+row*60, 350, 50)
        else:
            r = pygame.Rect(350, 100+ruRand[row]*60, 580, 50)
        if bool:
            pygame.draw.rect(screen, 0, r)
            eng[row] = None
            ru[row] = None
        else:                    
            pygame.draw.rect(screen, 0, r, width=5)             

    arrResults = []
   
    

# выделяем нажатое слово
def highlight(place):
    if not place:
        return False
     
    global oldR
    global oldCol
    global arrResults 

    

    arrResults.append(place)      

    row = place%10-1
    col = place//10

    if col == oldCol and oldR:
        pygame.draw.rect(screen,0, oldR, width=5)
        print('HRHRH')
        oldR = None
        arrResults = [place]

    if not place:
        return False  
   
    print(' > > > > >>>row', row)
    r = None
    if col == 1 and eng[row]:
        x = eng[row].get_width()        
        r = pygame.Rect(300-x, 100+row*60, x, 50)
    elif ru[row]:
        x = ru[row].get_width()
        r = pygame.Rect(370, 100+ruRand[row]*60, x, 50)
        

    if r:
        pygame.draw.rect(screen, (100, 0, 0), r, width=5) 
    else :
        return False
    
    oldCol = col
    oldR = r 

    if len(arrResults)>1:
        return victoryCheck()
    

def victoryCheck():    
    winner(arrResults[0]%10 == arrResults[1]%10)
    if not isFinishLevel():
        # print(':::: victoryCheck arrTrue', arrTrue)
        # print(':::: victoryCheck arrFalse', arrFalse)
        global eng
        global ru
        global coor
        result = []
        coor=[]
        eng=[]
        ru=[]
        for i in arrTrue:
            if i not in arrFalse:
                result.append(i)
        return {'ready':result, 'repeat':arrFalse}


def collizia (pos):
    x, y = pos
    element = None
    count = 1
    
    for co in coor:
        if x>co['x1'] and x<co['w1'] and y>co['y1'] and y<co['y1']+60 :
            element = 10+count
        y2 = co['y2'] #+(ruRand[count-1]-count)*60
        if x>co['x2'] and x<co['w2'] and y>y2 and y<y2+60 :
            element = 20+int(ruRand.index(count-1)+1)
        count += 1
    print(element)
    return highlight(element)
    # return element

def clearScreen():
    r = pygame.Rect(0, 100, 780, 500)
    pygame.draw.rect(screen, 0, r)

def showReport(res):
    print ('res res res res res res res res res', res)   
    clearScreen()
    

    follow = font.render('      Отчет      ', 1, 'wheat', (0, 110, 0))
    screen.blit(follow, (150,120))    