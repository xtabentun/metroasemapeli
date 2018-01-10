import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
playerImg = pygame.image.load("isompispurdo.png")
ESImg = pygame.image.load("ESpieni.png")
class Player(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 100
    height = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        gameDisplay.blit(playerImg, (self.x, self.y))

    def left_bound(self):
        if self.x <= 0:
            self.x_speed = self.x_speed * -1
    def right_bound(self):
        if self.x > display_width - self.width:
            self.x_speed = self.x_speed * -1
    def top_bound(self):
        if self.y <= 0:
            self.y_speed = self.y_speed * -1
    def bottom_bound(self):
        if self.y >= display_height - self.height:
            self.y_speed = self.y_speed * -1

    def bound(self):
        self.left_bound()
        self.right_bound()
        self.top_bound()
        self.bottom_bound()

class ESball(object):
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    width = 90
    height = 90

    def __init__(self):
        side = random.randint(1,4)

        if side == 1:
            self.x = -60
            self.y = random.randint(0, display_height-self.height)
            x_speed = 10
        elif side == 2:
            self.x = random.randint(0, display_width-self.width)
            self.y = -60
            self.y_speed = 10
        elif side == 3:
            self.x = display_width + 60
            self.y = random.randint(0, display_height-self.height)
            self.x_speed = -10
        elif side == 4:
            self.x = random.randint(0, display_width-self.width)
            self.y = display_height + 60
            self.y_speed = -10

    def upfate(self):
        self.x += self.x_speed
        self.y += self.y_speed
        gameDisplay.blit(ESImg, (self.x, self.y))
#def paint_player(player):
    #gameDisplay.blit(playerImg, (player.x, player.y))

def game_loop():
    player = Player(100,100)
    ess = []
    score = 0
    gameDisplay.fill((255,255,255))
    player.update()
    #paint_player(player)
    #gameDisplay.blit(playerImg, (player.x, player.y))
    pygame.display.update()

    alive = True
    while alive:
        ess.append(ESball())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.x_speed = 2
                if event.key == pygame.K_LEFT:
                    player.x_speed = -2
                if event.key == pygame.K_DOWN:
                    player.y_speed = 2
                if event.key == pygame.K_UP:
                    player.y_speed = -2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_speed = 0

        gameDisplay.fill((255,255,255))
        player.bound()
        player.update()
        for es in ess:
            es.update()
        pygame.display.update()
        clock.tick(60)


game_loop()

time.sleep(2)
