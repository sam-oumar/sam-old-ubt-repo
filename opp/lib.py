import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()

DELE = list()


class Liste(list):
    def __init__(self, nom):
        self.nom = nom
        self.chemin = os.path.join(DATA_DIR, f"{self.nom}.json")

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Chaines de caracteres uniquement")

        if element in self:
            LOGGER.error(f"{element} deja present dans la liste")
            return False
        self.append(element)
        return True

    def enlever(self, element):
        global DELE
        DELE.append(element)
        if element in self:
            self.remove(element)
            return True
        return False

    def sauvegarder(self, cat):
        # chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        if cat == "a":
            with open(self.chemin, "r") as f:
                add = json.load(f)
                rec = [el for el in self if el not in add]
                # for el in add:
                #     if el in self:
                #         print(f" - {el} yet in the list")
                #         self.remove(el)
                add.extend(rec)
                with open(self.chemin, "w") as f:
                    json.dump(add, f, indent=4)

        elif cat == "d":
            with open(self.chemin, "r") as f:
                ele = json.load(f)
                ele = [et for et in ele if et not in DELE]

                with open(self.chemin, "w") as f:
                    json.dump(ele, f, indent=4)

        return True

    def afficher(self):
        # chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        with open(self.chemin, "r") as f:
            element = json.load(f)
            print(f"Ma liste de {self.nom} :")
            for item in element:
                print(f" - {item}")


if __name__ == "__main__":
    print("Main")