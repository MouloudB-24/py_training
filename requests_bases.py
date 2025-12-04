# FAIRE DES APPEL RESEAUU AVEC REQUESTS

# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html


import requests
import json

# Requetes pour récupérer du texte 
response = requests.get("https://codeavecjonathan.com/res/pizzas1.json")
if response.status_code == 200:
    response.encoding = "utf-8"
    pizzas = json.loads(response.text)
    
    print("Nombre de pizza :", type(pizzas))
else:
    print(f"Erreur code : {response.status_code}")
    

# Requete pour récupérer une image

response = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
if response.status_code == 200:
    with open("data/papillon.jpg", "wb") as f:
        f.write(response.content)
        print("Ecriture terminée")
    
