def moyenne_v1(tab):
    n = 0
    for val in tab:
        n += val
    n /= len(tab)
    return n

def moyenne_v2(tab):
    n = 0
    f = 0
    for i in range(len(tab)):
        for j in range(tab[i][1]):
            n += tab[i][0]
            f += 1
    n /= f
    return n

def moyenne_v3(tab1,tab2):
    n = 0
    f = 0
    for i in range(len(tab1)):
        for j in range(tab2[i]):
            n += tab1[i]
            f += 1
    n /= f
    return n

def moyenne_v4(classe):
    dico = {}
    for nom in classe:
        n = 0
        f = 0
        for val in classe[nom]:
            n = n + classe[nom][val]
            f += 1
        n = round(n/f,1)
        dico[nom] = n
    return dico

def moyenne_v5(classe):
    
            
            
            
            
            
