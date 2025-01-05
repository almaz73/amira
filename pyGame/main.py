import pygame
import sys
import words


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Запоминаем 1000 часто используемых английских слов')  # заголовок
img = pygame.image.load('pyGame/icon.png')  # рисунок иконки
pygame.display.set_icon(img)  # закрепляем иконку
screen = pygame.display.set_mode((800, 500))  # размеры игрового поля
font = pygame.font.SysFont('comicsansms', 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
follow = font.render('Найди пару', 1, RED, GREEN)

screen.blit(follow, (300,20))




word4 = words.getWords()
print(word4)


# расставит 4 пары слов
def setPlace(words):
    eng=[]
    ru=[]
    print(len(words))
    for i in words:
        eng.append(font.render('    '+i[0]+'  ', 1, GREEN, BLUE))
        ru.append(font.render( i[1]+'  ', 1, GREEN, BLUE))
    for r in range(len(words)):
        screen.blit(eng[r], (350-eng[r].get_width(),100+r*60))
        screen.blit(ru[r], (420,100+r*60))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    setPlace(word4)
    pygame.display.flip()
    clock.tick(1)
    
    #time.sleep(2)



