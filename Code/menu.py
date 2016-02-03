# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:17:34 2016

@author: Nicolas
"""

import pygame
import classes
import display
import class_decors
import os
from pygame.locals import *

# Lancement
pygame.init()

# Fenêtre : 1280x720
fenetre = pygame.display.set_mode((1280,720))

# Nom
pygame.display.set_caption('The Five Stages of Grief')

#Souris non visible dans cadre
pygame.mouse.set_visible(0)

continueGeneral = 1
levelFinished = 0

# Menu de contrôle général
while continueGeneral:
    arrowPos = 1
    menuContinue = 1
    jeuContinue = 1

    # Musique du menu : AND HIS NAME IS JOHN CENA !!
    pygame.mixer.music.load("JC.mp3")
    pygame.mixer.music.play()

    # Background : image avec flèches qui reload page avec boutons
    fond = pygame.image.load("bgMenu"+str(arrowPos)+".jpg").convert()
    fenetre.blit(fond, (0,0))

    pygame.display.flip()

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

#----------------------------------------------------------------------------------------#

    if not continueGeneral:
        # Arrêt général
        pygame.quit()
    else:
        # ON A SELECTIONNE UN NIVEAU

        pygame.mixer.music.stop()
        numEcran = 0

        # Launch music
        pygame.mixer.music.load('huntingForYourDreams.mp3')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

        # Création du lecteur de fichier
        my_fichier = classes.LecteurFichier("niveau"+str(arrowPos)+"/"+str(numEcran+1)+".txt")

        #Chargement du niveau
        tableauEcran = os.listdir('niveau'+str(arrowPos))
        nombreEcran = len(tableauEcran)
        nomNiveau = 'niveau'+str(arrowPos)+'/'+tableauEcran[numEcran]
        niveau = classes.Niveau(nomNiveau)
        niveau.genererTableau()

        # Déclaration des blocks + récupération des blocks à partir fichier + création blocks
        id = niveau.structure
        groupe_blocks_test = class_decors.Blocks_Groupe(id)

        # Création perso + objets décor
        fond = pygame.image.load("bgNiveau"+str(arrowPos)+"-"+str(numEcran+1)+".jpg").convert()
        posDepart = my_fichier.retournePositionCaractere('D')
        my_hero = classes.MyHero(posDepart[0], posDepart[1], "data/char_hero/face_hero.png", "data/char_hero/latD_hero.png", "data/char_hero/latG_hero.png")

        # Boucle de jeu
        while jeuContinue:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    jeuContinue = 0
                if event.type == QUIT:
                    pygame.quit()

            # Mouvement des entités
            centre = my_hero.getPositionCarreau()
            surrondings = my_fichier.getSurrondings(centre[0],centre[1])
            my_hero.movement(surrondings)

            if(my_hero.isFinDuLevel(nomNiveau)):
                if(numEcran+1<nombreEcran):
                    numEcran+=1
                    nomNiveau = 'niveau'+str(arrowPos)+'/'+tableauEcran[numEcran]
                    niveau = Niveau(nomNiveau)
                    niveau.genererTableau()
                    my_fichier = LecteurFichier(nomNiveau)
                    positionHero = my_fichier.retournePositionCaractere('D')
                    my_hero.setPosition(positionHero[0],positionHero[1])

            # Affichage de la fenêtre
            display.display(fenetre, fond, [0,0], my_hero, groupe_blocks_test)

#----------------------------------------------------------------------------------------#
