import random

volonte = "o"
start = 0
end = 4
while volonte == "o":
    nombre_mystere = random.randint(start,end)
    i = 1
    while i <= 3:
        nombre_saisi = int(input(f"Veuillez saisir votre nombre mystere entre {start} et {end} : "))
        if nombre_saisi == nombre_mystere:
            print("Bien joue!!!")
            print(f"Vous avez reussi en {i} coup(s)")
            break
        elif i == 3:
            print("Essaie une prochane fois!")
        i+=1

    volonte = input("Voulez-vous continer? o/n : ")

