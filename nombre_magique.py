import random

NOMBRE_MAX = 10
NOMBRE_MIN = 1
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4


def demander_nombre(nb_min, nb_max):
    nombre_saisi = 0
    while nombre_saisi == 0:
        try:
            nombre_saisi = int(input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) : "))
        except ValueError:
            print("Erreur : Vous devez entrer un nombre, Réessayez !\n")
        else:
            if not 1 <= nombre_saisi <= 10:
                print(f"Erreur : Le nombre doit être compris en {nb_min} et {nb_max}. Réessayez !\n")
                nombre_saisi = 0
    return nombre_saisi


vies = NB_VIES

while True:
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    
    if vies == 0:
        print(f"Dommage, Vous avez perdu ! Le nombre magique était {NOMBRE_MAGIQUE}")
        break
    print(f"Il vous reste {vies} vies")
    
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné !")
        break
    elif nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand !\n")
    else:
        print("Le nombre magique est plus petit !\n")
    vies -= 1