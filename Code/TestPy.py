from classes import *
import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

# initialise les modules pygame
pygame.init()

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
screenNiveau = pygame.display.set_mode(size)


# Charge l'image de fond
background_image = load_image("space.png").convert()
background_position = [0, 0]




#Chargement du niveau
niveau = Niveau("niveau.txt")
niveau.genererTableau()
# Boucle de jeu
while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		os._exit(1)
    screen.blit(background_image,background_position)
    niveau.afficher(screen)
    pygame.display.flip()



    # Calculs
    # Affichages
    # On recommence jusqu'a ce que l'utilisateur quitte
