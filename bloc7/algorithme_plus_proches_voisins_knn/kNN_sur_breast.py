import csv
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


def charger_fichier( nom_fic ):
    lignes = [] 
    with open(nom_fic ,'r', newline ='', encoding ='utf-8') as csvfile :
        lecteur = csv.reader ( csvfile , delimiter =',')
        for enreg in lecteur : 
            lignes.append (enreg)
    return lignes

def obtenir_table_datas( chemin_fichier ):
    '''Permet de charger le contenu du fichier de données dans une table'''
    queue_descripteurs = [  'rayon', 'texture', 'perimetre', 'aire', 
                            'regularite', 'compacite', 'concavite', 'nb_concave', 
                            'symetrie', 'fractale']
    sur_queue = ['M', 'ES', 'P']
    descripteurs = ['ID', 'Etiquette']
    for i in range(3):
        for descripteur in queue_descripteurs:
            descripteurs.append(descripteur + sur_queue[i])
    datas = charger_fichier( chemin_fichier )
    table = [ {descripteurs[j]:float(datas[i][j]) for j in range(2, len(descripteurs))} for i in range(len(datas))]
    for i in range(len(table)):
        table[i][descripteurs[0]] = int(datas[i][0])
        table[i][descripteurs[1]] = datas[i][1]
    return table

def extraire_colonne(descripteur, table):
    '''
    Extrait deux listes de la table de mesures passée en argument :
    M : mesures du descripteur sur les patientes étiquetées M
    B : mesures du descripteur sur les patientes étiquetées B
    '''
    M, B = [], []
    for enregistrement in table :
        if enregistrement['Etiquette'] == 'M' :
            M.append(enregistrement[descripteur])
        else : 
            B.append(enregistrement[descripteur])
    return M, B

def afficher_mesures_descripteur(descripteur, table):
    '''
    Trace les points des mesures de la table correspondant au descripteur. 
    Couleur rouge pour les points de diagnostic M et verts pour ceux de diagnostic B.
    '''
    M, B = extraire_colonne(descripteur, table)
    fig = plt.figure(figsize = (10,1))
    plt.plot(M, [0]*len(M), linestyle = ' ', marker = 'o', color = "#ff000030")
    plt.plot(B, [0]*len(B), linestyle = ' ', marker = 'o', color = "#00ff0030")    
    plt.gca().set_xlabel(descripteur, size = 18)
    plt.yticks([])
    #plt.gca().set_ylabel(descripteur2, size = 18)
    plt.show()
    
    
    
def extraire_deux_colonnes(descripteur1, descripteur2, table):
    '''
    Extrait quatre listes de la table de mesures passée en argument :
    M1 : mesures du descripteur 1 sur les patientes M
    M2 : mesures du descripteur 2 sur les patientes M
    B1 : mesures du descripteur 1 sur les patientes B
    B2 : mesures du descripteur 2 sur les patientes B 
    '''
    M1, M2, B1, B2 = [], [], [], []
    for enregistrement in table :
        if enregistrement['Etiquette'] == 'M' :
            M1.append(enregistrement[descripteur1])
            M2.append(enregistrement[descripteur2])
        else : 
            B1.append(enregistrement[descripteur1])
            B2.append(enregistrement[descripteur2]) 
    return M1, M2, B1, B2

def afficher_mesures_deux_descripteurs(descripteur1, descripteur2, table):
    '''
    Trace le nuage de points des mesures de la table correspondant aux descripteurs 1 et 2. 
    Couleur rouge pour les points de diagnostic M et verts pour ceux de diagnostic B.
    '''
    M1, M2, B1, B2 = extraire_deux_colonnes(descripteur1, descripteur2, table)
    plt.plot(M1, M2, linestyle = ' ', marker = 'o', color = "#ff000060")
    plt.plot(B1, B2, linestyle = ' ', marker = 'o', color = "#00ff0060")    
    plt.gca().set_xlabel(descripteur1, size = 18)
    plt.gca().set_ylabel(descripteur2, size = 18)
    plt.show()
    
    
    



def extraire_trois_colonnes(descripteur1, descripteur2, descripteur3, table):
    '''Retourne six listes : M1, M2, M3, B1, B2, B3 
    M1 : mesures du descripteur 1 sur les patientes M
    M2 : mesures du descripteur 2 sur les patientes M
    M3 : mesures du descripteur  sur les patientes M
    B1 : mesures du descripteur 1 sur les patientes B
    B2 : mesures du descripteur 2 sur les patientes B 
    B3 : mesures du descripteur 3 sur les patientes B
    '''    
    M1, M2, M3, B1, B2, B3 = [], [], [], [], [], []
    for enregistrement in table :
        if enregistrement['Etiquette'] == 'M' :
            M1.append(enregistrement[descripteur1])
            M2.append(enregistrement[descripteur2])
            M3.append(enregistrement[descripteur3])
        else : 
            B1.append(enregistrement[descripteur1])
            B2.append(enregistrement[descripteur2])
            B3.append(enregistrement[descripteur3])
    return M1, M2, M3, B1, B2, B3


