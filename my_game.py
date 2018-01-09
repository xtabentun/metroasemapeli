import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
playerImg = pygame.image.load("isompispurdo.png")

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

def game_loop():
    player = Player(0,0)
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(playerImg, (player.x, player.y))
    pygame.display.update()

    alive = True
    while alive:
        for event in pygame.event.get():
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
        player.update()
        pygame.display.update()
        clock.tick(60)


game_loop()

time.sleep(2)
