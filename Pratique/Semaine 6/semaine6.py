#Ex1:
def compression_delta(tab):
    tab1 = [tab[0]]
    for i in range(1,len(tab)):
        tab1.append(tab[i]-tab[i-1])
    return tab1