def afficher_mesures_trois_descripteurs(descripteur1, descripteur2, descripteur3, table):
    '''
    Trace le nuage de points des mesures de la table correspondant aux descripteurs 1, 2 et 3. 
    Couleur rouge pour les points de diagnostic M et verts pour ceux de diagnostic B.
    '''
    M1, M2, M3, B1, B2, B3 = extraire_trois_colonnes(descripteur1, descripteur2, descripteur3, table)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(M1, M2, M3, marker = 'o', color = "#ff000060")
    ax.scatter(B1, B2, B3, marker = 'o', color = "#00ff0060")
    ax.set_xlabel(descripteur1, size = 18)
    ax.set_ylabel(descripteur2, size = 18)
    ax.set_zlabel(descripteur3, size = 18)
    plt.show()


def calculer_distance(patiente_a, patiente_b, descripteurs, coefficients = []):
    '''
    Mesure la distance entre deux patients en prenant en compte :
    - les descripteurs mentionnés dans la liste descripteurs
    - dont les mesures sont affectéss des coefficients indiqués dans la liste coefficients
    '''
    distance = 0
    numero_descripteur = 0
    if coefficients == [] :
        coefficients = [1] * len(descripteurs)
    for descripteur in descripteurs:
        distance = distance + coefficients[numero_descripteur]*(patiente_a[descripteur] - patiente_b[descripteur])**2
        numero_descripteur = numero_descripteur + 1
    distance = math.sqrt(distance)
    return distance 

def extraire_distances_et_etiquettes(patiente_a_diagnostiquer, table_apprentissage, descripteurs, coefficients = []):
    '''
    Renvoie la liste des couples (distance, étiquette) entre un patient et tous les patients de table_apprentissage
    en prenant en compte les descripteurs mentionnés dans la liste affectés des coefficients
    présents dans la liste des coefficients.
    '''
    distances_et_etiquettes = []
    for mesure in table_apprentissage:
        distance = calculer_distance(patiente_a_diagnostiquer, mesure, descripteurs, coefficients)
        distances_et_etiquettes.append((distance, mesure['Etiquette']))
    return distances_et_etiquettes

def diagnostic_k_plus_proches_voisins(distances_et_etiquettes, k):
    '''Renvoie l'étiquette prédite à partir d'une liste de distances et d'étiquettes.'''
    distances_et_etiquettes.sort(key = lambda couple: couple[0])
    k_etiquettes = [distances_et_etiquettes[i][1] for i in range(k)]
    nb_malignes = k_etiquettes.count('M')
    nb_benignes = k_etiquettes.count('B')
    diagnostic = 'M' if nb_malignes > nb_benignes else 'B'
    return diagnostic

def evaluer_methode(patiente, table_apprentissage, descripteurs, k):
    '''
    Retourne le couple Etiquette, Diagnostic d'une patiente où :
    - l'étiquette est celle qui a été constatée sur la patiente
    - le diagnostic est celui effectué sur la patiente à partir des 30 mesures effectuées sur celle-ci
    - en utilisant les données contenues dans la table d'apprentissage
    '''
    distances_et_etiquettes = extraire_distances_et_etiquettes(patiente, table_apprentissage, descripteurs)
    diagnostic = diagnostic_k_plus_proches_voisins(distances_et_etiquettes, k)
    return patiente['Etiquette'], diagnostic

def LOOCV(descripteurs, k, table_mesures):
    '''
    Pour chaque patiente de table_mesures :
        - crée la table d'apprentissage en enlevant la patiente de la table des mesures,
        - effectue un diagnostic sur la patiente en se basant sur les mesures de cette patiente
        - compare la diagnostic obtenu avec l'étiquette de la patiente
        - en fonction du résultat, augmente le compteur correspondant
    (nb_BM désigne ainsi le nombre de patientes Bénignes ayant eu un diagnostic Maligne)
    (c'est à dire le nombre de faux positifs)  
    '''
    nb_BB, nb_BM, nb_MM, nb_MB = 0, 0, 0, 0
    for numero_patiente in range(569):
        patiente = table_mesures[numero_patiente]
        table_apprentissage = table_mesures[:numero_patiente]
        table_apprentissage.extend(table_mesures[numero_patiente+1:])
        (etiquette, diagnostic) = evaluer_methode(patiente, table_apprentissage, descripteurs, k)
        if (etiquette, diagnostic) == ('B', 'B'):
            nb_BB = nb_BB + 1
        elif (etiquette, diagnostic) == ('B', 'M'):
            nb_BM = nb_BM + 1
        elif (etiquette, diagnostic) == ('M', 'M'):
            nb_MM = nb_MM + 1
        elif (etiquette, diagnostic) == ('M', 'B'):
            nb_MB = nb_MB + 1
    return (nb_BB, nb_BM, nb_MM, nb_MB)

def afficher_contingences(resultats):
    '''
    permet d'afficher dans une table les résultats de la méthode de prédiction
    E pour Etiquette
    D pour diagnostic
    '''
    nb_BB, nb_BM, nb_MM, nb_MB = resultats
    lines = []
    lines.append('-------------------')
    lines.append('| \_ D|  B  |  M  |')
    lines.append('|E  \ |     |     |') 
    lines.append('-------------------')
    lines.append('|  B  |' + '{:^5}'.format(nb_BB) + '|' +  '{:^5}'.format(nb_BM) + '|')
    lines.append('-------------------')
    lines.append('|  M  |' + '{:^5}'.format(nb_MB) + '|' +  '{:^5}'.format(nb_MM) + '|')
    lines.append('-------------------')
    for line in lines :
        print(line)
