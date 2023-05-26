from random import randint

nombre_de_vie_joueur = nombre_de_vie_ennemi = 50
nombre_de_potion = 3

while nombre_de_vie_joueur > 0 and nombre_de_vie_ennemi > 0:
    choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    if not (choix_joueur.isdigit() and 1 <= int(choix_joueur) <= 2):
        print("Veuillez choisir entre l'option (1) et (2)! ")
        continue

    choix_joueur = int(choix_joueur)

    if choix_joueur == 1:
        nombre_de_vie_ennemi -= randint(5,10)
        if nombre_de_vie_ennemi <= 0:
            break
        nombre_de_vie_joueur -= randint(5,15)
    else:
        if nombre_de_potion > 0:
            nombre_de_potion -= 1
            nombre_de_vie_ajouter = randint(15,50)
            nombre_de_vie_joueur += nombre_de_vie_ajouter
            print(f"Vous avez recu ({nombre_de_vie_ajouter}) nombre de vie")
            print(f"Il vous reste ({nombre_de_potion}) potion{'s' if nombre_de_potion > 1 else ''}.")
            nombre_de_vie_joueur -= randint(5,15)
        else:
            print("Vous disposez de (0) potion.")
            continue
    
    print(f"Il vous reste ({nombre_de_vie_joueur}) nombre de vie")
    print(f"Il reste a votre ennemi ({nombre_de_vie_ennemi}) nombre de vie")

#test du vainqueur
if (nombre_de_vie_joueur > 0):
    print("Vous avez combattu avec bravoure. BRAVO!!!".upper())
    print(f"Il vous reste ({nombre_de_vie_joueur}) nombre de vie")
else:
    print("La prochaine fois sera votre chance.".upper())
    print(f"Il reste a votre ennemi ({nombre_de_vie_ennemi}) nombre de vie")