import pygame
import sys
import words
import canvas_mod
import time

clock = pygame.time.Clock()
dirty = True # нужно обновлять список

word4 = words.getWords() # получим новый список
print(': : : : : word4', word4)
# startNewGame = word4[1] 

canvas_mod.setPlace(word4[0]) # отрисуем

# Прошли уровень, сообщаем , пердлагаем играть дальше
def next(res):
    if not res:
        return False
    # print(':::: КОНЕЦ ::::: ', res)
    # print(' > > > word4[1]', word4[1])
    report = words.backAfterFinish(res)
    canvas_mod.showReport(report)    
    word5 = words.getWords() # получим новый список
    pygame.display.flip()
    time.sleep(1)
    # print(': : : : : word5', word5)
    canvas_mod.clearScreen()
    canvas_mod.setPlace(word5[0]) # отрисуем


while True:
    for event in pygame.event.get():
        # print ("Hello", event.type) 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print("Позиция мыши: ", event.pos)
                next(canvas_mod.collizia(event.pos))
            dirty = True 
      
    
    if dirty:
        dirty = False
        pygame.display.flip()

clock.tick(5)
    



