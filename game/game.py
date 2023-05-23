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
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'images/rock{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = int(0)
        self.is_clicked= False
    def update(self):
        #gravity
        if waiting==False:
            self.velocity+=1.5
            if self.velocity>15:
                self.velocity=15
            if self.rect.top<5:
                self.rect.top=10
            if self.rect.bottom>700:
                self.rect.bottom=699
            self.rect.y+=self.velocity
            #controls
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.load('sound/rock_flap.mp3')
                pygame.mixer.music.play()
                self.velocity=-10
        #animation
        self.counter+=1
        cooldown=4
        if self.counter>cooldown:
            self.counter=0
            self.index+=1
            if self.index >= len(self.images):
                self.index=0
            self.image=self.images[self.index]
rock_group=pygame.sprite.Group()
rock=pygame.image.load('images/rock1.png')
rock_x=50
rock_y=325
rock_show=Rock(rock_x, rock_y)
rock_group.add(rock_show)
y_change=0
#obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self) # to inherit the pygame.sprite class
        self.image=pygame.image.load('images/spike.png')
        self.rect=self.image.get_rect()
        if position==1:
            self.image=pygame.transform.flip(self.image , False, True)
            self.rect.bottomleft=[x,y-int(obstacle_gap)/2]
        elif position==-1:
            self.rect.topleft=[x,y+int(obstacle_gap)/2]
    def update(self):
        if waiting==False:
            self.rect.x-=4
            if self.rect.x<-40:
                self.kill() #kys <3
obstacle_group=pygame.sprite.Group()
obstacle_gap=200
starting_position_obstacle_x=500
obstacle_frequency=1500 #miliseconds
last_tick=pygame.time.get_ticks()-obstacle_frequency
#background
bg= pygame.image.load('images/background.png')
#when the game starts
while running:
    clock.tick(fps)
    pygame.display.set_caption("Flappy Rock")
    screen.blit(bg, (0,0))
    rock_group.draw(screen)
    rock_group.update()
    obstacle_group.draw(screen)
    obstacle_group.update()
    if pygame.sprite.groupcollide(rock_group, obstacle_group, False, False):
        pygame.mixer.music.load('sound/rock_dead.mp3')
        pygame.mixer.music.play()
        pygame.time.delay(550)
        break
    rock_show=Rock(rock_x, rock_y)
    present_time=pygame.time.get_ticks()
    if present_time-last_tick>obstacle_frequency:
        obstacle_y_top=random.randrange(190,651) 
        obstacle_bottom=Obstacle(starting_position_obstacle_x, obstacle_y_top, 1 )
        obstacle_top=Obstacle(starting_position_obstacle_x, obstacle_y_top, -1)
        obstacle_group.add(obstacle_bottom)
        obstacle_group.add(obstacle_top)
        last_tick=present_time
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            waiting=False
    pygame.display.update()
pygame.quit()
