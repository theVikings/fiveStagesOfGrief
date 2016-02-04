import pygame

from constante import *

# Affichage global
def display(screen, background_image, background_position, MyHero, blocks):
    # Ajoute images a afficher (1er = fond; dernier=1er plan)
    screen.blit(background_image, background_position)
    screen.blit(MyHero.get_img(), MyHero.get_rect())
    for id in blocks.tableau_blocks:
        id.block_move()
        screen.blit(id.image, id.rect)
    pygame.display.flip()
    # Limite le nombre d'images par seconde
    pygame.time.wait(10)


# Affichage du game over
def display_game_over(screen, background_image, background_position):
    # Crée un objet 'font' (police) necessaire pour afficher du texte
    basicfont = pygame.font.SysFont(None, 48)
    # Crée une 'surface' avec notre Font
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
