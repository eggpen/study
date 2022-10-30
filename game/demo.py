import sys
import pygame

pygame.init()

pygame.display.set_mode((800, 600))

pygame.display.set_caption('myDemo')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()