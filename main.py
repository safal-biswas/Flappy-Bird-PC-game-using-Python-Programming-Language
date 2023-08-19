from lib2to3 import pygram
from flappybird import game
from credit import credit
from options import options

import pygame
import os

pygame.font.init()


WIN_WIDTH = 500
WIN_HEIGHT = 800


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



SCORE_FONT = pygame.font.SysFont("comicsans", 30)



BIRDS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
TITLE_IMG = pygame.image.load(os.path.join('imgs', 'title.png'))

PLAY_IMG = pygame.image.load(os.path.join('imgs', 'play.png'))
OPTIONS_IMG = pygame.image.load(os.path.join('imgs', 'options.png'))
CREDIT_IMG = pygame.image.load(os.path.join('imgs', 'credit.png'))
EXIT_IMG = pygame.image.load(os.path.join('imgs', 'exit.png'))

SELECT_IMG = pygame.image.load(os.path.join('imgs', 'select.png'))





pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(BIRDS_IMG)







MENU_STRING = 250







def draw_window_play(win):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, MENU_STRING))
    win.blit(PLAY_IMG, (WIN_WIDTH/2 - PLAY_IMG.get_width()/2, MENU_STRING))
    win.blit(OPTIONS_IMG, (WIN_WIDTH/2 - OPTIONS_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + 20))
    win.blit(CREDIT_IMG, (WIN_WIDTH/2 - CREDIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + OPTIONS_IMG.get_height() + 45))
    win.blit(EXIT_IMG, (WIN_WIDTH/2 - EXIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() +  OPTIONS_IMG.get_height() +  CREDIT_IMG.get_height() + 75))

    pygame.display.update()



def draw_window_options(win):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(PLAY_IMG, (WIN_WIDTH/2 - PLAY_IMG.get_width()/2, MENU_STRING))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + 20))
    win.blit(OPTIONS_IMG, (WIN_WIDTH/2 - OPTIONS_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + 20))
    win.blit(CREDIT_IMG, (WIN_WIDTH/2 - CREDIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + OPTIONS_IMG.get_height() + 45))
    win.blit(EXIT_IMG, (WIN_WIDTH/2 - EXIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() +  OPTIONS_IMG.get_height() +  CREDIT_IMG.get_height() + 75))
    
    pygame.display.update()


def draw_window_credit(win):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(PLAY_IMG, (WIN_WIDTH/2 - PLAY_IMG.get_width()/2, MENU_STRING))
    win.blit(OPTIONS_IMG, (WIN_WIDTH/2 - OPTIONS_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + 20))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + OPTIONS_IMG.get_height() + 45))
    win.blit(CREDIT_IMG, (WIN_WIDTH/2 - CREDIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + OPTIONS_IMG.get_height() + 45))
    win.blit(EXIT_IMG, (WIN_WIDTH/2 - EXIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() +  OPTIONS_IMG.get_height() +  CREDIT_IMG.get_height() + 75))
    
    pygame.display.update()


def draw_window_exit(win):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(PLAY_IMG, (WIN_WIDTH/2 - PLAY_IMG.get_width()/2, MENU_STRING))
    win.blit(OPTIONS_IMG, (WIN_WIDTH/2 - OPTIONS_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + 20))
    win.blit(CREDIT_IMG, (WIN_WIDTH/2 - CREDIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() + OPTIONS_IMG.get_height() + 45))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() +  OPTIONS_IMG.get_height() +  CREDIT_IMG.get_height() + 75))
    win.blit(EXIT_IMG, (WIN_WIDTH/2 - EXIT_IMG.get_width()/2, MENU_STRING + PLAY_IMG.get_height() +  OPTIONS_IMG.get_height() +  CREDIT_IMG.get_height() + 75))
    
    pygame.display.update()



def exit():
    pygame.quit





def menu ():

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()


    run_play = True
    while run_play:############################################################### Play

        clock.tick(30)
        draw_window_play(win)


        #with open("hiscore.txt","r") as f:
        #    hiscore = f.read()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_play = False
                pygame.quit()
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN  or  event.key == pygame.K_s:
                    
                    run_options = True
                    while run_options:########################################################## Options
                        clock.tick(30)
                        draw_window_options(win)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    options()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                    run_options = False


                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DOWN  or  event.key == pygame.K_s:

                                     run_credit = True
                                     while run_credit:######################################################## Credit
                                        clock.tick(30)
                                        draw_window_credit(win)
                        
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_SPACE:
                                                    credit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                                    run_credit = False


                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_DOWN  or  event.key == pygame.K_s:

                                                    run_exit = True
                                                    while run_exit:############################################################### Exit
                                                        clock.tick(30)
                                                        draw_window_exit(win)
                        
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.QUIT:
                                                                pygame.quit()

                                                            if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_SPACE:
                                                                    pygame.quit()

                                                            if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                                                    run_exit = False

            
                    




menu()