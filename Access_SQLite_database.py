import sqlite3
import pandas as pd

# --- Create Connection object ---
conn = sqlite3.connect("INSTRUCTOR.db")

# --- Create Cursor object ---
cursor = conn.cursor()

# --- Run Queries ---
# Create table
cursor.execute("DROP TABLE IF EXISTS instructor")
table = """CREATE TABLE IF NOT EXISTS instructor(
                            ID INTEGER PRIMARY KEY NOT NULL,
                            FNAME VARCHAR(20),
                            LNAME VARCHAR(20),
                            CITY VARCHAR(20),
                            CCODE CHAR(2));"""
cursor.execute(table)
print("Table is ready")

# Insert data
cursor.execute("""INSERT INTO instructor VALUES
                    (2, 'Raul', 'Chong', 'Markham', 'CA'),
                    (3, 'Aylan', 'Vasudevan', 'Paris', 'US'),
                    (4, 'Hima', 'Vasudevan', 'Chicago', 'US'),
                    (5, 'Mily', 'Vasudevan', 'Paris', 'US')""")

# Retreive data
sql_statement = "SELECT * FROM instructor"
cursor.execute(sql_statement)
result = cursor.fetchall()
for row in result:
    print(row)
    
update_query = "UPDATE instructor SET CCODE='FR' WHERE ID=3 OR ID=5"
cursor.execute(update_query)
cursor.execute(sql_statement)
result = cursor.fetchall()
for row in result:
    print(row)

# Retreive data into pandas
df = pd.read_sql_query(sql_statement, conn)
print(df)

# --- Free ressources ---
conn.close()