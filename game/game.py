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
last_tick=pygame.time.get_ticks()
#rock
rock=pygame.image.load('images/rock1.png')
rock_x=50
rock_y=325
y_change=0
def show_rock(x,y):
    screen.blit(rock,(x, y))
#obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self) # to inherit the pygame.sprite class
        self.image=pygame.image.load('images/spike.png')
        self.rect=self.image.get_rect()
        if position==1:
            self.image=pygame.transform.flip(self.image , False, True)
            self.rect.topleft=[x,y]
        elif position==-1:
            self.rect.topleft=[x,y]
    def update(self):
        self.rect.x-=3
obstacle_group=pygame.sprite.Group()
obstacle_gap=75
starting_position_obstacle_x=500
obstacle_frequency=1500 #miliseconds
#background
bg= pygame.image.load('images/background.png')
#when the game starts
while running:
    clock.tick(fps)
    pygame.display.set_caption("Flappy Dwayne 🗿")
    screen.blit(bg, (0,0))
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                waiting=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    y_change=-9
                    pygame.mixer.music.load("sound/rock_flap.mp3")
                    pygame.mixer.music.play()
                    rock= pygame.image.load('images/rock2.png')
                    rock=pygame.image.load('images/rock3.png')
                    waiting=False
        show_rock(rock_x, rock_y)
        pygame.display.update()
    y_change+=0.65
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                y_change=-9
                rock= pygame.image.load('images/rock2.png')
                rock=pygame.image.load('images/rock3.png')
                pygame.mixer.music.load("sound/rock_flap.mp3")
                pygame.mixer.music.play()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                rock=pygame.image.load('images/rock1.png')
    rock_y+=y_change
    if rock_y <=0:
        rock_y=0
    elif rock_y >= 700:
        rock_y=700
    present_time=pygame.time.get_ticks()
    if present_time-last_tick>obstacle_frequency:
        obstacle_y_top=random.randrange(190,651) 
        obstacle_bottom=Obstacle(starting_position_obstacle_x, obstacle_y_top, 1 )
        obstacle_top=Obstacle(starting_position_obstacle_x, (-750-obstacle_gap)+(obstacle_y_top), -1)
        obstacle_group.add(obstacle_bottom)
        obstacle_group.add(obstacle_top)
        last_tick=present_time

    obstacle_group.draw(screen)
    obstacle_group.update()
    show_rock(rock_x, rock_y)
    pygame.display.update()
pygame.quit()
