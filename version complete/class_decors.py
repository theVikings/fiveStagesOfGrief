import sys
import pygame
import os

from class_entity import *
from constante import *

#class representant les blocks du terrain

class Blocks_Groupe():

    #constructor
    def __init__(self, pos_x, pos_y, id, dim_x, dim_y):
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dim_x = dim_x
        self.dim_y = dim_y


    def creation_carreau(self, screen):
        ligne = 1
        colonne = 1


        for id_case in self.id:
            if colonne <= self.dim_x:
                if id_case == 1:
                    #creation du carreau -> repositionnment -> affichage
                    block = Block_classic
                    block.set_position((self.pos_x)+(colonne-1)*taille_block, (self.pos_y)+(ligne-1)*taille_block)
                    screen.blit(block.image, block.rect)
                colonne = colonne + 1
            elif ligne < self.dim_y:
                ligne = ligne + 1
                colonne = 1
                if id_case == 1:
                    #creation du carreau -> repositionnment -> affichage
                    block = Block_classic
                    block.set_position((self.pos_x)+(colonne-1)*taille_block, (self.pos_y)+(ligne-1)*taille_block)
                    screen.blit(block.image, block.rect)
                colonne = colonne + 1
