import pygame
import constante
import display

def load_image(name):
    image = pygame.image.load(name)
    return image

class Niveau:

    """Classe permettant de créer un niveau"""

    # Constructeur
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    # Générateur de tableau à partir de fichier texte
    def genererTableau(self):
        with open(self.fichier, "r") as fichierNiveau:
            structure_niveau = []
            for ligne in fichierNiveau:
                ligne_niveau = []
                for bloc in ligne:
                    if bloc != '\n':
                        ligne_niveau.append(bloc)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

class LecteurFichier:
    # Constructeur
    def __init__(self,fichier):
        self.fichier = fichier

    def recupererBlocPosition(self,x,y):     #x et y étant le nombre de blocs
        i = 0
        lettreBloc = '0'
        with open(self.fichier, "r") as fichierNiveau:
            for ligne in fichierNiveau:
                for bloc in ligne:
                    if i == ((y*33)+x):
                        lettreBloc = bloc
                    i = i+1
        return lettreBloc

    def getSurrondings(self,x,y):
        tableau={}
        tableau[0]=[pygame.Rect(x*constante.taille_block,(y-1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x,y-1)] #carreauHaut
        tableau[1]=[pygame.Rect((x-1)*constante.taille_block,y*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x-1,y)] #carreauGauche
        tableau[2]=[pygame.Rect(x*constante.taille_block,(y+1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x,y+1)]#carreauBas
        tableau[3]=[pygame.Rect((x+1)*constante.taille_block,y*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x+1,y)] #carreauDroit
        tableau[4]=[pygame.Rect((x-1)*constante.taille_block,(y-1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x-1,y-1)] #carreauHautDiagonaleGauche
        tableau[5]=[pygame.Rect((x+1)*constante.taille_block,(y-1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x+1,y-1)] #carreauHautDiagonaleDroit
        tableau[6]=[pygame.Rect((x-1)*constante.taille_block,(y+1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x-1,y+1)] #carreauBasDiagonaleGauche
        tableau[7]=[pygame.Rect((x+1)*constante.taille_block,(y+1)*constante.taille_block,constante.taille_block,constante.taille_block),self.recupererBlocPosition(x+1,y+1)] #carreauBasDiagonaleDroit
        return tableau

    def retournePositionCaractere(self,caractere):
        positionX = -1
        positionY = -1
        numLigne = 0
        with open(self.fichier, "r") as fichierNiveau:
            for ligne in fichierNiveau:
                numCase = 0
                for bloc in ligne:
                    numCase+=1
                    if bloc == caractere:
                        positionX = numCase
                        positionY = numLigne
                numLigne+=1
        if(positionX != -1):
            position = [positionX*constante.taille_block,positionY*constante.taille_block]
            return position
        else:
            return -1

# Entités (classe mère)
class MySprite():
	# Constructeur
    def __init__(self, pos_x, pos_y, image1, image2, image3):
        # Tableau de toutes les images de l'entite
        self.images = []
        imagesG = []
        imagesD = []
        for img in images_bank[0]:
            imagesG.append(load_image(img))
        for img in images_bank[1]:
            imagesD.append(load_image(img))
        self.images.append(imagesG)
        self.images.append(imagesD)
        #apparence actuelle de l'entite
        self.image = self.images[1][0]
        # position (du rectangle) de l'image
        self.rect = pygame.Rect(pos_x, pos_y, 35, 21)
   	# Retourne la position
    def get_rect(self):
    	return self.rect

    # Retourne l'apparence actuelle
    def get_img(self):
    	return self.image

    # modifie l'image actuelle par rapport a la direction souhaite (direction du regard) : "gauche"/"droite"/"centre"
    def set_image(self, cote):
        imagesG = []
        imagesD = []
        for img in images_bank[0]:
            imagesG.append(load_image(img))
        for img in images_bank[1]:
            imagesD.append(load_image(img))
        self.images.append(imagesG)
        self.images.append(imagesD)

    def getCentreSprite(self):
        centreX = self.rect.centerx
        centreY = self.rect.centery
        centre = [centreX,centreY]
        return centre

    def getPositionCarreau(self):
        centre = self.getCentreSprite()
        x = int((centre[0]/constante.taille_block))
        y = int(centre[1]/constante.taille_block)
        centre = [x,y]
        return centre

    def setPosition(self,x,y):
        self.rect = pygame.Rect(x,y,constante.taille_block,constante.taille_block)
        return self.rect

# Class MyHero (personnage principal) : hérite de MySprite
class MyHero(MySprite):
        # Constructeur
        def __init__(self, pos_x, pos_y, image1, image2, image3):
            MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)

        # Gestion du mouvement
        def movement(self,surrondings):
            keys = pygame.key.get_pressed()
           # Teste la touche pressée
            if keys[pygame.K_LEFT] and self.rect.left > 0 and self.canMoveLeft(surrondings):
                self.set_image("gauche")
                self.rect = self.rect.move(-5, 0)
            if keys[pygame.K_RIGHT] and self.rect.right < constante.width+5 and self.canMoveRight(surrondings):
                self.set_image("droite")
                self.rect = self.rect.move(5, 0)
            if keys[pygame.K_UP] and self.rect.top > 0 and self.canMoveUp(surrondings):
                self.set_image("centre")
                self.rect = self.rect.move(0, -5)
            if keys[pygame.K_DOWN] and self.rect.bottom < constante.height+5 and self.canMoveDown(surrondings):
                self.set_image("centre")
                self.rect = self.rect.move(0, 5)
                
        #affichage des animation de marchedu hero
        def anim_marche(self, fenetre, fond, pos,groupe_blocks,sens):
            if sens == "gauche":
                for img in self.images[0]:
                    self.image = img
                    display.display(fenetre, fond, pos, self, groupe_blocks)
            if sens == "droite":
                for img in self.images[1]:
                    self.image = img
                    display.display(fenetre, fond, pos, self, groupe_blocks)
                    
        def canMoveUp(self,surrondings):
            listeCaracSpe=['\n','0','E','D']
            if(((surrondings[0][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[0][0]) or ((surrondings[4][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[4][0])) or ((surrondings[5][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[5][0])))):
               return False
            else:
               return True

        def canMoveDown(self,surrondings):
            listeCaracSpe=['\n','0','E','D']
            if(((surrondings[2][1] not in listeCaracSpe)and self.rect.colliderect(surrondings[2][0]) or ((surrondings[6][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[6][0])) or ((surrondings[7][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[7][0])))):
               return False
            else:
               return True

        def canMoveLeft(self,surrondings):
            listeCaracSpe=['\n','0','E','D']
            if(((surrondings[1][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[1][0]) or ((surrondings[4][1] not in listeCaracSpe)and self.rect.colliderect(surrondings[4][0])) or ((surrondings[6][1] not in listeCaracSpe)and self.rect.colliderect(surrondings[6][0])))):
               return False
            else:
               return True

        def canMoveRight(self,surrondings):
            listeCaracSpe=['\n','0','E','D']
            if(((surrondings[3][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[3][0]) or ((surrondings[5][1] not in listeCaracSpe) and self.rect.colliderect(surrondings[5][0])) or ((surrondings[7][1] not in listeCaracSpe)and self.rect.colliderect(surrondings[7][0])))):
               return False
            else:
               return True

        def isFinDuLevel(self,nomFichier):
            my_fichier = LecteurFichier(nomFichier)
            position = self.getPositionCarreau()
            blocJoueur = my_fichier.recupererBlocPosition(position[0],position[1])
            return (blocJoueur == 'E')

# Class Enemy (entite adverse) herite de 'MySprite'
class Enemy(MySprite):
    #constructeur
    def __init__(self, pos_x, pos_y, image1, image2, image3, speed):
        MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
        self.speed = speed
