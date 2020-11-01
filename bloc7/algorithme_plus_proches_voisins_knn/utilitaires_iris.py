import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def charger_fichier_entete( nom_fic ):
    """
    Permet de lire un fichier CSV en utilisant la ligne d'entêtes
    Retourne une liste de dictionnaires.
    """
    lignes = []
    with open( nom_fic , "r", newline ="", encoding ="utf -8" ) as csvfile :
        lecteur = csv.DictReader( csvfile , delimiter =",")
        for enreg in lecteur :
            lignes.append (dict ( enreg )) # enreg est de type OrderedDict on le remet endict
    return lignes

def extraire_deux_colonnes(descripteur1, descripteur2, table):
    '''
    Retourne six listes : se1, se2, ve1, ve2, vi1, vi2    
    #setosa, versicolor, virginica
    
    descripteur1 et descripteur2 sont les noms des colonnes au choix parmi longueur_sepale, 
    largeur_sepale, longueur_petale, largeur_petale    
    '''

    se1, se2 = [], []
    for i in range(50):
        se1.append(float(table[i][descripteur1]))
        se2.append(float(table[i][descripteur2]))
        
    ve1, ve2 = [], []
    for i in range(50, 100):
        ve1.append(float(table[i][descripteur1]))
        ve2.append(float(table[i][descripteur2]))
        
    vi1, vi2 = [], []
    for i in range(100, 150):
        vi1.append(float(table[i][descripteur1]))
        vi2.append(float(table[i][descripteur2]))
    
    return se1, se2, ve1, ve2, vi1, vi2

def afficher_deux_colonnes(x, y, colorc, ax):
    ax.plot(x, y, linestyle = ' ', marker = 'o', color = colorc)

def afficher_donnees_deux_colonnes(descripteur1, descripteur2, table):
    '''
    affiche un graphique 2D avec en abscisse descripteur1 et en ordonnée descripteur2
    '''
    
    fig = plt.figure(figsize = (4, 4))
    ax = fig.add_subplot(111)
    
    se1, se2, ve1, ve2, vi1, vi2 = extraire_deux_colonnes(descripteur1, descripteur2, table)
    afficher_deux_colonnes(se1, se2, "#ff0000", ax)
    afficher_deux_colonnes(ve1, ve2, "#00ff00", ax)
    afficher_deux_colonnes(vi1, vi2, "#0000ff", ax)
    
    plt.gca().set_xlabel(descripteur1, size = 18)
    plt.gca().set_ylabel(descripteur2, size = 18)
    plt.show()
    print("setosa : rouge, versicolor : vert, virginica : bleu")
    
    
    
def extraire_trois_colonnes(descripteur1, descripteur2, descripteur3, table):
    '''
    Retourne neuf listes : se1, se2, se3, ve1, ve2, ve3, vi1, vi2, vi3    
    #setosa, versicolor, virginica
    
    descripteur1, descripteur2, descripteur3 sont les noms des colonnes au choix parmi longueur_sepale, 
    largeur_sepale, longueur_petale, largeur_petale     
    '''
    
    se1, se2, se3 = [], [], []
    for i in range(50):
        se1.append(float(table[i][descripteur1]))
        se2.append(float(table[i][descripteur2]))
        se3.append(float(table[i][descripteur3]))
        
    ve1, ve2, ve3 = [], [], []
    for i in range(50, 100):
        ve1.append(float(table[i][descripteur1]))
        ve2.append(float(table[i][descripteur2]))
        ve3.append(float(table[i][descripteur3]))
        
    vi1, vi2, vi3 = [], [], []
    for i in range(100, 150):
        vi1.append(float(table[i][descripteur1]))
        vi2.append(float(table[i][descripteur2]))
        vi3.append(float(table[i][descripteur3]))
    
    return se1, se2, se3, ve1, ve2, ve3, vi1, vi2, vi3

def afficher_trois_colonnes(x, y, z, colorc, ax):
    ax.scatter(x, y, z, marker = 'o', color = colorc)


def afficher_donnees_trois_colonnes(descripteur1, descripteur2, descripteur3, table):
    '''
    affiche un graphique 2D avec en abscisse descripteur1 et en ordonnée descripteur2
    '''
    se1, se2, se3, ve1, ve2, ve3, vi1, vi2, vi3 = extraire_trois_colonnes(descripteur1, descripteur2, descripteur3, table)
    
    fig = plt.figure(figsize = (4, 4))
    ax = fig.add_subplot(111, projection='3d')
    
    afficher_trois_colonnes(se1, se2, se3, "#ff0000", ax)
    afficher_trois_colonnes(ve1, ve2, ve3, "#00ff00", ax)
    afficher_trois_colonnes(vi1, vi2, vi3, "#0000ff", ax)
    
    ax.set_xlabel(descripteur1, size = 18)
    ax.set_ylabel(descripteur2, size = 18)
    ax.set_zlabel(descripteur3, size = 18)
    plt.show()
    print("setosa : rouge, versicolor : vert, virginica : bleu")
    


