class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property
	def description(self):
		return (f"{self.name}")

p = Pet("Cesar", 1)
print(p.description)