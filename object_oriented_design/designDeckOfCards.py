class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	def show(self):
		print "{} of {}".format(self.value, self.suit)


class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		suits = ["spades", "diamonds", "hearts", "clubs"]
		for suit in suits:
			for value in xrange(1,14):
				self.cards.append(Card(suit, value))

	def show(self):
		for card in self.cards:
			card.show()

	def shuffle(self):
		for i in xrange(len(self.cards)-1, 0, -1):
			r = random.randint(0,i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def drawCard():
		return self.cards.pop()


class Player(object):
	def __init__(self, name):
		self.hand = []
		self.name = name

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for my_card in self.hand:
			my_card.show()

	def discard(self):
		return self.hand.pop()

