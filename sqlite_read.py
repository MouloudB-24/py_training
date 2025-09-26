# Lire les données d'un base de données sqlite3
import sqlite3


connexion = sqlite3.connect("data/albums_copie.db")


cursor = connexion.cursor()


donnees = cursor.execute("SELECT nom, titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id").fetchall()

for donnee in donnees:
    print(donnee[0],":", donnee[1])

connexion.close()