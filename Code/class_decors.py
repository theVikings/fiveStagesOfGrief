import constante

# Classe représentant les blocks du terrain

class Blocks_Groupe():

    #constructor
    def __init__(self, id):
        self.id = id
        ligne = 1
        
        self.tableau_blocks = []  
        
        for id_ligne_case in self.id:
            colonne = 1
            for id_colonne_case in id_ligne_case:
                if id_colonne_case == 'd':
                    
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "dirt.jpg")
                    self.tableau_blocks.append(block)
                elif id_colonne_case == 'c':
                    
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "cobble.png")
                    self.tableau_blocks.append(block)
                    print(colonne)
                elif id_colonne_case == 'l':
                    
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "lava.png")
                    self.tableau_blocks.append(block)
                    print(colonne)
                colonne = colonne + 1
            ligne = ligne + 1




#liste des blocks
#Block_classic = Block(100, 0, "data/decors/block1.jpg")
#screen.blit(block.image, block.rect)
#Block_D_Horizontal = Block_Mouvement(0,0,"data/decors/block1.jpg",300,0,[5,0])
