def afficher_file(file):
    if file.est_vide():
        ligne = '<-  '
    else:
        ligne = '<- | '
        tab = []
        while not file.est_vide():
            elt = file.defiler()
            tab.append(elt)
            ligne += str(elt) + ' | '
        for val in tab:
            file.enfiler(val)
    ligne = '  '+(len(ligne)-2)*'-' + '\n' + ligne + '\n  ' + (len(ligne)-2)*'-'
    print(ligne)

## Exercice 4 :

class File_tab:
    def __init__(self, taille):
        self.tab = [None] * taille
        self.indice = 0
        self.nb_elts = 0

    def est_vide(self):
        return self.nb_elts == 0

    def enfiler(self, element):
        assert self.nb_elts < len(self.tab), 'La file est pleine'
        self.nb_elts += 1
        self.tab[(self.indice + self.nb_elts - 1) % len(self.tab)] = element
            

    def avant(self):
        return self.tab[self.indice]

    def defiler(self):
        n = self.tab[self.indice%len(self.tab)]
        self.tab[self.indice%len(self.tab)] = None
        self.indice += 1
        self.indice %= len(self.tab)
        self.nb_elts -= 1
        return n

#ma_file = File_tab(4)
#afficher_file(ma_file)
#ma_file.est_vide()
#ma_file.enfiler(-4)
#ma_file.enfiler(3)
#ma_file.enfiler(0)
#afficher_file(ma_file)
#ma_file.enfiler(5)
#ma_file.est_vide()
#ma_file.avant()
#ma_file.defiler()
#afficher_file(ma_file)
#ma_file.enfiler(-1)
#ma_file.avant()
#ma_file.defiler()
#afficher_file(ma_file)

## Exercice 5 :

class Maillon:
    def __init__(self, element):
        self.suivant = None
        self.contenu = element

class File_chainee:
    def __init__(self):
        self.maillon_avant = None
        self.maillon_arriere = None

    def est_vide(self):
        return self.maillon_avant == None

    def enfiler(self, element):
        maillon = Maillon(element)
        if self.est_vide() == True:
            self.maillon_avant = maillon
        else:
            self.maillon_arriere.suivant = maillon
        self.maillon_arriere = maillon
            
    def avant(self):
        return self.maillon_avant.contenu

    def defiler(self):
        n = self.maillon_avant.contenu
        self.maillon_avant = self.maillon_avant.suivant
        return n
    
#ma_file = File_chainee()
#afficher_file(ma_file)
#ma_file.est_vide()
#ma_file.enfiler(-4)
#ma_file.enfiler(3)
#ma_file.enfiler(0)
#afficher_file(ma_file)
#ma_file.enfiler(5)
#ma_file.est_vide()
#ma_file.avant()
#ma_file.defiler()
#afficher_file(ma_file)
#ma_file.enfiler(-1)
#ma_file.avant()
#ma_file.defiler()
#afficher_file(ma_file)

## Exercice 6 :

class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return len(self.contenu) == 0

    def empiler(self, element):
        self.contenu.append(element)

    def sommet(self):
        return self.contenu[-1]

    def depiler(self):
        return self.contenu.pop()

class File_via_pile:
    def __init__(self):
        self.pile_arriere = Pile()
        self.pile_avant = Pile()

    def est_vide(self):
        return self.pile_avant.est_vide() and self.pile_arriere.est_vide()

    def enfiler(self, element):
        self.pile_arriere.empiler(element)

    def _transvasement(self):
        assert self.pile_avant.est_vide(), "Le transvasement ne s'effectue que si la pile avant est vide"
        while not self.pile_arriere.est_vide() :
            self.pile_avant.empiler(self.pile_arriere.sommet())
            self.pile_arriere.depiler()

    def avant(self):
        if self.pile_avant.est_vide():
            self._transvasement()
        return self.pile_avant.sommet()

    def defiler(self):
        if self.pile_avant.est_vide():
            self._transvasement()
        return self.pile_avant.depiler()
        
ma_file = File_via_pile()
afficher_file(ma_file)
ma_file.est_vide()
ma_file.enfiler(-4)
ma_file.enfiler(3)
ma_file.enfiler(0)
afficher_file(ma_file)
ma_file.enfiler(5)
ma_file.est_vide()
ma_file.avant()
ma_file.defiler()
afficher_file(ma_file)
ma_file.enfiler(-1)
ma_file.avant()
ma_file.defiler()
afficher_file(ma_file)
