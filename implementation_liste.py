def creer_liste_vide():
    '''
    crée une liste vide
    '''
    return None

def est_vide(lst):
    '''
    renvoie True si lst est la liste vide, False sinon'''
    return lst is None

def ajouter_tete(lst, elt):
    '''
    renvoie une nouvelle liste avec elt en tête et lst en queue
    '''
    return (elt, lst)

def tete(lst):
    '''
    renvoie l'élément de tête de lst
    pré : est_vide(lst) = faux
    '''
    assert est_vide(lst) == False, 'la liste est vide'
    return lst[0]

def queue(lst):
    '''
    renvoie la liste de queue de lst
    pré : est_vide(lst) = faux
    '''
    assert est_vide(lst) == False, 'la liste est vide'
    return lst[1]

def representer_liste(lst):
    if est_vide(lst):
        return '<>'
    else:
        return f'<{elements(lst)}>'

def elements(lst):
    if not est_vide(queue(lst)):
        return f'{tete(lst)}, {elements(queue(lst))}'
    else:
        return str(tete(lst))

def taille(lst):
    if est_vide(lst):
        return 0
    return 1 + taille(queue(lst))

def acceder(lst, k):
    if est_vide(lst):
        return None
    if k == 1:
        return tete(lst)
    return acceder(queue(lst), k-1)
    """var = lst
    if est_vide(lst):
        return None
    for _ in range(k-1):
        var = queue(var)
    return tete(var)"""
    
def modifier(lst, i, val,k=0):
    n = 0
    liste = creer_liste_vide()
    if tete(lst) == val:
        liste.ajouter_tete(liste, val)
    if k == i:
    '''for l in range(k+1):
        liste = ajouter_tete(lst, acceder(lst, l))
        if l == i:
            liste = ajouter_tete(lst, val)
            for j in range(taille(lst)-i):
                liste = ajouter_tete(lst, acceder(lst, j))
            return liste
        modifier(liste, i, val,k+1)'''
        

lst = creer_liste_vide()
lst = ajouter_tete(lst, 7)
lst = ajouter_tete(lst, 0)
lst = ajouter_tete(lst, 5)
lst = ajouter_tete(lst, 15)
lst = ajouter_tete(lst, 5)
lst = ajouter_tete(lst, -2)
lst = ajouter_tete(lst, 1)
lst = ajouter_tete(lst, 5)
lst = ajouter_tete(lst, 12)
lst = ajouter_tete(lst, 0)
lst = ajouter_tete(lst, 5)
lst = ajouter_tete(lst, -2)
lst = ajouter_tete(lst, 7)
print(representer_liste(lst))
assert taille(lst) == 13
assert acceder(lst, 5) == 12
nouvelle_liste = modifier(lst, 5, -20)
assert representer_liste(nouvelle_liste) == '<7, -2, 5, 0, -20, 5, 1, -2, 5, 15, 5, 0, 7>'
nouvelle_liste = modifier(lst, 1, -20)
assert representer_liste(nouvelle_liste) == '<-20, -2, 5, 0, 12, 5, 1, -2, 5, 15, 5, 0, 7>'
nouvelle_liste = modifier(lst, 13, -20)
assert representer_liste(nouvelle_liste) == '<7, -2, 5, 0, 12, 5, 1, -2, 5, 15, 5, 0, -20>'