import sys
import pygame
import os

from class_entity import *
from constante import *

#class representant les blocks du terrain

class Blocks_Groupe():

    #constructor
    def __init__(self, id):
        self.id = id
        ligne = 1
        colonne = 1
        self.tableau_blocks = []
        for id_ligne_case in self.id:
            for id_colonne_case in id_ligne_case:
                if id_colonne_case == 1:
                    #creation du carreau -> repositionnment -> affichage
                    block = Block((colonne-1)*taille_block, (ligne-1)*taille_block,"data/decors/block1.jpg")
                    self.tableau_blocks.append(block)
                elif id_colonne_case == 2:
                    #creation du carreau -> repositionnment -> affichage
                    block = Block_Mouvement((colonne-1)*taille_block, (ligne-1)*taille_block,"data/decors/block1.jpg",width,height,[4,0])
                    self.tableau_blocks.append(block)
                elif id_colonne_case == 3:
                    #creation du carreau -> repositionnment -> affichage
                    block = Block_Mouvement((colonne-1)*taille_block, (ligne-1)*taille_block,"data/decors/block1.jpg",width,height,[0,4])
                    self.tableau_blocks.append(block)
                colonne = colonne + 1
            ligne = ligne + 1




#liste des blocks
#Block_classic = Block(100, 0, "data/decors/block1.jpg")
#screen.blit(block.image, block.rect)
#Block_D_Horizontal = Block_Mouvement(0,0,"data/decors/block1.jpg",300,0,[5,0])
