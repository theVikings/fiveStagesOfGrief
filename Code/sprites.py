import sys
import pygame
from pygame.locals import *

# Sprite du perso principal
class spritePerso():

    # Constructeur
    def __init__(self, x, y, img):    
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = Rect(x,y,20,20)

    # Getters
    def get_rect(self):
        return self.rect

    def get_img(self):
        return self.image
        
