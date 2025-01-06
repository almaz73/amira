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

coor=[]

# def randomization(len):
#     for i in range(len):

ruRand = []

# расставит 4 пары слов
def setPlace(words):
    eng=[]
    ru=[]
    global ruRand
    ruRand = list(range(len(words)))
    random.shuffle(ruRand)
    print('>>>> ruRand = ',ruRand)
    print('>>>> ruRand = ',ruRand[0])
    
    for i in words:
        eng.append(font.render('    '+i[0]+'  ', 1, GREEN, BLUE))
        ru.append(font.render( i[1]+'  ', 1, GREEN, BLUE))
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
    return element
         
    