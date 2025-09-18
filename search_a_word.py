
# Search for a given word in various folders
from pathlib import Path

folder = Path("/Users/mouloud/Documents")
word = "Python"

# Parcourez tous les fichiers dans le dossier
files_list = []
for file in folder.rglob("*.txt"):
    if file.is_file():
        with open(file, 'r') as f:
            content = f.read()
            if word in content:
                files_list.append(file)

print(len(files_list))

        




