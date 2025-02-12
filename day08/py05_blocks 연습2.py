# py05_blocks.py
# 벽돌깨기 게임
import pygame 
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, Rect
import sys 

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = 800

class Block:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270 # 최소값 225~315 사이의 값

    def move(self): # 볼 무브
        # 볼의 움직이는 x축 값을 계속 계산하려면 x는 dir 값을 라디언으로 변환 후 코사인처리
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        # 볼의 움직이는 y축 값을 계속 계산하려면 y는 dir 값을 라디언으로 변환 후 사인처리
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_E(self): # 공을 circle이 아니라 ellipse로 생성
        pygame.draw.ellipse(Surface, self.col, self.rect)

    def draw_R(self):
        pygame.draw.rect(Surface, self.col, self.rect)

pygame.init()
Surface = pygame.display.set_mode((1000, 800)) 
FPSCLOK = pygame.time.Clock() 
pygame.display.set_caption('Pygame Blocks!!')
pygame.key.set_repeat(10,10)

def main():
    is_game_start = False
    score = 0
    BLOCK = []
    # 공만듦
    BALL = Block((200,200,0),Rect(375,650,20,20), 10) # 공 생성
    PADDLE = Block((200,200,0), Rect(375,700,100,30)) # 공을 맞출 패달을 생성
    
    # 클래스 생성
    # 무지개색 정보
    colors = [(255,0,0),(255,150,0),(255,228,0),
              (11,201,4),(0,80,255),(0,0,147),
              (201,0,167)]

    # 초기에 생성 될 블록들(무지개색으로 아홉개씩, 54개 블록)
    for y, color in enumerate(colors, start=0): # y값은 0~6
        for x in range(0,9):
            BLOCK.append(Block(color, Rect(x*80+150, y*40+40, 60, 20)))


    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR!', True, 'yellow')
    M_FAIL = bigFont.render('FAILED!!', True, 'red')



    while True:
        # 스코어, 스피드 글자 들어갈 자리
        Surface.fill((0, 0, 0)) 
        for event in pygame.event.get(): # 이벤트 처리 기본
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if PADDLE.rect.centerx < 55:
                        PADDLE.rect.centerx = 55
                    else:
                        PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    if PADDLE.rect.centerx > 945: 
                        PADDLE.rect.centerx = 945
                    else:
                        PADDLE.rect.centerx += 10
                elif event.key == K_SPACE:
                    is_game_start = True # 게임시작

        # 게임화면 렌더링
        if is_game_start == False:
            Surface.blit(M_GAME_TITLE,((SCREEN_WIDTH/2)-(400/2),
                                       (SCREEN_HEIGTH/2)-(50/2)))
            Surface.blit(M_GAME_SUBTITLE,((SCREEN_WIDTH/2)-(300/2),
                                       (SCREEN_HEIGTH/2)+50))
        else: # 게임시작 후 블록, 볼이 움직이게 처리, 바도 움직이도록
            LenBlock = len(BLOCK) # 54개로 시작하지만 공에 충돌 시 갯수가 줄어들도록
            # Collision Detection(충돌체크)
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock: # 공에 블록에 맞아서 갯수가 맞지 않음
                BALL.dir *= -1 # 공의 방향이 바뀜


            if BALL.rect.centery < 1000:
                BALL.move()

            if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000: # 게임화면 양쪽 벽 밖으로 못나가게
                BALL.dir = 180 - BALL.dir # 반사각만큼 방향 전환
            elif BALL.rect.centery < 0: # 게임화면 천장에 부딪히면 반사
                BALL.dir = - BALL.dir 

            BALL.draw_E() # 볼그리기
            PADDLE.draw_R() # 바그리기

            for i in BLOCK: # Block()
                i.draw_R()


        pygame.display.update() 
        FPSCLOK.tick(30)

if __name__ == '__main__':
    main()
