from PIL import Image

def lire_image(nom_fichier):
    '''
    convertit l'image donnée en une matrice de pixels en niveau de gris
    et la renvoie
    '''
    image = Image.open(nom_fichier)
    nb_col, nb_lig = image.size
    pixels = image.load()
    if type(pixels[0,0]) == int:
        mat = [[pixels[j,i] for j in range(nb_col)] for i in range(nb_lig)]
    else:
        mat = [[(pixels[j,i][0]+pixels[j,i][1]+pixels[j,i][2])//3
                    for j in range(nb_col)] for i in range(nb_lig)]
    return mat

def construire_image(mat, mode):
    '''
    constuit et remvoie l'image donnée sous forme d'une matrice de pixels et
    l'affiche
    mode possible :
    - mode='gris' pour une image en niveau de gris
    - mode='noir&blanc' pour une image en noir et blanc
    '''
    nb_lig, nb_col = len(mat), len(mat[0])
    if mode == 'noir&blanc':
        image = Image.new('1', (nb_col, nb_lig))
    elif mode == 'gris':
        image = Image.new('L', (nb_col, nb_lig))
    else:
        return None
    pixels = image.load()
    for i in range(nb_lig):
        for j in range(nb_col):
            pixels[j,i] = mat[i][j]
    image.show()
    return image