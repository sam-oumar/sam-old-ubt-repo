from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


# mycards = [(s,r) for s in SUITE for r in RANKS]
# print(mycards)
# print("#############################################")
# print(mycards[:26])
# print("#############################################")
# print(mycards[26:])
# shuffle(mycards)
# print(mycards)


class Deck:

	def __init__(self):
		print("Creating New Ordered Deck")
		self.allcards = [(s,r) for s in SUITE for r in RANKS]

	def shuffle(self):
		print("SHUFFLING DECK")
		shuffle(self.allcards)

	def split_in_half(self):
		return (self.allcards[:26], self.allcards[26:])

class Hand:
	
	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return f"Contains {len(self.cards)} cards"

	def add(self, added_cards):
		self.cards.extend(added_cards)

	def remove_card(self):
		return self.cards.pop()

class Player:

	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

	def play_cards(self):
		drawn_card = self.hand.remove_card()
		print(f"{self.name} has placed: {drawn_card}")
		print("\n")
		return drawn_card

	def remove_war_cards(self):
		war_cards = []
		if len(self.hand.cards) < 3:
			return self.hand.cards
		else:

			for x in range(3):
				war_cards.append(self.hand.cards.pop())
				# war_cards.append(self.hand.remove_card())
			return war_cards

	def still_has_cards(self):
		return len(self.hand.cards) != 0

print("Wlecome To War, let's begin")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

a = Hand(half1)
b = Hand(half2)

print(a, b)

comp = Player("computer", Hand(half1))

#creer un objet Hand pour le passer en parametre après

name = input("What is your name: ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards()  and comp.still_has_cards():
	total_rounds += 1
	print("Time for a new round !")
	print("Here are the current standing")
	print(user.name + " has the count : " + str(len(user.hand.cards)))
	print(comp.name + " has the count : " + str(len(comp.hand.cards)))
	print("play a card !")
	print("\n")

	tables_cards = []

	c_card = comp.play_cards()
	p_card = user.play_cards()

	tables_cards.append(c_card)
	tables_cards.append(p_card)

	if c_card[1] == p_card[1]:
		war_count += 1

		print("################################## WAR !")

		tables_cards.extend(user.remove_war_cards())
		tables_cards.extend(comp.remove_war_cards())

		if RANKS.index(c_card[1]) > RANKS.index(p_card[1]):
			user.hand.add(tables_cards)
		else:
			comp.hand.add(tables_cards)
print("game over, number of rounds :" +str(total_rounds))
print("a war happend " + str(war_count) + " times")
print("Does the computer still have cards ?")
print(str(comp.still_has_cards()))
print("Does the humain player still have cards ?")
print(str(user.still_has_cards()))