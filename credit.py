import pygame
import os


pygame.font.init()


WIN_WIDTH = 500
WIN_HEIGHT = 800


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


CREDIT_FONT_l = pygame.font.SysFont("comicsans", 30)
CREDIT_FONT = pygame.font.SysFont("comicsans", 25)
CREDIT_FONT_s = pygame.font.SysFont("comicsans", 20)



BIRDS_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
TITLE_IMG = pygame.image.load(os.path.join('imgs', 'title.png'))

SELECT_IMG = pygame.image.load(os.path.join('imgs', 'select.png'))
BACK_IMG = pygame.image.load(os.path.join('imgs', 'back.png'))


pygame.display.set_caption("Flappy Bird - Credit")
pygame.display.set_icon(BIRDS_IMG)




def draw_credit_window(win):
    win.blit(BG_IMG, (0,0))
    win.blit(TITLE_IMG, (WIN_WIDTH/2 - TITLE_IMG.get_width()/2, 20))

    credit_text = CREDIT_FONT_l.render("This Game is Developed By,", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   - 180))
    
    credit_text = CREDIT_FONT.render("Safal Kumar Biswas", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   - 100))
    
    credit_text = CREDIT_FONT_s.render("Department of Electrical & Computer Engneering,", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   - 50))
    
    credit_text = CREDIT_FONT_s.render("RUET", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   - 20))
    
    credit_text = CREDIT_FONT_s.render("Roll: 1810056", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   + 20))
    
    credit_text = CREDIT_FONT_s.render("Contact: safalbiswas005@gmail.com", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   + 60))
    
    credit_text = CREDIT_FONT_s.render("...Happy Playing...", 1, BLACK)
    win.blit(credit_text, (WIN_WIDTH/2 - credit_text.get_width()/2, WIN_HEIGHT/2 - credit_text.get_height()/2   + 120))
    

    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2      + 200))
    
    win.blit(BACK_IMG, (WIN_WIDTH/2 - BACK_IMG.get_width()/2, WIN_HEIGHT/2 - BACK_IMG.get_height()/2   + 200))
    

    pygame.display.update()




def credit():

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()


    run = True
    while run:

        clock.tick(30)


        draw_credit_window(win)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    return



#credit()