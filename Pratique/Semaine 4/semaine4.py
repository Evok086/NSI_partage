#1
def extremum_v1(tab):
    maxi =  tab[0]
    for i in range(len(tab)):
        if tab[i]>maxi:
            maxi = tab[i]
    return maxi

def extremum_v2(tab):
    maxi =  tab[0]
    n = 0
    for i in range(len(tab)):
        if tab[i]>maxi:
            maxi = tab[i]
            n = i
    return n

def extremum_v3(tab):
    maxi =  tab[0]
    n = 0
    for i in range(len(tab)):
        if tab[i]>maxi:
            maxi = tab[i]
            n = i
        elif tab[i] == maxi:
            n = i
    return (n,maxi)
    
def extremum_v4(tab):
    mini =  tab[0]
    n = []
    for i in range(len(tab)):
        if tab[i]<mini:
            mini = tab[i]
            n = [i]
        elif tab[i] == mini:
            n.append(i)
    return (mini,n)
    
def extremum_v5(tab):
    dico = {'maximum':None,'minimum':None}
    maxi =  tab[0]
    mini =  tab[0]
    for i in range(len(tab)):
        if tab[i]>maxi:
            maxi = tab[i]
        if tab[i]<mini:
            mini = tab[i]
    dico['maximum'] = maxi
    dico['minimum'] = mini
    return dico
    
#2
def dépouiller(urne):
    dép = {}
    for i in range(len(urne)):
        if urne[i] not in dép:
            dép[urne[i]] = 1
        else:
            dép[urne[i]] += 1
    return dép

def maximum_voix(voix):
    maxi = voix[0]
    gens = []
    for i in range(len(voix)):
        if voix[i]>maxi:
            maxi = voix[i]
            gens.append(voix[])
        
        