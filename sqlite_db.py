import sqlite3

conn = sqlite3.connect("data/database.db")

c = conn.cursor()


# Création de la table
c.execute("""CREATE TABLE IF NOT EXISTS employees (
            prenom text,
            nom text,
            salaire INTEGER)""")

# Inserer les donnes dans la table
d = {"prenom": "Victor", "nom": "Biz", "salaire": 1000}
c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

d = {"prenom": "Youssef", "nom": "Toto", "salaire": 2000}
c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

d = {"prenom": "Nicolas", "nom": "Sar", "salaire": 5000}
c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

# Récupérer et afficher les donnes depuis la table
donnees = c.execute("SELECT * FROM employees WHERE prenom='Victor'").fetchall()
print(donnees)

# Mettre à jour les données de la table
c.execute("UPDATE employees SET salaire=100 WHERE prenom='Victor'")

donnees = c.execute("SELECT * FROM employees WHERE prenom='Victor'").fetchall()
print(donnees)

conn.commit()

conn.close()