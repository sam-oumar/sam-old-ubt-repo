class Liste(list):

    dele = ""

    # chemin = os.path.join(DATA_DIR, f"{self.nom}.json")

    def __init__(self, nom):
        self.nom = nom
        # self.chemin = os.path.join(DATA_DIR, f"{self.nom}.json")

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Chaines de caracteres uniquement")

        if element in self:
            LOGGER.error(f"{element} deja present dans la liste")
            return False
        self.append(element)
        return True

    def enlever(self, element):
        global dele
        dele = element
        if element in self:
            self.remove(element)
            return f"{dele}"
        return False

    def aff_dele(self):
        print(dele)


liste = Liste("Test")
print(liste.nom)
liste.ajouter("Test1")
liste.ajouter("Test2")
for el in liste:
    print(el)
print("supression de :", liste.enlever("Test1"))
liste.aff_dele()