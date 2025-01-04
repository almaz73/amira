import pygame
import sys
import time
import words
import text_1

pygame.init()
pygame.display.set_caption('Моя Первая Игра на питоне')  # заголовок
img = pygame.image.load('pyGame/icon.png')  # рисунок иконки
pygame.display.set_icon(img)  # закрепляем иконку
screen = pygame.display.set_mode((800, 500))  # размеры игрового поля
font = pygame.font.SysFont('comicsansms', 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
follow = font.render('Найди пару', 1, RED, GREEN)
like = font.render('Ставь лайк', 1, GREEN, BLUE)

r = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

print('- - - - -', text_1.text.split('\n')[0])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(follow, (300,20))
    screen.blit(like, (100,100))
    pygame.display.flip()
    time.sleep(.5)



