# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:17:34 2016

@author: Nicolas
"""

import pygame
from pygame.locals import *

# Lancement
pygame.init()

# Fenêtre : 1280x720 
fenetre = pygame.display.set_mode((1280,720))
# Nom
pygame.display.set_caption('The Five Stages of Grief')
#Souris non visible dans cadre
pygame.mouse.set_visible(0)

# Background : image avec flèches qui reload page avec boutons
fond = pygame.image.load("bgMenu1.jpg").convert()
fenetre.blit(fond, (0,0))

pygame.display.flip()

arrowPos = 1
menuContinue = 1
levelFinished = 0

# Musique du menu : AND HIS NAME IS JOHN CENA !!
son = pygame.mixer.music.load("JC.mp3")
pygame.mixer.music.play()

while menuContinue:
   
   # Limitation de la vitesse de la boucle
   # 30 frames par seconde suffisent
   pygame.time.Clock().tick(30)

   for event in pygame.event.get():
            
        # Quitter
        if event.type == QUIT:
            menuContinue = 0
        # Si on clique sur flèche du bas, fléche descend    
        elif event.type == KEYDOWN and event.key == K_DOWN:
            if arrowPos<7:
                if levelFinished == arrowPos-1:
                    arrowPos = 6
                else:    
                    arrowPos+=1
                fond = pygame.image.load("bgMenu"+str(arrowPos)+".jpg").convert()
                fenetre.blit(fond, (0,0))

        # Si on clique sur flèche du haut, flèche monte        
        elif event.type == KEYDOWN and event.key == K_UP:
            if arrowPos>1:
                if arrowPos>levelFinished+1:
                    if(arrowPos == 7):
                        arrowPos-=1
                    else:    
                        arrowPos = levelFinished+1
                else:    
                    arrowPos-=1
                fond = pygame.image.load("bgMenu"+str(arrowPos)+".jpg").convert()
                fenetre.blit(fond, (0,0))
        
        # Si on clique sur ENTER, on ouvre le niveau associé à la position actuelle
        elif event.type == KEYDOWN and event.key == K_RETURN:
            if arrowPos == 7:
                menuContinue = 0
                
        # On refresh        
        pygame.display.flip()        
pygame.quit()        