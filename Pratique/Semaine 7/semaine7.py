# Ex 1

def tri_bulles(tab):
    n = 0
    for _ in range(len(tab)):
        for i in range(1,len(tab)-n):
            if tab[i-1] > tab[i]:
                tab[i],tab[i-1] = tab[i-1],tab[i]
        n += 1
    return tab

# Ex 2
def comptage_valeurs(n,tab1):
    tab = []
    m = 0
    for i in range(n+1):
        for j in range(len(tab1)):
            if tab1[j] == i:
                m += 1
        tab.append(m)
        m = 0
    return tab

def tri_comptage(n,tab1):
    tab = comptage_valeurs(n,tab1)
    tab2 = []
    for i in range(n+1):
        for j in range(tab[i]):
            tab2.append(i)
    return tab2

# Ex 3

def tri_01(tab):
    i = len(tab)
    nb0 = 0
    nb1 = 0
    while i != 0:
        if tab[nb0] == 1:
            tab.append(1)
            tab.pop(nb0)
            nb1 += 1
        else:
            nb0 += 1
        i -= 1
    return tab

# Ex 4

def 