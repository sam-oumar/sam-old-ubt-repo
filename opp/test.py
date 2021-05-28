class Bien:
	
	def __init__(self, type_c):
		self.type_c = type_c

	def add(self, added_cards):
		self.type_c.extend(added_cards)

class Person:

	def __init__(self, name, bien):
		self.name = name
		self.bien = bien



b1 = Bien("Voiture")
b2 = Bien("Maison")

p1 = Person("Barou", b1)
b1.add(b2)

print(p1.bien.type_c)