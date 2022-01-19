from collections import Counter
import random

def oe ():
    o = int(input("Donnes le nombre recherché: ")) #Valeurs de base cherché
    l = int(input("Et donnes la marge du nombre randoms (0, n): "))
    n = 1 #Dit juste le nombre d'opérations faites
    k = 0 #Compte le nombre de 1 dans la boucle
    y = -1 #Compteur de liste
    nom = [] #liste ou on va mettre tous les nombres hasardeux
    t =o+1#nombre hasardeux
    
    while t != o:
        t = random.randint(0, l)
        if t==1:
            k = k +1
        nom.append(t)
        n=n+1
        #print(t)
    print("il y a eu", n-1," oppérations avant d'atteindre", o,)
    h = Counter(nom).most_common(1)[0][0]
    j = Counter(nom).most_common(1)[0][1]
    print ("le nombre apparu le plus de fois est", h," avec", j,"apparitions")
    print ("il a aussi eu",k," fois le nombre 1")
    return None

def des():
    p = 0
    if 'n' in locals() == None :
        None
    else :
        n = int(input("Combien de dés tu veux ? "))

    if 'x' in locals() :
        None
    else :
        x = int(input("Des dés avec combien de faces ? "))
    for i in range(0, n):
        u = random.randint(1, x)
        p = p + u
    print ("La somme des ",n ,"dés de ", x," faces est de", p)
    return None

def comptedes():
    r = int(input("Combien de fois veux-tu lancer les dés ? "))
    ##n = int(input("Combien de dés tu veux ? "))
    ##x = int(input("Des dés avec combien de faces ? "))
    for i in range(0, r):
        des()
    return None

##compte des marche pas (2 fois le cbn de dé tu veux dans le else)
##donc maybe le n in locals  et peut etre aussi le r dans comptedes() à déplacer
##(jsp)
