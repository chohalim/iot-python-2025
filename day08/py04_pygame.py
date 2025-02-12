# py04_pygame.py

import pygame 
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION # 누르고, 떼고, 움직임
import sys 

pygame.init()
Surface = pygame.display.set_mode((640, 400)) 
FPSCLOK = pygame.time.Clock() 
pygame.display.set_caption('Pygame Mouse')

def main():
    pos = [] 
    check = mousebotton = False
    while True:
        Surface.fill((0, 0, 0)) 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == MOUSEBUTTONDOWN:
                # pos.append(event.pos)
                check = True
                mousebotton = True
            elif event.type == MOUSEMOTION:
                if mousebotton: pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousebotton = False
                check = False
                pos.clear()

        # for mpos in pos:
            # pygame.draw.circle(Surface,'white', mpos, 5)
        if check:
            if len(pos) > 1:
                pygame.draw.lines(Surface, 'white', False, pos)


        pygame.display.update() 
        FPSCLOK.tick(30)

if __name__ == '__main__':
    main()