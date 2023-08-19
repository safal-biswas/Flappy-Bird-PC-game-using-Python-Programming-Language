# _**Project: Flappy Bird**_

## _**Language & IDE**_

1. Python Programming language (including pygame library).
2. Visual Studio Code.

<br><br>

## _**Classes**_
<br>
In 'flappybird.py' file, a window is created with dimension 500*800 & import all images with that is used in the game,

```
WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))), 
              pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))), 
              pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

```
<br><br>
In Bird class the parameters of the birds are

```
IMGS = BIRDS_IMGS            # Store the images of the bird
MAX_ROTATION = 25            # To determine how much the bird will rotate
ROT_VEL = 20                 # To determine how fast the rotation occur
ANIMATION_TIME = 5

def __init__(self, x, y):    # for the position of the bird
def jump(self):              # for the jump when 'Space' is pressed
def move(self):              # for general movement of bird
def draw(self, win):         # for draw the bird in the screen
def get_mask(self):          # for masking the bird to operate accurate colision

```

<br><br>
In Pipe class the parameters of the birds are

```
GAP = 235                    # To determine the gap between upper & lower pipe
VEL = 5                      # To detrmine how fast the pipe will move

def __init__(self, x):       # for the position of the pipe
def set_height(self):        # for generate pipe at the random height
def move(self):              # for general movement from right to left of pipe
def draw(self, win):         # for draw the pipe in the screen
def collide(self, bird):     # for colision of bird_mask & pipe_mask

```
<br><br>
Base & BG(Background) class contain same parameters

```
VEL = 5                            # To determine how fast the Base or BG will move
WIDTH = BASE_IMG.get_width()       # To find the width of Base or BG image
IMG = BASE_IMG

def __init__(self, y):
def move(self):
def draw(self, win):

```

<br><br>

## _**game function**_
<br>


The game will start like this after 3 second of counting,
<br>
<img src="start.png" style="width:200px;">

<br><br>
While playing the game, 'Space' key will make the jump to the bird & 'W' key will pause the game
```
if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

            #if key_pressed[pygame.K_SPACE]:
                #bird.jump()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w  or event.key == pygame.K_ESCAPE:

                    draw_window(win, bird, pipes, base, bg, score, hiscore)

                    paused = not paused
                    while paused:
                        clock.tick(30)

                        draw_pausing_continue(win)

```


<br><br>

### _**Pause:**_
<br>
"draw_pausing_continue(win)" function will print a screen. Where we can choose between 2 options with arrow keys & 'space' to proceed.

<br>

* Continue = To continue the game.
* Quit = To quit the game.


<img src="pause.png" style="width:200px;">


<br><br>

### _**Score & High Score:**_
<br>

* Each time the bird cross a pipe, the score will be increased by one.
* When score is greater than high score, it will be written on the "hiscore.txt" file. Then both score & highscore will be increased simultaneously.

```
if add_pipe:
    score += 1
    pipes.append(Pipe(600))

    h_score = int(hiscore)

    if score > h_score:
        h_score = score
                
        with open("hiscore.txt", "w") as f:
            f.write(str(h_score))

```





<br><br>

### _**Game Over:**_

<br>
If the bird collide with pipe, the will be over.

```
if pipe.collide(bird):
                
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
```
<br>


"draw_boom_restart(win)" function will print a screen. Where we can choose between 2 options with arrow keys & 'space' to proceed.

<br>

* Restart = To start a new game.
* Quit = To quit the game.


<img src="over.png" style="width:200px;">
