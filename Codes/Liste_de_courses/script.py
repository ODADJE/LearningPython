import sys
import os
import json

chemin_fichier = os.path.join(os.path.dirname(__file__),"liste.json")
course_liste = []
with open(chemin_fichier, "r") as f:
    course_liste.extend(json.load(f))
while True:
    print("_____________________________________________")
    print("Choisissez parmi les 5 options suivantes : ")
    print("1: Ajouter un element a la liste.")
    print("2: Retirer un element a la liste.")
    print("3: Afficher la liste.")
    print("4: Vider la liste.")
    print("5: Quitter.")

    print("Veuillez faire un choix entre 1 et 5.")
    choix_menu = input("> Votre choix : ")
    if not (choix_menu.isdigit() and 1 <= int(choix_menu) <= 5):
        continue

    if choix_menu == "1":
        element_de_liste = input("> Veuillez saisir l'element a ajouter : ")
        course_liste.append(element_de_liste)
        print(f"l'element {element_de_liste} a ete bien ajoute a la liste de course.")

    elif choix_menu == "2":
        element_de_liste = input("> Veuillez saisir l'element a supprimer : ")
        if element_de_liste in course_liste:
            course_liste.remove(element_de_liste)
            print(f"l'element {element_de_liste} a ete bien retire a la liste de course.")
        else:
            print(f"L'element {element_de_liste} ne se trouve pas dans la liste de course ou la liste est vide.")

    elif choix_menu == "3":
        if course_liste:
            for i, element in enumerate(course_liste,1):
                print(f"{i}. {element}")
        else:
            print("La liste de course est vide.")

    elif choix_menu == "4":
        course_liste.clear()
        print("la liste de course a ete videe.")

    elif choix_menu == "5":
        with open(chemin_fichier, "w") as f:
            json.dump(course_liste,f,indent=4)
        sys.exit()