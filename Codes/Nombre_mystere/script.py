from random import randint

volonte = "o"
start = 0
end = 100

while volonte == "o":

    nombre_de_chance = 5
    nombre_mystere = randint(start,end)
    i = 1
    while  nombre_de_chance > 0:

        print(f"Il vous reste {nombre_de_chance} chance")
        nombre_saisi = input(f"Veuillez saisir votre nombre mystere entre {start} et {end} : ")

        if not nombre_saisi.isdigit():
            continue

        nombre_saisi = int(nombre_saisi)

        if nombre_saisi == nombre_mystere:
            print("Bien joue!!!")
            print(f"Le nombre mystere est bien {nombre_saisi}")
            print(f"Tu a reussi en {i} coup(s)")
            break
        elif (nombre_saisi > nombre_mystere):
            print(f"Le nombre mystere est plus petit que {nombre_saisi}")
        elif (nombre_saisi < nombre_mystere):
            print(f"Le nombre mystere est plus grand que {nombre_saisi}")

        nombre_de_chance -= 1
        i += 1

    if nombre_de_chance == 0:
        print(f"Essaie une prochane fois! Le nombre mystere etait {nombre_mystere}")
    volonte = input("Voulez-vous continer? o/n : ")

print("Fin du jeu.")

