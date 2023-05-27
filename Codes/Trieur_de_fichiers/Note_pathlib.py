from pathlib import Path

# Avoir le chemin du home
# Ex: /home/odadje
dossier_utilisateur = Path.home() # /home/odadje 

# Recuperer le dossier courant
dossier_courant = Path.cwd()

# Creation de chemin specifique
chemin_specifique = Path("/home/odadje/Documents")

# Si on affiche l'objet créé à partir de la classe Path, on se retrouve avec un objet PosixPath.
# Cet objet représente les chemins des systèmes Linux et Mac OS.

# On peut concatener un chemin
home = Path.home()  # PosixPath('/home/odadje/')
documents = home / "Documents"  # PosixPath('/home/odadje/Documents')

home = Path.home()  # PosixPath('/home/odadje/')
documents = home / "Documents" / "source_code"  # PosixPath('/home/odadje/Documents/source_code')
# On peut également utiliser la méthode **joinpath** sur un objet Path.
# Pour la concatenation
home = Path.home()  # PosixPath('/home/odadje/')
dossiers = ['Projets', 'Django', 'blog']
home.joinpath(*dossiers)  # PosixPath('/home/odadje/Projets/Django/blog')

### RECUPERATION DES INFORMATIONS SUR UN CHEMIN

p = Path("/Users/thibh/Documents/index.html")
p.name    # "index.html"
p.parent  # "/home/odadje/Documents"
p.stem    # "index"
p.suffix  # ".html"
p.parts   # ("/", "home", "odadje", "documents", "index.html")

# Pour verifier l'existence et le type d'un chemin
p = Path("/Users/thibh/Documents/index.html")
p.exists()   # True -> Si le chemin existe
p.is_dir()   # False -> Si le chemin est de type dossier
p.is_file()  # True -> Si le chemin est de type fichier

### CREATION ET SUPPRESSION DE DOSSIERS

# Creation 
dossier = Path("/home/odadje/Documents/SiteWeb")
dossier.mkdir()  # Lève une erreur si le dossier existe déjà
dossier.mkdir(exist_ok=True)

# Le dossier SiteWeb et ses sous-dossiers n'existent pas
dossier = Path("/home/odadje/Documents/SiteWeb/sources/css")
# On peut tout créer d'un coup avec le paramètre parents
dossier.mkdir(parents=True)

# Supression
dossier = Path("/Users/thibh/Documents/SiteWeb")
dossier.rmdir() # Ne marche que lorsque le dossier est vide

# Si le dossier contient des fichiers ou d'autres sous-dossiers, cette méthode ne fonctionnera pas, et c'est le seul cas de figure où nous sommes obligés de repasser par le module shutil et la fonction rmtree
import shutil # On importe d'abord shutil
dossier = Path("/Users/thibh/Documents/SiteWeb")
shutil.rmtree(dossier)

# Créer, lire et écrire dans un fichier
fichier = Path.home() / "Documents" / "SiteWeb" / "index.html"
fichier.touch() # On cree le fichier
fichier.unlink() # On supprime le fichier

fichier.write_text("Acceuil du site") #Ecrire dans un fichier

# Scanner un dossier le contenu d'un dossier et recuperer

for f in Path.home().iterdir():
    print(f.name)

dossiers = [d for d in Path.home().iterdir() if d.is_dir()] #Recuperer les dossier

# on pegalement utiliser la methode ** glob **
for f in Path.home().glob("*.png"):
    print(f.name)
#Scan recursif 
for f in Path.home().rglob("*.png"):
    print(f.name)
# On peut utiliser la méthode ** rename ** pour déplacer un fichier
chemin_source = "/home/odadje/Documents/index.html"
chemin_destination = "/home/odadje/Documents/SiteWeb/index.html"
chemin_source.rename(chemin_destination)