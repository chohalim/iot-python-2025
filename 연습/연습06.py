import pygame 
from pygame.locals import QUIT 
from pygame.draw import *
import pygame.image as image

import sys 

# 기본변수
pygame.init()
Surface = pygame.display.set_mode((400, 400)) ## root.geometry('640x400)
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Graphic')

def main():
    # 이미지 로드
    snake = image.load('./image/snake.png')
    # 텍스트 변수
    myfont = pygame.font.SysFont('NanumGotic', 50)
    message1 = myfont.render('This is my message', True, (255,150,255)) # 안티알리싱-계단현상완화
    message2 = myfont.render('This is PyGame', False, (255,150,255)) 


    while True:
        Surface.fill(color='black')
        # Surface.fill((255, 255, 255)) # #FFFFFF = white. #0000000 / #00FFFFFF alpha 투명도
        for event in pygame.event.get(): # 키보드, 마우스 이벤트 체크
            if event.type == QUIT: # WM_DELETE_WINDOW
                pygame.quit()   # pygame을 종료
                sys.exit()      # 윈도우 앱 탈출
        
        # 화면
        for x in range(10, 400, 10):
            line(Surface, 'white', (x, 0), (x, 400))
        for y in range(10, 400, 10):
            line(Surface, 'white', (0, y), (400, y))

        pygame.draw.line(Surface, color=(255,0,0), start_pos=(30,30),end_pos=(150,30), width=3)
        line(Surface, (0,255,0),(30,60),(150,60),5)
        line(Surface, (0,0,255),(30,90),(150,150),7)

        pygame.draw.rect(Surface, color='white', rect=(200,30,50,50))
        # rect(Surface,(255,0,0), (260,30,100,50),3)

        Surface.blit(message1, (30,230))
        Surface.blit(message2, (30,280))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()




