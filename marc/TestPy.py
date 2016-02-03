from classes import *
import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

# initialise les modules pygame
pygame.init()

#Creation du personnage
my_hero = MyHero(0, 0, "data/char_hero/face_hero.png", "data/char_hero/latD_hero.png", "data/char_hero/latG_hero.png")



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




#Chargement du niveau
tableauEcran=os.listdir('level1')
nombreEcran=len(tableauEcran)
numEcran=0
nomNiveau='level1/'+tableauEcran[numEcran]
niveau = Niveau(nomNiveau)
niveau.genererTableau()

#Creation du lecteur de fichier
my_fichier= LecteurFichier(nomNiveau)
# Boucle de jeu
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(1)
    centre=my_hero.getPositionCarreau()
    surrondings=my_fichier.getSurrondings(centre[0],centre[1])
    my_hero.movement(surrondings)    
    screen.blit(background_image,background_position)
    niveau.afficher(screen)
    screen.blit(my_hero.image,(my_hero.get_rect().topleft))
    pygame.display.flip()
    if(my_hero.isFinDuLevel(nomNiveau)):
        if(numEcran+1<nombreEcran):
            numEcran=numEcran+1
            nomNiveau='level1/'+tableauEcran[numEcran]
            niveau=Niveau(nomNiveau)
            niveau.genererTableau()
            my_fichier=LecteurFichier(nomNiveau)
            positionHero=my_fichier.retournePositionCaractere('D')
            my_hero.setPosition(positionHero[0],positionHero[1])
            



    # Calculs
    # Affichages
    # On recommence jusqu'a ce que l'utilisateur quitte
