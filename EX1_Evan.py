def factorielle(n):
    if n == 0:
        return 1
    return factorielle(n-1)*n

assert factorielle(5) == 120
assert factorielle(23) == 25852016738884976640000


def nb_occurrences_v1(tab,n):
    nb = 0
    if len(tab) == 0:
        return 0
    if tab[0] == n:
        nb = 1
    return nb + nb_occurrences_v1(tab[1:],n)

assert nb_occurrences_v1([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 1) == 4
assert nb_occurrences_v1([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 4) == 0


def nb_occurrences_v2(tab,n,k=0):
    nb = 0
    if len(tab)-k == 0:
        return 0
    if tab[k] == n:
        nb = 1
    return nb + nb_occurrences_v2(tab,n,k+1)

assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 3, 0) == 3
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 3, 1) == 3
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 3, 2) == 2
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 3, 6) == 2
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 3, 7) == 1
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 1) == 4
assert nb_occurrences_v2([1, 3, 0, 2, 1, 1, 3, 2, 0, 0, 1, 3], 4) == 0


def maximum_v1(tab):
    maxi = tab[0]
    if len(tab) == 1:
        return maxi
    if maximum_v1(tab[1:]) > maxi:
        maxi = maximum_v1(tab[1:])
    return maxi

assert maximum_v1([5, -3, 2, 7, 0, 2, 1, 6]) == 7
assert maximum_v1([-4]) == -4


def maximum_v2(tab,k=0):
    maxi = tab[k]
    if len(tab)-k == 1:
        return maxi
    if maximum_v2(tab[1:],k) > maxi:
        maxi = maximum_v2(tab[1:],k)
    return maxi

assert maximum_v2([5, -3, 2, 7, 0, 2, 1, 6], 0) == 7
assert maximum_v2([5, -3, 2, 7, 0, 2, 1, 6], 2) == 7
assert maximum_v2([5, -3, 2, 7, 0, 2, 1, 6], 3) == 7
assert maximum_v2([5, -3, 2, 7, 0, 2, 1, 6], 4) == 6
assert maximum_v2([-2, -12, -5, -8]) == -2


def palindrome_v1(mot):
    if len(mot) == 1 or len(mot) == 0:
        return True
    if mot[0] == mot[-1] and palindrome_v1(mot[1:-1]):
        return True
    return False

assert palindrome_v1('kayak') == True
assert palindrome_v1('exemple') == False


def palindrome_v2(mot,n=0):
    if len(mot)-n*2 == 1 or len(mot)-n*2 == 0:
        return True
    if mot[n] == mot[-1-n] and palindrome_v2(mot[1+n:-1-n]):
        return True
    return False

assert palindrome_v2('maman', 0) == False
assert palindrome_v2('maman', 1) == True
assert palindrome_v2('kayak') == True
assert palindrome_v2('exemple') == False