#ex5
def premier(x):
    compteur = 2
    var = True
    while x > compteur and var == True :
        if x%compteur == 0 :
            var = False 
        compteur = compteur + 1
    return var

#ex6
def kpremier(k):
    range(k)
    compteur = 2
    var = True
    while k > compteur and var == True :
       if k % compteur == 0 :
            var = False 
    compteur = compteur + 1
    return var
