import pygame
import os


pygame.font.init()


WIN_WIDTH = 500
WIN_HEIGHT = 800


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


OPTIONS_FONT = pygame.font.SysFont("comicsans", 50)




BIRDS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
TITLE_IMG = pygame.image.load(os.path.join('imgs', 'title.png'))

SELECT_IMG = pygame.image.load(os.path.join('imgs', 'select.png'))
RESET_IMG = pygame.image.load(os.path.join('imgs', 'reset.png'))
BACK_IMG = pygame.image.load(os.path.join('imgs', 'back.png'))


pygame.display.set_caption("Flappy Bird - Options")
pygame.display.set_icon(BIRDS_IMG)


def draw_options_window_reset_hiscore(win, hiscore):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2 + 50))
    win.blit(RESET_IMG, (WIN_WIDTH/2 - RESET_IMG.get_width()/2, WIN_HEIGHT/2 - RESET_IMG.get_height()/2 + 50))
    win.blit(BACK_IMG, (WIN_WIDTH/2 - BACK_IMG.get_width()/2, WIN_HEIGHT/2 - BACK_IMG.get_height()/2 + 200))
    
    hiscore_text = OPTIONS_FONT.render("High Score: " + str(int(hiscore)), 1, BLACK)
    win.blit(hiscore_text, (WIN_WIDTH/2 - 170, WIN_HEIGHT/2 - 100))

    pygame.display.update()



def draw_options_window_back(win, hiscore):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))
    win.blit(RESET_IMG, (WIN_WIDTH/2 - RESET_IMG.get_width()/2, WIN_HEIGHT/2 - RESET_IMG.get_height()/2 + 50))
    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2 + 200))
    win.blit(BACK_IMG, (WIN_WIDTH/2 - BACK_IMG.get_width()/2, WIN_HEIGHT/2 - BACK_IMG.get_height()/2   + 200))

    
    hiscore_text = OPTIONS_FONT.render("High Score: " + str(int(hiscore)), 1, BLACK)
    win.blit(hiscore_text, (WIN_WIDTH/2 - 170, WIN_HEIGHT/2 - 100))

    pygame.display.update()



def options():
     win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
     clock = pygame.time.Clock()


     run_reset_hiscore = True
     while run_reset_hiscore:############################### Reset Hiscore
        clock.tick(30)

        with open("hiscore.txt","r") as f:
            hiscore = f.read()

        draw_options_window_reset_hiscore(win, hiscore)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: ################### Action of Reset High Score

                     h_score = int(hiscore)
                     h_score = 0
                
                     with open("hiscore.txt", "w") as f:
                        f.write(str(h_score))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN  or  event.key == pygame.K_s:

                    run_back = True
                    while run_back:################################################## Back
                        clock.tick(30)

                        draw_options_window_back(win, hiscore)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    #run_back = False
                                    #run_reset_hiscore = False
                                    return

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                    run_back = False    


#options()