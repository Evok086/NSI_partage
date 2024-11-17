# Ex 1

def entiers_consecutifs(tab):
    tab1 = []
    prec = tab[0]
    suiv = tab[1]
    for i in range(len(tab)-2):
        if suiv == prec + 1:
            tab1.append((prec,suiv))
        prec = suiv
        suiv = tab[i+2]
    return tab1

assert entiers_consecutifs([4, 8, 9, 5, 4, 0]) == [(8, 9)]
assert entiers_consecutifs([4, 8, -1, 9, 0]) == []
assert entiers_consecutifs([4, 8, 9, 5, -2, -1, 0, 3]) == [(8, 9), (-2, -1), (-1, 0)]


# EX 2

def coefficients_binomiaux(n):
    tab = [[1]]
    for i in range(n):
        ligne_precedente = tab[-1]
        ligne_suivante = [1]
        for j in range(len(ligne_precedente)):
            nb1 = ligne_precedente[j]
            if j+1 < len(ligne_precedente):
                nb2 = ligne_precedente[j+1]
            else:
                nb2 = 0
            ligne_suivante.append(nb1+nb2)
        tab.append(ligne_suivante)
    return tab

assert coefficients_binomiaux(0) == [[1]]
assert coefficients_binomiaux(1) == [[1],[1,1]]
assert coefficients_binomiaux(2) == [[1],[1,1],[1,2,1]]
assert coefficients_binomiaux(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]


# Ex 3

def crible_eratosthene(n):
    tab = [False, False]
    for i in range(n-2):
        tab.append(True)
    for j in range(len(tab)):
        if tab[j] == True:
            m = 2
            while True:
                k = j*m
                if k > len(tab)-1:
                    break
                tab[k] = False
                m += 1
    premiers = []
    for h in range(len(tab)):
        if tab[h]:
            premiers.append(h)
    return premiers

assert crible_eratosthene(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]


# Ex 4

def inserer(tab,indice,elt):
    tab1 = [0 for i in range(len(tab)+1)]
    decalage = 0
    for i in range(len(tab)):
        if i == indice:
            tab1[indice] = elt
            decalage = 1
        if indice >= len(tab):
            tab1[-1] = elt
        tab1[i+decalage] = tab[i]
    return tab1

ma_liste = [7, -1, 5]
assert inserer(ma_liste, 0, 2) == [2, 7, -1, 5]
assert inserer(ma_liste, 2, 2) == [7, -1, 2, 5]
assert inserer(ma_liste, 3, 2) == [7, -1, 5, 2]
assert inserer(ma_liste, 6, 2) == [7, -1, 5, 2]