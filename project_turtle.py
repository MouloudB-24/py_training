import turtle

def escalier(taille, n_marche):
    for _ in range(n_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10

    t.forward(30)
    

def carre(taille):
    for _ in range(4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nb_carres):
    for i in range(nb_carres):
        taille = taille_depart * (i + 1)
        carre(taille)


t = turtle.Turtle()

#escalier(50, 5)
carres(10, 20)

turtle.done()





