from pathlib import Path

data = {
    ".mp3" : "Musiques",
    ".mp4" : "Videos",
    ".jpg" : "Images",
    ".png" : "Images",
    ".zip" : "archive",
}

dossier_a_trier = Path.home() / "Downloads"
fichiers = [f for f in dossier_a_trier.iterdir() if f.is_file()]

for f in fichiers:
    dossier = dossier_a_trier / data.get(f.suffix, "Autres")
    if not dossier.exists(): 
        # dossier.mkdir(exist_ok=True) : ce code peut remplacer toute la condition
        dossier.mkdir()
    f.rename(dossier / f.name)