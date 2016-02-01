import pygame
import os

class Niveau:

    """Classe permettant de créer un niveau"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def genererTableau(self):
        with open(self.fichier, "r") as fichierNiveau:
            structure_niveau = []
            for ligne in fichierNiveau:
                ligne_niveau = []
                for bloc in ligne:
                    if bloc != '0':
                        ligne_niveau.append(bloc)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    

    

    def afficher(self, fenetre):
        mur = pygame.image.load("dirt.jpg").convert()
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for bloc in ligne:
                x = num_case*40
                y = num_ligne*40
                if bloc == 'b':          
                    fenetre.blit(mur,(x,y))
                num_case += 1
            num_ligne += 1
