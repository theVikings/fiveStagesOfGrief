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
                if id_colonne_case == 's':

                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "spikeInvert.png")
                    self.tableau_blocks.append(block)
                elif id_colonne_case == 'B' or id_colonne_case == 'F':

                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "cobble.png")
                    self.tableau_blocks.append(block)
                elif id_colonne_case == 'S':

                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "spike.png")
                    self.tableau_blocks.append(block)

                elif id_colonne_case == 'z':
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "platform.png")
                    self.tableau_blocks.append(block)
                    
                elif id_colonne_case == 'i':
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block_Mouvement((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "platform.png", 200, 0, [4,0])
                    self.tableau_blocks.append(block)

                elif id_colonne_case == 'u':
                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block_Mouvement((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "platform.png", -160, 0, [4,0])
                    self.tableau_blocks.append(block)    
                    
                elif id_colonne_case == '\n':

                    # Création du carreau -> repositionnment -> affichage
                    block = constante.Block((colonne-1)*constante.taille_block, (ligne-1)*constante.taille_block, "dirt.jpg")
                    self.tableau_blocks.append(block)
                colonne = colonne + 1
            ligne = ligne + 1
