import pygame
import sys
import words
import canvas_mod

clock = pygame.time.Clock()
dirty = True # нужно обновлять список

word4 = words.getWords() # получим новый список
canvas_mod.setPlace(word4) # отрисуем

while True:
    for event in pygame.event.get():
        # print ("Hello", event.type) 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print("Позиция мыши: ", event.pos)
                canvas_mod.collizia(event.pos)
            dirty = True 
      
    
    if dirty:
        # canvas_mod.setPlace(word4)
        dirty = False

    pygame.display.flip()
    clock.tick(5)
    
    #time.sleep(2)



