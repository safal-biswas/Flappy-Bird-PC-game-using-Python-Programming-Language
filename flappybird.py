import pygame
import os
import random




from pygame.time import Clock
pygame.font.init()


WIN_WIDTH = 500
WIN_HEIGHT = 800


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)



SCORE_FONT = pygame.font.SysFont("comicsans", 30)
DEAD_FONT = pygame.font.SysFont("comicsans", 50)
BOOM_FONT = pygame.font.SysFont("comicsans", 100)
NOTE_FONT = pygame.font.SysFont("comicsans", 30)


BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))), 
              pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))), 
              pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))


PAUSED_IMG = pygame.image.load(os.path.join('imgs', 'paused.png'))
BOOM_IMG = pygame.image.load(os.path.join('imgs', 'boom.png'))
NUM3_IMG = pygame.image.load(os.path.join('imgs', '3.png'))
NUM2_IMG = pygame.image.load(os.path.join('imgs', '2.png'))
NUM1_IMG = pygame.image.load(os.path.join('imgs', '1.png'))
START_IMG = pygame.image.load(os.path.join('imgs', 'start.png'))

SELECT_IMG = pygame.image.load(os.path.join('imgs', 'select.png'))

CONTINUE_IMG = pygame.image.load(os.path.join('imgs', 'continue.png'))
QUIT_IMG = pygame.image.load(os.path.join('imgs', 'quit.png'))
RESTART_IMG = pygame.image.load(os.path.join('imgs', 'restart.png'))



pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(BIRDS_IMGS[1])























class Bird:
    IMGS = BIRDS_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]


    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y


    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL


    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)


    def get_mask(self):
        return pygame.mask.from_surface(self.img)

























class Pipe:
    GAP = 235
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()


    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP


    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))


    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True

        return False






















class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG


    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH


    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH


    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
















class BG:
    VEL = 1
    WIDTH = BG_IMG.get_width()
    IMG = BG_IMG


    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH


    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH


    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
















def draw_boom_restart(win):

    win.blit(BOOM_IMG, (WIN_WIDTH/2 - BOOM_IMG.get_width()/2, WIN_HEIGHT/2 - BOOM_IMG.get_height()/2))

    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2  + 100 ))
    win.blit(RESTART_IMG, (WIN_WIDTH/2 - RESTART_IMG.get_width()/2, WIN_HEIGHT/2 - RESTART_IMG.get_height()/2  + 100 ))

    win.blit(QUIT_IMG, (WIN_WIDTH/2 - QUIT_IMG.get_width()/2, WIN_HEIGHT/2 - QUIT_IMG.get_height()/2  + 200 ))
    
    pygame.display.update()




def draw_boom_quit(win):

    win.blit(BOOM_IMG, (WIN_WIDTH/2 - BOOM_IMG.get_width()/2, WIN_HEIGHT/2 - BOOM_IMG.get_height()/2))

    win.blit(RESTART_IMG, (WIN_WIDTH/2 - RESTART_IMG.get_width()/2, WIN_HEIGHT/2 - RESTART_IMG.get_height()/2  + 100 ))

    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2  + 200 ))
    win.blit(QUIT_IMG, (WIN_WIDTH/2 - QUIT_IMG.get_width()/2, WIN_HEIGHT/2 - QUIT_IMG.get_height()/2  + 200 ))
    
    pygame.display.update()















def draw_pausing_continue(win):

    win.blit(PAUSED_IMG, (WIN_WIDTH/2 - PAUSED_IMG.get_width()/2, WIN_HEIGHT/2 - PAUSED_IMG.get_height()/2))

    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2  + 100 ))
    win.blit(CONTINUE_IMG, (WIN_WIDTH/2 - CONTINUE_IMG.get_width()/2, WIN_HEIGHT/2 - CONTINUE_IMG.get_height()/2  + 100 ))

    win.blit(QUIT_IMG, (WIN_WIDTH/2 - QUIT_IMG.get_width()/2, WIN_HEIGHT/2 - QUIT_IMG.get_height()/2  + 200 ))

    pygame.display.update()


def draw_pausing_quit(win):

    win.blit(PAUSED_IMG, (WIN_WIDTH/2 - PAUSED_IMG.get_width()/2, WIN_HEIGHT/2 - PAUSED_IMG.get_height()/2))

    win.blit(CONTINUE_IMG, (WIN_WIDTH/2 - CONTINUE_IMG.get_width()/2, WIN_HEIGHT/2 - CONTINUE_IMG.get_height()/2  + 100 ))

    win.blit(SELECT_IMG, (WIN_WIDTH/2 - SELECT_IMG.get_width()/2, WIN_HEIGHT/2 - SELECT_IMG.get_height()/2  + 200 ))
    win.blit(QUIT_IMG, (WIN_WIDTH/2 - QUIT_IMG.get_width()/2, WIN_HEIGHT/2 - QUIT_IMG.get_height()/2  + 200 ))

    pygame.display.update()













def draw_window(win, bird, pipes, base, bg, score, hiscore):
    bg.draw(win)

    for pipe in pipes:
        pipe.draw(win)

    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    win.blit(score_text, (WIN_WIDTH - 50 - score_text.get_width(), 10))

    hiscore_text = SCORE_FONT.render("Best: " + str(int(hiscore)), 1, WHITE)
    win.blit(hiscore_text, (10, 10))

    base.draw(win)
    bird.draw(win)

    pygame.display.update()
























