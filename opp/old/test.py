import json

chemin = "/home/samabaly/Bureau/opp/old/fichier.json"

val = 0

while val != 5:
    print("Choisissez une option :")
    print("         1: Ajouter un élément")
    print("         2: Enlever un élément")
    print("         3: Afficher la liste")
    print("         4: Vider la liste")
    print("         5: Terminer")
    a = int(input())
    if a == 1:
        b = input("Entrer le nom de l'élément à ajouter :")
        with open(chemin, "r") as f:
            liste = json.load(f)
            # if liste:
            with open(chemin, "w") as l:
                liste.append(b)
                json.dump(liste, l, indent=4)
    elif a == 2:
        b = input("Entrer le nom de l'élément à enlever :")
        with open(chemin, "r") as f:
            liste = json.load(f)
            # if liste:
            with open(chemin, "w") as l:
                liste.remove(b)
                json.dump(liste, l, indent=4)
    elif a == 3:
        print("Les éléments de la liste")
        with open(chemin, "r") as f:
            liste = json.load(f)
            liste.sort()
            for co, el in enumerate(liste, 1):
                print(f"{co} - {el}")
    elif a == 4:
        with open(chemin, "r") as f:
            liste = json.load(f)
            # if liste:
            with open(chemin, "w") as l:
                liste.clear()
                json.dump(liste, l)
    elif a == 5:
        val = a
    # val = int(input("Voulez continuer ?"))