# EX 1

def pile_positive_v2(pile):
    pile_tampon = []
    new_pile = []
    while not len(pile) == 0:
        elt = pile.pop()
        if elt > 0:
            new_pile.append(elt)
        pile_tampon.append(elt)
    while len(pile_tampon) != 0:
        elt = pile_tampon.pop()
        pile.append(elt)
    return new_pile

def pile_positive_v4(pile):
    new_pile = []
    pile_tampon = pile_positive_v2(pile)
    new_pile = pile_positive_v2(pile_tampon)
    return new_pile

def pile_positive_v1(pile):
    new_pile = []
    pile_tampon = pile_positive_v2(pile)
    while not len(pile_tampon) == 0:
        new_pile.append(pile_tampon.pop())
    return new_pile

def pos(n):
    return n > 0

def pile_positive_v3(pile):
    return list(filter(pos,pile))


# EX 2

class Pile:
    """Classe implémentant la structure de données d'une pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booléen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'élément v au sommet de la pile.
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()
        
    
def bon_balisage(expression):
    pile = Pile()
    for balise in expression:
        if balise in ('(', '[', '{'):
            pile.empiler(balise)
        elif pile.est_vide():
            return False
        else:
            elt = pile.depiler()
            if elt == '(' and balise != ')':
                return False
            elif elt == '[' and balise != ']':
                return False
            elif elt == '{' and balise != '}':
                return False
    return pile.est_vide()


# EX 3

def oux_bit_par_bit(tab1, tab2):
    assert len(tab1) == len(tab2)
    bits = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            bits.append(0)
        else:
            bits.append(1)
    return bits


# EX 4

NUM_LETTRE = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,\
              'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,\
              'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in NUM_LETTRE:
            indice = (NUM_LETTRE[lettre]+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat