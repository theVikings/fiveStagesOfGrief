﻿import pygame

# Méthode permettant de charger une image et renvoyant l'objet surface associé
def load_image(name):
    image = pygame.image.load(name)
    return image

# Dimensions fenêtre de jeu
width = 1280
height = 720

# Taille d'un block de terrain
taille_block = 40

#Liste des caracteres speciaux
listeCaracSpe=['\n','0','E','D','H','u','i','j','x','z','V','S','s']


class Block():
    # Constructeur
    def __init__(self, pos_x, pos_y, image):
        self.image = load_image(image)
        self.rect = pygame.Rect(pos_x, pos_y, taille_block, taille_block)
        self.speed = [0,0]
        self.move_x = 0
        self.move_y = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_end = 0
        self.pos_y_end = 0

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(pos_x, pos_y, taille_block, taille_block)

    def block_move(self):
        if self.rect.left <= self.pos_x or self.rect.right >= self.pos_x_end:
            self.speed[0] = -(self.speed[0])
        if self.rect.top <= self.pos_y or self.rect.bottom >= self.pos_y_end:
            self.speed[1] = -(self.speed[1])
        self.rect = self.rect.move(self.speed)

    def recupererPositionBloc(self):
        x = int((self.rect.centerx/taille_block))
        y = int(self.rect.centery/taille_block)
        centre = [x,y]    


class Block_Mouvement(Block):
        def __init__(self, pos_x, pos_y, image, move_x, move_y, speed):
            Block.__init__(self, pos_x, pos_y, image)
            self.speed = speed
            self.pos_x_end = pos_x + move_x
            self.pos_y_end = pos_y + move_y

        def block_move(self):
            if self.pos_x_end < self.pos_x:
                if self.rect.right > self.pos_x+taille_block or self.rect.left <= self.pos_x_end or self.rect.left < 0:
                    self.speed[0] = -(self.speed[0])
            else:
                if self.rect.left < self.pos_x or self.rect.right > self.pos_x_end or self.rect.right > width:
                    self.speed[0] = -(self.speed[0])
            if self.pos_y_end < self.pos_y:
                if self.rect.top < self.pos_y_end or self.rect.bottom > self.pos_y+taille_block or self.rect.top < 0:
                    self.speed[1] = -(self.speed[1])
            else:
                if self.rect.top < self.pos_y or self.rect.bottom > self.pos_y_end or self.rect.bottom > height:
                    self.speed[1] = -(self.speed[1])
            self.recupererPositionBloc()
            self.rect = self.rect.move(self.speed)
