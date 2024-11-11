# Ex 1

def agregation_dico_v1(dico1,dico2):
    dico = {}
    for cles1 in dico1:
        for cles2 in dico2:
            if cles1 == cles2:
                dico[cles2] = dico1[cles1] + dico2[cles2]
    for cles in dico:
        del dico1[cles]
        del dico2[cles]
    if dico1 != {}:
        for cles1 in dico1:
            dico[cles1] = dico1[cles1]
        for cles2 in dico2:
            dico[cles2] = dico2[cles2]
    return dico

'''def agregation_dico_v2(dico1,dico2):
    dico = {}
    keys1 = list(dico1.keys())
    keys2 = list(dico2.keys())
    keys = keys1 + keys2
    keys = set(keys)
    for cle in keys:
        
    return keys'''

def est_cyclique_v1(plan):
    exp = 'P1'
    for _ in range(len(plan)-1):
        dest = plan[exp]
        if dest == 'P1':
            return False
        exp = dest
    return True

# Ex 2

plan_a = {'P1': 'P5', 'P2': 'P6', 'P3': 'P4', 'P4': 'P3', 'P5': 'P2', 'P6': 'P1'}
assert est_cyclique_v1(plan_a) == False

plan_b = {'P1': 'P3', 'P2': 'P6', 'P3': 'P5', 'P4': 'P1', 'P5': 'P2', 'P6': 'P4'}
assert est_cyclique_v1(plan_b) == True

def est_cyclique_v2(plan):
    exp = 'P1'
    dest = ''
    compteur = 0
    while dest != 'P1':
        dest = plan[exp]
        exp = dest
        compteur += 1
    return compteur > len(plan)-1

plan_a = {'P1': 'P5', 'P2': 'P6', 'P3': 'P4', 'P4': 'P3', 'P5': 'P2', 'P6': 'P1'}
assert est_cyclique_v2(plan_a) == False

plan_b = {'P1': 'P3', 'P2': 'P6', 'P3': 'P5', 'P4': 'P1', 'P5': 'P2', 'P6': 'P4'}
assert est_cyclique_v2(plan_b) == True


# Ex 3

def select_date(mat,date):
    tab = []
    for reservation in mat:
        if reservation['date'] == date:
            dico = {'nom':reservation['nom'],'nb_pers':reservation['nb_pers'],'matin':reservation['matin']}
            tab.append(dico)
    return tab

reservations = [{'nom': 'Dupont', 'date': '2022-11-11', 'nb_pers': 2, 'matin': True},
{'nom': 'Dupont', 'date': '2022-11-12', 'nb_pers': 2, 'matin': True},
{'nom': 'Dupond', 'date': '2022-11-11', 'nb_pers': 3, 'matin': False},
{'nom': 'Toto', 'date': '2022-11-12', 'nb_pers': 1, 'matin': True}]
assert select_date(reservations, '2022-11-11') == [{'nom': 'Dupont', 'nb_pers': 2, 'matin': True}, {'nom': 'Dupond', 'nb_pers': 3, 'matin': False}]


reservations = [{'nom': 'Dupont', 'date': '2022-11-11', 'nb_pers': 2, 'matin': True},
{'nom': 'Dupont', 'date': '2022-11-12', 'nb_pers': 2, 'matin': True},
{'nom': 'Dupond', 'date': '2022-11-11', 'nb_pers': 3, 'matin': False},
{'nom': 'Toto', 'date': '2022-11-12', 'nb_pers': 1, 'matin': True}]
assert select_date(reservations, '2022-11-12') == [{'nom': 'Dupont', 'nb_pers': 2, 'matin': True}, {'nom': 'Toto', 'nb_pers': 1, 'matin': True}]

# Ex 4

from image import lire_image, construire_image

def hauteur(image):
    return len(image)

def lomgueur(image):
    return len(image[0])

def agrandir_ligne(ligne,k):
    nw_ligne = []
    for px in ligne:
        for i in range(k):
            nw_ligne.append(px)
    return nw_ligne

def agrandir_image(image,k):
    nw_image =[]
    for ligne in image:
        nw_ligne = agrandir_ligne(ligne,k)
        for i in range(k):
            nw_image.append(nw_ligne)
    return nw_image

def negatif(image):
    nw_image = []
    for ligne in image:
        nw_ligne = []
        for px in ligne:
            nw_ligne.append(255 - px)
        nw_image.append(nw_ligne)
    return nw_image

def noir_et_blanc(image,k):
    nw_image = []
    for ligne in image:
        nw_ligne = []
        for px in ligne:
            if px >= k:
                nw_ligne.append(1)
            else:
                nw_ligne.append(0)
        nw_image.append(nw_ligne)
    return nw_image



nsi = lire_image('nsi.png')
construire_image(agrandir_image(negatif(nsi), 100), 'gris')
