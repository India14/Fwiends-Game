import pygame
import time
import os
pygame.init()

width = 1280
height = 1280

FramePerSec = pygame.time.Clock
displaysurface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Franco and Steven')

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(())