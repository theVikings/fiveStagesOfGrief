from classes import *
import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

# initialise les modules pygame
pygame.init()

#Creation du personnage
my_hero = MyHero(200, 200, "data/char_hero/face_hero.png", "data/char_hero/latD_hero.png", "data/char_hero/latG_hero.png")

#Creation du lecteur de fichier
my_fichier= LecteurFichier("niveau.txt")

# Launch music
pygame.mixer.music.load('huntingForYourDreams.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 1280, 720 #32 blocs de largeur et 18 blocs de hauteur
screen = pygame.display.set_mode(size)
screenNiveau = pygame.display.set_mode(size)


# Charge l'image de fond
background_image = load_image("lavacavern.jpg").convert()
background_position = [0, 0]

#Charge la tête de megaman
dadFace=load_image("dadFace.png").convert()


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
    screen.blit(dadFace,(175,533))
    centre=my_hero.getPositionCarreau()
    surrondings=my_fichier.getSurrondings(centre[0],centre[1])
    my_hero.movement(surrondings)
    screen.blit(my_hero.image,(my_hero.get_rect().topleft))
    pygame.display.flip()



    # Calculs
    # Affichages
    # On recommence jusqu'a ce que l'utilisateur quitte
