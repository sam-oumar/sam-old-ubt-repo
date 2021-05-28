# import os

# chemin = "/home/samabaly/Bureau/opp"
# dossier = os.path.join(chemin, "data")
# print(dossier)
# os.makedirs(dossier)

import json

chemin = "/home/samabaly/Bureau/opp/fichier2.json"

elements = ["Fincoura", "Badiallo", "Diallo", "Rose"]

with open(chemin, "r") as f:
    liste = json.load(f)
    if liste:
        with open(chemin, "w") as l:
            dp = liste
            for el in elements:
                dp.append(el)
            json.dump(dp, l, indent=4)
    elif not liste:
        with open(chemin, "w") as l:
            # dp = liste
            liste.extend(elements)
            json.dump(liste, l, indent=4)