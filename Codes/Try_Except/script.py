chemin = input("Veuillez saisir le chemin vers le fichier a lire : ")

try:
    with open(chemin,"r") as f:
        contenu = f.read()
        print(contenu)
except UnicodeDecodeError:
    print("Le fichier est impossible a ouvrir")
except FileNotFoundError:
    print("Le fichier est introuvable")