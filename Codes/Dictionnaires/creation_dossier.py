from pathlib import Path

chemin = "/home/odadje/Documents/Python/Codes/Dictionnaires/dossier_projet_creation"
 
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

BASE_DIR = Path(chemin)
for dossier_principal,dossier in d.items():
    for dossier_second in dossier:
        chemin_a_creer = BASE_DIR / dossier_principal / dossier_second
        chemin_a_creer.mkdir(exist_ok=True, parents=True)