import pygame 
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, Rect
import sys 

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = 800

class Block:
    def __init__(self,col,rect,speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45)+90

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir))*self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))*self.speed

    def draw_E(self):
        pygame.draw.ellipse(Surface, self.col, self.rect)

    def draw_R(self):
        pygame.draw.rect(Surface, self.col, self.rect)

pygame.init()
Surface = pygame.display.set_mode((1000, 800)) 
FPSCLOK = pygame.time.Clock()
pygame.display.set_caption('Pygame Event')
pygame.key.set_repeat(10,10)

def main():
    is_game_start = False
    score = 0
    BLOCK = []
    BALL = Block((200,200,0),Rect(375,650,20,20),10)
    PADDLE = Block((200,200,0), Rect(375,700,100,30))

    colors = [(255,0,0),(255,150,0),(255,228,0),
              (11,201,4),(0,80,255),(0,0,147),
              (201,0,167)]
    
    for y, color in enumerate(colors, start=0):
        for x in range(0,9):
            BLOCK.append(Block(color, Rect(x*80+150, y*40+40, 60, 20)))

    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR!', True,'yellow')
    M_FAIL = bigFont.render('FAILED!!', True, 'red')

    while True:
        M_SCORE = smallFont.render(f'SCORE: {score}', True, 'White')
        M_SPEED = smallFont.render(f'SPEED: {BALL.speed}', True, 'White')
        Surface.fill((0,0,0))
        for event in pygame.event.get():
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
                    is_game_start = True 

        if is_game_start == False:
            Surface.blit(M_GAME_TITLE,((SCREEN_WIDTH/2)-(400/2),
                                       (SCREEN_HEIGTH/2)-(50/2)))
            Surface.blit(M_GAME_SUBTITLE,((SCREEN_WIDTH/2)-(300/2),
                                          (SCREEN_HEIGTH/2)+50))
        else:
            Surface.blit(M_SCORE, (10,770))
            Surface.blit(M_SPEED, (SCREEN_WIDTH - 220, 770))

            LenBlock = len(BLOCK)
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock:
                BALL.dir *= -1
                BALL.speed += 0.25
                score += 10
                
            if BALL.rect.centery < 1000:
                BALL.move()

            if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000:
                BALL.dir = 180 - BALL.dir
            elif BALL.rect.centery < 0:
                BALL.dir = - BALL.dir

            BALL.draw_E()
            PADDLE.draw_R()

            for i in BLOCK:
                i.draw_R()

        pygame.display.update()
        FPSCLOK.tick(30)

if __name__ == '__main__':
    main()