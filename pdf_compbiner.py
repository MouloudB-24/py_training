from PyPDF2 import PdfWriter, PdfReader


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