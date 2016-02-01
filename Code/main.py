import pygame
import sys
from pygame.locals import *
import sprites

# Décor : 1280x720
# Blocks : 20x20
# Largeur : 64 blocks
# Hauteur : 36 blocks

# Lancement
pygame.init()

# Fenêtre : 1280x720 scrollable
fenetre = pygame.display.set_mode((1280,720), pygame.DOUBLEBUF)
# Nom
pygame.display.set_caption('The five stages of Grief')
#Souris non visible dans cadre
pygame.mouse.set_visible(0)

# Background : à modif avec un file lu
fond = pygame.image.load("test.jpg").convert()
fenetre.blit(fond, (0,0))

# Sprite perso
perso = sprites.spritePerso(50,50,"sprite.png")
perso_rect = perso.get_rect()
fenetre.blit(perso.image, perso_rect)


pygame.display.flip()

# Boucle de jeu
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN and event.key == K_SPACE:
            print("Espace")
pygame.quit()            
            
    