def game ():
    bird = Bird(230, 350)
    base = Base(730)
    bg = BG(0)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()

    score = 0
    count=0





    run = True
    paused = False
    while run:

        clock.tick(30)



        with open("hiscore.txt","r") as f:
            hiscore = f.read()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

            #if key_pressed[pygame.K_SPACE]:
                #bird.jump()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w  or event.key == pygame.K_ESCAPE:

                    draw_window(win, bird, pipes, base, bg, score, hiscore)

                    paused = not paused
                    while paused:################################################ Continue
                        clock.tick(30)

                        draw_pausing_continue(win)


                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                pygame.quit()


                            if event.type == pygame.KEYDOWN:
                                 if event.key == pygame.K_w or event.key == pygame.K_ESCAPE  or event.key == pygame.K_SPACE:
                                    paused = not paused

                                    pygame.time.delay(500)

                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                    win.blit(NUM3_IMG, (WIN_WIDTH/2 - NUM3_IMG.get_width()/2, WIN_HEIGHT/2 - NUM3_IMG.get_height()/2     + 45 ))
                                    pygame.display.update()
                                    pygame.time.delay(1000)



                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                    win.blit(NUM2_IMG, (WIN_WIDTH/2 - NUM2_IMG.get_width()/2, WIN_HEIGHT/2 - NUM2_IMG.get_height()/2     + 45 ))
                                    pygame.display.update()
                                    pygame.time.delay(1000)



                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                    win.blit(NUM1_IMG, (WIN_WIDTH/2 - NUM1_IMG.get_width()/2, WIN_HEIGHT/2 - NUM1_IMG.get_height()/2     + 45 ))
                                    pygame.display.update()
                                    pygame.time.delay(1000)



                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                    win.blit(START_IMG, (WIN_WIDTH/2 - START_IMG.get_width()/2, WIN_HEIGHT/2 - START_IMG.get_height()/2     + 25  ))
                                    pygame.display.update()
                                    pygame.time.delay(1000)

                                    draw_window(win, bird, pipes, base, bg, score, hiscore)


                            if event.type == pygame.KEYDOWN:
                                 if event.key == pygame.K_DOWN or event.key == pygame.K_s:

                                    draw_window(win, bird, pipes, base, bg, score, hiscore)

                                    run_quit = True
                                    while run_quit:############################################################### Quit
                                        clock.tick(30)

                                        draw_pausing_quit(win)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_SPACE:
                                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                                    return

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                                    draw_window(win, bird, pipes, base, bg, score, hiscore)
                                                    run_quit = False


        bird.move()
        
        
        
        
        





        
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                
                not_again = True

                while not_again:################################## Restart
                    clock.tick(30)
                    draw_boom_restart(win)

                    pygame.time.delay(1500)

                    win.blit(BG_IMG, (0,0))
                    draw_boom_restart(win)
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            run = False
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                run = False  
                                game()


                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                
                                win.blit(BG_IMG, (0,0))

                                run_quit = True
                                while run_quit:############################################################### Quit
                                        clock.tick(30)

                                        draw_boom_quit(win)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_SPACE:
                                                    return

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                                    win.blit(BG_IMG, (0,0))
                                                    run_quit = False


                        

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()


        if add_pipe:
            score += 1
            pipes.append(Pipe(600))

            h_score = int(hiscore)

            if score > h_score:
                h_score = score
                
                with open("hiscore.txt", "w") as f:
                    f.write(str(h_score))
                    


        for r in rem:
            pipes.remove(r)



        if bird.y + bird.img.get_height() >= 730 or bird.y <= -200:
            not_again = True

            while not_again:
                clock.tick(30)

                draw_boom_restart(win)

                pygame.time.delay(1500)

                win.blit(BG_IMG, (0,0))
                draw_boom_restart(win)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            run = False
                            game()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:

                                win.blit(BG_IMG, (0,0))
                                
                                run_quit = True
                                while run_quit:############################################################### Quit
                                        clock.tick(30)

                                        draw_boom_quit(win)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_SPACE:
                                                    return

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_UP  or  event.key == pygame.K_w:
                                                    win.blit(BG_IMG, (0,0))
                                                    run_quit = False  
                            
                    






        base.move()
        bg.move()

        draw_window(win, bird, pipes, base, bg, score, hiscore)

        if count== 0:
            win.blit(NUM3_IMG, (WIN_WIDTH/2 - NUM3_IMG.get_width()/2, WIN_HEIGHT/2 - NUM3_IMG.get_height()/2     + 45 ))
            pygame.display.update()
            pygame.time.delay(1000)



            draw_window(win, bird, pipes, base, bg, score, hiscore)
            win.blit(NUM2_IMG, (WIN_WIDTH/2 - NUM2_IMG.get_width()/2, WIN_HEIGHT/2 - NUM2_IMG.get_height()/2     + 45 ))
            pygame.display.update()
            pygame.time.delay(1000)



            draw_window(win, bird, pipes, base, bg, score, hiscore)
            win.blit(NUM1_IMG, (WIN_WIDTH/2 - NUM1_IMG.get_width()/2, WIN_HEIGHT/2 - NUM1_IMG.get_height()/2     + 45 ))
            pygame.display.update()
            pygame.time.delay(1000)



            draw_window(win, bird, pipes, base, bg, score, hiscore)
            win.blit(START_IMG, (WIN_WIDTH/2 - START_IMG.get_width()/2, WIN_HEIGHT/2 - START_IMG.get_height()/2     + 25  ))
            pygame.display.update()
            pygame.time.delay(1000)

            draw_window(win, bird, pipes, base, bg, score, hiscore)

            count += 1

    pygame.quit()
    quit()


#game()