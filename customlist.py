class CustomList(list):

    def __init__(self, *args):
        self.valeurs = list(args)

    def append(self, element):
        if isinstance(element, int):
            return print("Tu ne peux pas ajouter des nombre à la liste")
        elif isinstance(element, list):
            self.valeurs.extend(element)
        elif element in self.valeurs:
            return
        else:
            self.valeurs.append(element)

ma_liste = CustomList("Pierre", "Aylan", "Marie")
ma_liste.append(5)
ma_liste.append("Aylan")
print(ma_liste.valeurs)