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
        self.images.append(load_image(image1))
        self.images.append(load_image(image2))
        self.images.append(load_image(image3))
        #apparence actuelle de l'entite
        self.image = self.images[1]
        # position (du rectangle) de l'image
        self.rect = pygame.Rect(pos_x, pos_y, constante.taille_block, constante.taille_block)

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

# classe bullet pour les tirs
class Bullet():
    def __init__(self, pos_x, pos_y):
        #apparence actuelle de l'entite
        self.image = load_image("bullet.png").convert_alpha()
        # position (du rectangle) de l'image
        self.rect = pygame.Rect(pos_x, pos_y, constante.taille_block, constante.taille_block)

   	# Retourne la position
    def get_rect(self):
    	return self.rect

    # Retourne l'apparence actuelle
    def get_img(self):
    	return self.image

    def canMoveRight(self,surrondings):
        if(((surrondings[3][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[3][0]))):
           return False
        else:
           return True
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

    def canMoveUp(self,surrondings):
        if(((surrondings[0][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[0][0]) or ((surrondings[4][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[4][0])) or ((surrondings[5][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[5][0])))):
           return False
        else:
           return True

    def canMoveDown(self,surrondings):
        if(((surrondings[2][1] not in constante.listeCaracSpe)and self.rect.colliderect(surrondings[2][0]))):
           return False
        else:
           return True

    def canMoveLeft(self,surrondings):
        if(((surrondings[1][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[1][0]))):
           return False
        else:
           return True

    def canMoveRight(self,surrondings):
        if(((surrondings[3][1] not in constante.listeCaracSpe) and self.rect.colliderect(surrondings[3][0]))):
           return False
        else:
           return True

    def isFinDuLevel(self,nomFichier):
        my_fichier = LecteurFichier(nomFichier)
        position = self.getPositionCarreau()
        blocJoueur = my_fichier.recupererBlocPosition(position[0],position[1])
        return (blocJoueur == 'E')

    def jump(self, screen, fond, blocks, surrondings, fichier):
        L_SAUT = 60 #Longeur du saut en pixels
        i = 1
        rapport_saut = 8
        y = 112/rapport_saut
        toucheMur = 0

        while i < L_SAUT*2 + 1 and not toucheMur:   
            if i <= L_SAUT:
                if self.rect.top > 0 and self.canMoveUp(surrondings):
                    self.rect = self.rect.move(0, -y)
                else :
                    self.rect = self.rect.move(0, y)
            elif i > L_SAUT:
                if self.rect.bottom < constante.height+5 and self.canMoveDown(surrondings):
                    self.rect = self.rect.move(0, y)
                else :
                    toucheMur = 1
                    
            self.movement(surrondings)
            display.display(screen, fond, [0,0], self, blocks)
            centre = self.getPositionCarreau()
            surrondings = fichier.getSurrondings(centre[0],centre[1])
            self.movement(surrondings)
            i+=rapport_saut
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os._exit(1)
                    
        if not toucheMur:
            i = 0
            while not toucheMur:
                if self.rect.bottom < constante.height+5 and self.canMoveDown(surrondings):
                    self.rect = self.rect.move(0, y)
                else :
                    toucheMur = 1

                self.movement(surrondings)
                display.display(screen, fond, [0,0], self, blocks)
                centre = self.getPositionCarreau()
                surrondings = fichier.getSurrondings(centre[0],centre[1])
                self.movement(surrondings)
                i+=rapport_saut


    def getBlocAtPosPerso(self,lecteurFichier):
        position = self.getPositionCarreau()
        blocJoueur = lecteurFichier.recupererBlocPosition(position[0],position[1])
        return blocJoueur

    def isPersoDying(self,lecteurFichier):
        if(self.getBlocAtPosPerso(lecteurFichier)=='S' or self.getBlocAtPosPerso(lecteurFichier)=='s'):
            os._exit(1)
    def tirer(self, screen, fond, blocks, surrondings, fichier):
        if self.get_img() == self.images[1]: #tire à droite
            tir = Bullet(self.rect.right + 5, self.rect.top + 5)
            target = tir.rect.right + 700
            while tir.rect.right < target and tir.canMoveRight(surrondings):
                screen.blit(tir.get_img(), tir.rect)
                pygame.display.flip()
                screen.blit
                display.display(screen, fond, [0,0], self, blocks)
                tir.rect = tir.rect.move(10,0)
                centre = self.getPositionCarreau()
                surrondings = fichier.getSurrondings(centre[0],centre[1])
                self.movement(surrondings)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        os._exit(1)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        self.jump(screen, fond, blocks, surrondings, fichier)
                
# Class Enemy (entite adverse) herite de 'MySprite'
class Enemy(MySprite):
    #constructeur
    def __init__(self, pos_x, pos_y, image1, image2, image3, speed):
        MySprite.__init__(self, pos_x, pos_y, image1, image2, image3)
        self.speed = speed
