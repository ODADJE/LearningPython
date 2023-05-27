films = {
    
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5,
}
prix = 0
for f in films:
    prix += films.get(f)

print(prix)