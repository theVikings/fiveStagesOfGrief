import sys
import pygame
import os

#taille de la fenetre de jeu
width = 640
height = 480
# Methode permettant de charger une image et renvoyant l'objet surface associee
def load_image(name):
    image = pygame.image.load(name)
    return image


#Entites (classe mere)
class MySprite():
	# Constructeur
    def __init__(self, pos_x, pos_y, image1, image2, image3):
        # Tableau de toutes les images de l'entite
        self.images = []
        self.images.append(load_image(image1))
        self.images.append(load_image(image2))
        self.images.append(load_image(image3))
        #apparence actuelle de l'entite
        self.image = self.images[1]
        # position (du rectangle) de l'image
        self.rect = pygame.Rect(pos_x, pos_y, 48, 48)

   	# Retourne la position
    def get_rect(self):
    	return self.rect

    # Retourne l'apparence actuelle
    def get_img(self):
    	return self.image

    # modifie l'image actuelle par rapport a la direction souhaite (direction du regard) : "gauche"/"droite"/"centre"
    def set_image(self, cote):
        if cote is "droite":
            self.image = self.images[1]
        if cote is "gauche":
            self.image = self.images[2]
        if cote is "centre":
            self.image == self.images[0]



# Class MyHero (personnage principal) : herite de MySprite
class MyHero(MySprite):
        #constructeur
        def __init__(self, pos_x, pos_y, image1, image2, image3):
            MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
        #gestion du mouvement
        def movement(self):
            keys = pygame.key.get_pressed()
            # Test la touche pressee
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.set_image("gauche")
                self.rect = self.rect.move(-5, 0)
            if keys[pygame.K_RIGHT] and self.rect.right < width:
                self.set_image("droite")
                self.rect = self.rect.move(5, 0)
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.set_image("centre")
                self.rect = self.rect.move(0, -5)
            if keys[pygame.K_DOWN] and self.rect.bottom < height:
                self.set_image("centre")
                self.rect = self.rect.move(0, 5)


# Class Enemy (entite adverse) herite de 'MySprite'
class Enemy(MySprite):
    #constructeur
    def __init__(self, pos_x, pos_y, image1, image2, image3):
        MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
        self.speed = speed
    #gestion du deplacement
    #def movement(self):
