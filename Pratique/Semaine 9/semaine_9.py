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