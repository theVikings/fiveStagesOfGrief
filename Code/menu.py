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

continueGeneral = 1
levelFinished = 0

while continueGeneral:
    arrowPos = 1
    menuContinue = 1
    jeuContinue = 1
    
    # Musique du menu : AND HIS NAME IS JOHN CENA !!
    pygame.mixer.music.load("JC.mp3")
    pygame.mixer.music.play()
    
    # Boucle de menu    
    while menuContinue:
        optionsContinue = 1
       
        # Limitation de la vitesse de la boucle
        # 30 frames par seconde suffisent
        pygame.time.Clock().tick(30)
    
        # On attend les évènements
        for event in pygame.event.get():
                
            # Quitter
            if event.type == QUIT:
                menuContinue = 0
                continueGeneral = 0
                
            # Si on clique sur flèche du bas, flèche descend    
            elif event.type == KEYDOWN and event.key == K_DOWN:
                sonMove = pygame.mixer.Sound("soundReturn.wav")
                sonMove.play()
                                
                if arrowPos<7:
                    if levelFinished == arrowPos-1:
                        arrowPos = 6
                    else:    
                        arrowPos+=1
                    fond = pygame.image.load("bgMenu"+str(arrowPos)+".jpg").convert()
                    fenetre.blit(fond, (0,0))
    
            # Si on clique sur flèche du haut, flèche monte        
            elif event.type == KEYDOWN and event.key == K_UP:
                sonMove = pygame.mixer.Sound("soundReturn.wav")
                sonMove.play()
                
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
                # CHOIX = EXIT
                if arrowPos == 7:
                    menuContinue = 0
                    continueGeneral = 0
                
                #CHOIX = OPTIONS    
                elif arrowPos == 6:
                    fond = pygame.image.load("options.jpg").convert()
                    fenetre.blit(fond, (0,0))
                    
                    sonClic = pygame.mixer.Sound("soundClick.wav")
                    sonClic.play()
                    
                    while optionsContinue:                
                        for event in pygame.event.get():
                            # CHOIX = RETOUR AU MENU
                            if event.type == KEYDOWN and event.key == K_ESCAPE:
                                sonReturn = pygame.mixer.Sound("soundReturn.wav")
                                sonReturn.play()
                    
                                optionsContinue = 0
                                jeuContinue = 0
                                fond = pygame.image.load("bgMenu6.jpg").convert()
                                fenetre.blit(fond, (0,0))
                        
                        # On refresh        
                        pygame.display.flip()        
                else:
                    menuContinue = 0
                    
            # On refresh        
            pygame.display.flip() 
       
    if not continueGeneral:
        pygame.quit()
    else:    
        #niveau.niveau(arrowPos) 
    
        perso = pygame.image.load("sprite.png").convert()
        fenetre.blit(perso, (0,0))
        
        pygame.mixer.music.stop()
   
        # Boucle de jeu
        while jeuContinue:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    jeuContinue = 0
                    fond = pygame.image.load("bgMenu1.jpg").convert()
                    fenetre.blit(fond, (0,0))
                
                # On refresh        
                pygame.display.flip()     