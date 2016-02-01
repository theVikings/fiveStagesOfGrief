import sys
import pygame
import os

from display import *
from class_entity import *


###############################################################################
#boucle de jeu
def game_loop():
    #declaration du personnage
    my_hero = MyHero(200, 200, "data/char_hero/face_hero.jpg", "data/char_hero/latD_hero.jpg", "data/char_hero/latG_hero.jpg")
# Boucle de jeu
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(1)

        #######################################################################
        #instruction de jeu
        #######################################################################
        # mouvement des entitées
        my_hero.movement()
        #affichage de la fenetre
        # Affichage
        display(screen, background_image, background_position,my_hero)


###############################################################################
## POINT D ENTREE DU CODE #####################################################
###############################################################################
# Initialisation modules pygames
pygame.init()
# Charge l'image de fond
background_image = load_image("data/background/background.jpg")
background_position = [0, 0]
# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640,480
screen = pygame.display.set_mode(size)
# Lance la musique
pygame.mixer.music.load('data/tracks/music.mp3')
pygame.mixer.music.play(10)
# lance la boucle de jeu
game_loop()
