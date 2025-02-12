# py02_pygame.py
# PyGame 그래픽표현(선, 사각형, 원 ...)
import pygame 
from pygame.locals import QUIT 
from pygame.draw import *
import pygame.image as image

import sys 

pygame.init()
Surface = pygame.display.set_mode((600, 400)) 
FPSCLOK = pygame.time.Clock() 
pygame.display.set_caption('Pygame Graphic')

def main():

    myfont = pygame.font.SysFont('NanumGotic', 50)
    
    while True:
        Surface.fill((0, 0, 0)) 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 

        
        # 화면 표현 start_pos=(x, y)
        for x in range(10,400,10):
            line(Surface, 'white', (x,0), (x,400))
        for x in range(10,400,10):
            line(Surface, 'white', (0, y), (400, y))
        
        # 선 화면 표현, start_pos = (x, y) -> 화면 표현은 항상 for문 - update 사이 넣기
        pygame.draw.line(Surface, color=(255,0,0), start_pos=(30,30), end_pos=(150, 30), width=3) # 빨간 선이 그어짐 왼쪽상단이(0,0) # width=3 선이 두꺼워짐
        line(Surface, (0,255,0), (30,60), (150,60), 5)
        line(Surface, (0,0,255), (30,90), (150,150), 7)
        
        # 사각형
        pygame.draw.rect(Surface, color ='white', rect=(200,30,50,50)) 
        rect(Surface, (255,0,0), (260,30,100,50,),4) # (x, y, 넓이, 높이), 두께

        # 원(중심을 시작점으로)
        pygame.draw.rect(Surface, color=(255, 255, 0), center=(40, 180), radius=10)
        circle(Surface, (255,255,255), (80,180), 20) # 마지막 원의 반지름
        circle(Surface, (255,112,20), (280,160), 30, 10)

        # 타원
        pygame.draw.ellipse(Surface, color=(255,255,255), rect=(280,180,100,50))
        ellipse(Surface, (255,255,255), (280,300,100,50), 10)

        # polygon 다각형(별..)

        # 이미지 flaticon.com

        pygame.display.update() 
        FPSCLOK.tick(30)


if __name__ == '__main__':
    main()
