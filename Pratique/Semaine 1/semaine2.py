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
        return 'Heu, le nombre que t\'a rentré n\'est pas dans l\'intervale [1;+∞['
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

def tests_fibonacci():
    assert fibonacci_v1(1) == 0, 'le premier terme n\'est défini comme 0'
    assert fibonacci_v1(2) == 1, 'le deuxieme terme n\'est défini comme 1'
    assert fibonacci_v1(10) == 34, 'fibonacci_v1 de 10 devrait être = 34'
    assert fibonacci_v1(-10) == 'Heu, le nombre que t\'a rentré n\'est pas dans l\'intervale [1;+∞['
    
    assert fibonacci_v2(1) == [0], 'le premier terme n\'est défini comme 0'
    assert fibonacci_v2(2) == [0,1], 'le premier terme n\'est défini comme 0 et/ou le deuxieme terme n\'est défini comme 1'
    assert fibonacci_v2(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21], 'fibonacci_v2 de 10 devrait être = [0, 1, 1, 2, 3, 5, 8, 13, 21]'
    assert fibonacci_v2(-10) == None, 'fibonacci d\'un nb devrait être = None'
    


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
    if n <= 0:
        return None
    return len(Syracuse(n))-1

def temps_vol_altitude(n):
    if n <= 0:
        return None
    tps_de_vol = 0
    for hauteur in Syracuse(n):
        if hauteur < n:
            return tps_de_vol
        tps_de_vol += 1
    return None
        
def altitude_max(n):
    if n <= 0:
        return None
    maxi = 0
    for hauteur in Syracuse(n):
        if hauteur > maxi:
            maxi = hauteur
    return maxi
        
def tests_syracuse():
    assert temps_vol(6) == 8
    assert temps_vol_altitude(6) == 1
    assert altitude_max(6) == 16
    assert temps_vol(-1) == None
    assert temps_vol_altitude(-1) == None
    assert altitude_max(-1) == None
    
def tests():
    tests_syracuse()
    tests_fibonacci()