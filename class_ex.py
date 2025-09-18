class Voiture(object):
	def __init__(self, marque, prix, couleur):
		self.marque = marque
		self.prix = prix
		self.couleur = couleur
		
	@classmethod 
	def lamborghini(cls):
		return cls("Lamborghini", 150000, "rouge")
	@classmethod
	def porsche(cls):
		return cls("Porsche", 200000, "noire")
	@property
	def prix_euros(self):
		prix_euros = self.prix * 1.5
		return round(prix_euros)
	
		

lamborghini = Voiture.lamborghini()
print(lamborghini.prix)
print(lamborghini.prix_euros)
porsche = Voiture.porsche()
print(porsche.prix)
