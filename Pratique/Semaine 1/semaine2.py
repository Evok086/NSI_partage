nb1 = 0
nb2 = 1

def fibonacci_v1(n):
    nb = 'Heu, le nombre que t\'a rentré n\'est pas dans l\'intervale [1;+∞['
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
    return nb

def fibonacci_v2(n):
    nb1 = 0
    nb2 = 1
    suite = [0]
    if n>2:
        suite.append(nb2)
        for _ in range(n-2):
            suite.append(nb1+nb2)
            nb1 = nb2
            nb2 = nb1 + nb2
    elif n == 2:
        suite.append(nb2)
    elif n<1:
        return None
    return suite
        