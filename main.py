import pygame

pygame.init()


screen=pygame.display.set_mode((800,400))
#setting the tile
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

while True:
    pygame.display.update()

    clock.tick(60)