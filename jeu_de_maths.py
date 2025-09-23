import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTION = 10


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 2)
    if o == 1:
        operator = "*"
        calcul = a * b
    elif o == 0:
        operator = "+"
        calcul = a + b
    else:
        operator = "-"
        calcul = a - b
    reponse = input(f"Calculez : {a} {operator} {b} = ")
    if int(reponse) == calcul:
        return True
    return False


nb_points = 0
for i in range(NB_QUESTION):
    print(f"Question n° {i+1} sur {NB_QUESTION}")
    if poser_question():
        print("Réponse Correcte !\n")
        nb_points += 1
    else:
        print("Réponse Incorrecte !\n")
    

print(f"Votre score est {nb_points}/{NB_QUESTION}")

if nb_points == NB_QUESTION:
    print("Excellent !")
elif nb_points == 0:
    print("Révesez vos maths !")

elif nb_points > NB_QUESTION // 2:
    print("Pas mal !")
else:
    print("Peut mieux faire")

    