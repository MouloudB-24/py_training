import sqlite3

# Etablit la connexion
connexion = sqlite3.connect("data/albums_copie.db")

#  creation de curseur / Executer les requetes sql
cursor = connexion.cursor()

cursor.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR);""")

cursor.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

cursor.execute("""INSERT INTO artiste (nom) VALUES ("Mickael Jackson")""")

cursor.execute("""INSERT INTO artiste (nom) VALUES ("Celine Dion")""")

cursor.execute("""INSERT INTO artiste (nom) VALUES ("Gims")""")

cursor.execute("""INSERT INTO artiste (nom) VALUES ("Idir")""")


cursor.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "MJ1", 1990)""")

cursor.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (2, "CD1", 1991)""")

cursor.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (2, "CD2", 1991)""")

cursor.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (3, "GM1", 1991)""")

cursor.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (4, "ID1", 1991)""")



# Faire le commit pour s'assurer que les modis sont bien été faites
connexion.commit()

# Fermer la connexion
connexion.close()