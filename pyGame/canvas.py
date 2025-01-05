# тут работа со сценой
import pygame

screen = pygame.display.set_mode((800, 500))  # размеры игрового поля
font = pygame.font.SysFont('comicsansms', 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 100)
follow = font.render('      Найди пару      ', 1, 'wheat', (0, 110, 0))


# расставит 4 пары слов
def setPlace(words):
    eng=[]
    ru=[]
    # print(len(words))
    for i in words:
        eng.append(font.render('    '+i[0]+'  ', 1, GREEN, BLUE))
        ru.append(font.render( i[1]+'  ', 1, GREEN, BLUE))
    for r in range(len(words)):
        screen.blit(eng[r], (250-eng[r].get_width(),100+r*60))
        screen.blit(ru[r], (320,100+r*60))
        # тут сохраним координаты слов, чтобы понять что нажато