#ex1
def fibonacci_v1(n):
    nb = None
    nb1 = 0
    nb2 = 1
    if n>2:
        for _ in range(n-2):
            nb = nb1 + nb2
            nb1 = nb2
            nb2 = nb
    elif n == 2:
        nb = nb2
    elif n == 1:
        nb = nb1
    else:
        print('Heu, le nombre que t\'a rentré n\'est pas dans l\'intervale [1;+∞[')
    return nb

def fibonacci_v2(n):
    if n<1:
        return None
    if n == 1:
        return [0]
    suite = [0,1]
    for _ in range(n-3):
        suite.append(suite[len(suite)-1] + suite[len(suite)-2])
    return suite

#ex2

def Syracuse(n):
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3*n+1)
        suite.append(n)
    return suite
        
def temps_vol(n):
    return len(Syracuse(n)-1)

def temps_vol_altitude(n):
    tps_de_vol = 0
    for hauteur in Syracuse(n):
        if hauteur < n:
            return tps_de_vol
        tps_de_vol += 1
    return None
        
def altitude_max(n):
    maxi = 0
    for hauteur in Syracuse(n):
        if hauteur > maxi:
            maxi = hauteur
    return maxi
        
        
        