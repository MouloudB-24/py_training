from pprint import pprint
from PyPDF2 import PdfWriter, PdfReader

# PDF - Combiner des fichiers .pdf

# Créer un contenu pdf vide en mémoire
contenu_sortie = PdfWriter()


# Ouvrir les fichier PDF à combiner et ajouter leurs contenu dans le contenu_sortie
with open("data/presentation.pdf", "rb") as f:
    reader_presentation = PdfReader(f)
    contenu_sortie.add_page(reader_presentation.pages[0])


with open("data/recap.pdf", "rb") as f:
    reader_recap = PdfReader(f)
    for page in reader_recap.pages:
        contenu_sortie.add_page(page)


# Ecire le pdf combiné
with open("data/pdf_combiner.pdf", "wb") as f:
    contenu_sortie.write(f)
    

# PDF - Extraction du texte
with open("data/recap.pdf", "rb") as f:
    reader_pdf = PdfReader(f)
    texte = ""
    for num_page, contenu_page in enumerate(reader_pdf.pages, start=1):
        contenu_texte = contenu_page.extract_text()
        if contenu_texte: # Evite les pages vide
            texte += f"\n------- Page {num_page} ------\n"
            texte += contenu_texte.strip() + "\n"


print(texte)
