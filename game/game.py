import pygame
import random
pygame.init()
#all game variables
res=screen_x, screen_y= 500, 750
screen=pygame.display.set_mode(res)
running=True
fps=60
waiting=True
clock=pygame.time.Clock()
#rock
rock=pygame.image.load('images/rock1.png')
rock_x=50
rock_y=325
y_change=0
def show_rock(x,y):
    screen.blit(rock,(x, y))
#obstacles
obstacle=pygame.image.load('images/spike.png')
obstacle_bottom=pygame.transform.flip(obstacle, False, True)
obstacle_gap=120
obstacle_y=random.randrange(150,651)
obstacle_x=500
def show_obstacle(x,y):
    screen.blit(obstacle, (250,(-1*(750+obstacle_gap)+(obstacle_y))))
    screen.blit(obstacle_bottom, (250, obstacle_y))
#background
bg= pygame.image.load('images/background.png')
#when the game starts
while running:
    clock.tick(fps)
    pygame.display.set_caption("Flappy Dwayne")
    screen.blit(bg, (0,0))
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                waiting=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    y_change=-9
                    rock= pygame.image.load('images/rock2.png')
                    rock=pygame.image.load('images/rock3.png')
                    waiting=False
        show_rock(rock_x, rock_y)
        pygame.display.update()
    y_change+=0.7
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                y_change=-9
                rock= pygame.image.load('images/rock2.png')
                rock=pygame.image.load('images/rock3.png')
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                rock=pygame.image.load('images/rock1.png')
    rock_y+=y_change
    if rock_y <=0:
        rock_y=0
    elif rock_y >= 700:
        rock_y=700
    show_rock(rock_x, rock_y)
    show_obstacle(obstacle_x, obstacle_y)
    pygame.display.update()
pygame.quit()
