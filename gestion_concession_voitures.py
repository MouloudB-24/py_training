# Gestion d'une Concession Automobile
class Voiture:
    def __init__(self, marque: str, model: str, prix: float, km: int=0):
        self.marque = marque
        self.model = model
        self.prix = prix
        self.km = km
    
    def __str__(self):
        return f"{self.marque} {self.model}"
    
    def afficher_info(self):
        print(f"Marque: {self.marque}")
        print(f"Model : {self.model}")
        print(f"Prix : {self.prix}$")
        print(f"Kilométrage : {self.km} Km")


class VoitureElectrique(Voiture):
    def __init__(self,  marque: str, model: str, prix: float, autonomie: int, km: int=0):
        super().__init__(marque, model, prix, km)
        self.autonomie = autonomie
    
    def afficher_info(self):
        super().afficher_info()
        print(f"Autonomie : {self.autonomie} Km")


class Concession:
    def __init__(self, nom):
        self.nom = nom
        self.inventaire = []
    
    def __str__(self):
        return f"{self.nom} {len(self.inventaire)} voitures disponibles"
    
    def ajouter_voiture(self, voiture):
        if isinstance(voiture, (Voiture, VoitureElectrique)):
            self.inventaire.append(voiture)
        else:
            print("L'objet fourni n'est pas une instance de Voiture ou VoitureElectrique")
    
    def vendre_voiture(self, marque: str, model: str):
        for voiture in self.inventaire:
            vendue = False
            if marque == voiture.marque and model == voiture.model:
                self.inventaire.remove(voiture)
                vendue = True
        if vendue:
            print(f"La voiture {marque} {model} a été vendue")
        else:
            print(f"La voiture {marque} {model} n'a pas été trouvée")
    
    def afficher_inventaire(self):
        print(f"{self.nom} voitures disponibles :")
        for voiture in self.inventaire:
            voiture.afficher_info()
            print()
    
    def calculer_valeur_inventaire_voiture(self):
        valeur_inventaire = 0
        for voiture in self.inventaire:
            valeur_inventaire += voiture.prix
        return valeur_inventaire


# Tests
concession = Concession("Concession du Centre")
voiture1 = Voiture("BMW", "X5", 35000, 10000)
voiture2 = Voiture("Peugeot", "308", 15000, 100)
voiture_elec1 = VoitureElectrique("Renault", "Zoe", 20000, 200)
concession.ajouter_voiture(voiture1)
concession.ajouter_voiture(voiture2)
concession.ajouter_voiture(voiture_elec1)

concession.afficher_inventaire()

concession.vendre_voiture("Peugeot", "308")
concession.vendre_voiture("Peugeot", "208")
print()
print(concession)
print(f"Valeur inventaire : {concession.calculer_valeur_inventaire_voiture()} Euros")
