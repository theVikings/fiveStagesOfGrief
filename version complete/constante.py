import sys
import pygame
import os

from class_decors import *

# Methode permettant de charger une image et renvoyant l'objet surface associee
def load_image(name):
    image = pygame.image.load(name)
    return image


#dimension fenetre de jeu
width = 640
height = 480

#taille d'un blocks de terrain
taille_block = 40


class Block():
    #constructor
    def __init__(self, pos_x, pos_y, image):
        self.image = load_image(image)
        self.rect = pygame.Rect(pos_x, pos_y, 40, 40)

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(pos_x, pos_y, taille_block, taille_block)

#liste des blocks
Block_classic = Block(100, 0, "data/decors/block1.jpg")
