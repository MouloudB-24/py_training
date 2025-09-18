
while True:
    print("Veuillez faire un choix de conversion d'unité:\n"
          "1: pouces vers cm\n"
          "2: cm vers pouces")

    choix = input("\nEntrez votre choix : ")

    if choix in ["1", "2"]:
        valeur = float(input("Veuillez entrer la valeur à convertir :"))
        break

if choix == "1":
    valeur_convertir = valeur * 2.54
    print(f"{valeur} pouces égale {valeur_convertir} cm.")
else:
    valeur_convertir = valeur * 0.394
    print(f"{valeur} cm égale {valeur_convertir} pouces.")
