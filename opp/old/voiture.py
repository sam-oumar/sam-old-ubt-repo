class Voiture:
    def __init__(self, marque):
        self.marque = marque

    def afficher_marque(self, vitesse):
        print(
            f"La voiture que vous venez d'acheter est une {self.marque} et roule a une vitesse de {vitesse} km/h."
        )


v1 = Voiture("GLA")
v2 = Voiture("X6")
v3 = Voiture("RVS")

v1.afficher_marque(350)
Voiture.afficher_marque(v1, 400)