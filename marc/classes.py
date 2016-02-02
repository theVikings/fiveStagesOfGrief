import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

class Niveau:

    """Classe permettant de créer un niveau"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def genererTableau(self):
        with open(self.fichier, "r") as fichierNiveau:
            structure_niveau = []
            for ligne in fichierNiveau:
                ligne_niveau = []
                for bloc in ligne:
                    if bloc != '\n':
                        print(bloc)
                        ligne_niveau.append(bloc)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau
        

    

    

    def afficher(self, fenetre):
        dirt = pygame.image.load("dirt.jpg").convert()
        lava= pygame.image.load("lava.png").convert()
        cobble= pygame.image.load("cobble.png").convert()
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for bloc in ligne:
                x = num_case*40
                y = num_ligne*40
                if bloc == 'd':          
                    fenetre.blit(dirt,(x,y))
                elif bloc == 'c' or bloc=='s':
                    fenetre.blit(cobble,(x,y))
                elif bloc == 'l':
                    fenetre.blit(lava,(x,y))
                num_case+=1
            num_ligne += 1



class LecteurFichier:
    def __init__(self,fichier):
        self.fichier=fichier
        
        

    def recupererBlocPosition(self,x,y):     #x et y étant le nombre de bloc
        i=0
        lettreBloc='0'
        with open(self.fichier, "r") as fichierNiveau:
             for ligne in fichierNiveau:
                 for bloc in ligne:
                     i=i+1
                     if(i)==(y*33)+x:
                         lettreBloc=bloc
        return lettreBloc
    
    def getSurrondings(self,x,y):
        tableau={}
        tableau[0]=self.recupererBlocPosition(x,(y-1))
        tableau[1]=self.recupererBlocPosition((x-1),y)
        tableau[2]=self.recupererBlocPosition(x,(y+1))
        tableau[3]=self.recupererBlocPosition((x+1),y)
        print(tableau)
        return tableau
        
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

    def getCentreSprite(self):
        centreX=self.rect.centerx
        centreY=self.rect.centery
        centre=[centreX,centreY]
        return centre

    def getPositionCarreau(self):
        centre=self.getCentreSprite()
        x=round((centre[0]/40))
        y=round(centre[1]/40)-1
        centre=[x,y]
        print(centre)
        return centre


# Class MyHero (personnage principal) : herite de MySprite
class MyHero(MySprite):
        #constructeur
        def __init__(self, pos_x, pos_y, image1, image2, image3):
            MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
        #gestion du mouvement
        def movement(self,surrondings):
            keys = pygame.key.get_pressed()
            # Test la touche pressee
            if keys[pygame.K_LEFT] and self.rect.left > 0 and (surrondings[1]=='0' or surrondings[1]=='\n'):
                self.set_image("gauche")
                self.rect = self.rect.move(-5, 0)
            if keys[pygame.K_RIGHT] and self.rect.right < 1280 and (surrondings[3]=='0' or surrondings[3]=='\n'):
                self.set_image("droite")
                self.rect = self.rect.move(5, 0)
            if keys[pygame.K_UP] and self.rect.top > 0 and (surrondings[0]=='0' or surrondings[0]=='\n'):
                self.set_image("centre")
                self.rect = self.rect.move(0, -5)
            if keys[pygame.K_DOWN] and self.rect.bottom < 720 and (surrondings[2]=='0' or surrondings[2]=='\n'):
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

