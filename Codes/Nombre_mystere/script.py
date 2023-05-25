import random

volonte = "o"
start = 0
end = 4

while volonte == "o":

    nombre_de_chance = 3
    nombre_mystere = random.randint(start,end)
    
    while  nombre_de_chance > 0:
        print(f"Il vous reste {nombre_de_chance} chance")
        nombre_saisi = input(f"Veuillez saisir votre nombre mystere entre {start} et {end} : ")
        if not nombre_saisi.isdigit():
            continue
        nombre_saisi = int(nombre_saisi)
        if nombre_saisi == nombre_mystere:
            print("Bien joue!!!")
            break
        nombre_de_chance-=1

    if nombre_de_chance == 0:
        print("Essaie une prochane fois!")
    volonte = input("Voulez-vous continer? o/n : ")

