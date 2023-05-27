# Dans ce fichier, je reprends le code du trieur de fichier moi meme pour reussir a le realiser.
from pathlib import Path
# definition d'un dictionnaire
donnees = {
    ".mp3" : "Musique",
    ".wav" : "Musique",
    ".flac" : "Musique",
    ".avi" : "Videos", 
    ".mp4" : "Videos", 
    ".gif" : "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg" : "Images",
    ".txt" : "Documents", 
    ".pptx" : "Documents", 
    ".csv" : "Documents", 
    ".xls" : "Documents", 
    ".odp" : "Documents", 
    ".pages" : "Documents",
}

#Recuperer le dossier a trier
dossier_a_trier = Path.home() / "Downloads" / "data"
#Recuperer les fichiers du dossier dans une liste par scan
fichiers = [f for f in dossier_a_trier.iterdir() if f.is_file()]
# Creer le dossier correspondant a l'extension du fichier
for f in fichiers:
    dossier_a_creer = dossier_a_trier / donnees.get(f.suffix,"Autres")
    dossier_a_creer.mkdir(exist_ok=True)
    f.rename(dossier_a_creer / f.name)
