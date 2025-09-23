"""Pour cet exercice, vous allez créer un programme de conversion d'unités, qui sera capable de convertir des pouces (inch) en centimètres (cm), et vice-versa.



1 pouce = 2.54 cm

1 cm = 0.394 pouces



Exemple :

Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)



Voici comment votre programme doit se comporter :

1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

- fin du programme.



Nombres à virgule :

Nous avons vu comment manipuler des données numériques avec Python, notamment avec le type "int" qui concerne les nombres entiers (sans virgules).

Pour cet exercice, vous allez être amené à manipuler des nombres à virgule. Il s'agit du type "float".

Le principe du float est similaire à celui du int.

Pour utiliser un nombre à virgule, il faut utiliser le point (et non une virgule).

Exemples :

a = 5  # int

b = 5.2 # float

c = 5,2 # erreur : ne pas utiliser de virgule, mais le point



Optionnel :

Boucler pour convertir plusieurs valeurs (en conservant toujours le même sens de conversion), et proposer une option pour sortir du programme.



Votre réponse :

Codez avec l'éditeur de votre choix, puis faites un copier/coller de votre code directement dans le champ de la réponse.
    """

def choisir_option():
    print("""\nQuelle conversion souhaitez-vous faire : 
          - Saisir 1 pour convertir pouce vers cm 
          - Saisir 2 pour convertir cm vers pouce
          """)
    choix = 0
    while choix == 0:
        try:
            choix = int(input("Veuillez entrer option 1 ou 2 : "))
        except ValueError:
            print("Erreur : veuillez entrer une option valide !\n")
        else:
            if choix not in [1, 2]:
                print("Erreur : veuillez entrer option 1 ou 2\n")
                choix = 0
        
    return choix


def entrer_valeur():
    valeur_saisi = 0
    while valeur_saisi == 0:
        try:
            valeur_saisi = int(input("\nVeuillez entrer la valeur à convertir : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre\n")
    return valeur_saisi


def afficher_resultat():
    choix = choisir_option()
    valeur_saisi = entrer_valeur()
    if choix == 1:
        valeur_cm = valeur_saisi * 2.54
        print(f"\nRésultat : {valeur_saisi} pouces égal {valeur_cm} cm")
    else:
        valeur_pouce = valeur_saisi * 0.394
        print(f"\nRésultat : {valeur_saisi} cm égal {valeur_pouce} pouces")
    

while True:
    choix = ""
    while not choix in ["1", "2"]:
        print("""\n-------- Convertisseur des unités ------------
          1 - (Re)Commencer 
          2 - Quitter
          """)
        choix = input("Quel choix faites-vous : ")
    
    if choix == "2":
        break
    afficher_resultat()
    
        