import sys
import pygame
import os

#chargement des images
def load_image(name):
    image = pygame.image.load(name)
    return image

#affichage global
def display(screen, background_image, background_position, MyHero):
    # Ajoute images a afficher (1er = fond; dernier=1er plan)
    screen.blit(background_image, background_position)
    screen.blit(MyHero.get_img(), MyHero.get_rect())
    # Affichage
    pygame.display.flip()
    screen.blit
    # Limite le nombre d'images par seconde
    pygame.time.wait(10)

#affichage du game over
def display_game_over(screen, background_image, background_position):
    # Cree un objet 'font' (police) necessaire pour afficher du texte
    basicfont = pygame.font.SysFont(None, 48)
    # Cree une 'surface' avec notre Font
    # Les parametres sont le texte, l'antialiasing, et la couleur RVB
    text = basicfont.render('Game Over', True, (255, 0, 0))
    # Affichage de la surface au centre
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)
    pygame.display.flip()
    screen.blit
    pygame.time.wait(1000)
