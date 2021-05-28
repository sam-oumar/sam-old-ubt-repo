# mydict = {
#     0: {"Prenom": "Rabia", "Profession": "Ingenieur", "Ville": "Bamako", "Age": 1},
#     1: {"Prenom": "Oumar", "Profession": "Maitrise", "Ville": "Bamako", "Age": 30},
#     2: {"Prenom": "Ficoura", "Profession": "Master", "Ville": "Bamako", "Age": 20},
# }

# for key, value in mydict.items():
#     print(key, value)

# nombre = [10, 20, 30]


# def ajoute_40(liste):
#     liste.append(40)


# ajoute_40(nombre)
# print(nombre)

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("La fonction est bien executee")
logging.info("Message d'information")
logging.warning("Attention")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")