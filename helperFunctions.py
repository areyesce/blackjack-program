import random
def createDeck():
    deck = []
    for _ in range(4):
        deck.extend([x for x in range(2,11)])
        deck.extend(['J', 'Q', 'K', 'A'])
    return deck
    
def generateRandomCard(deck):
	card = random.choice(deck)
	
	if card in deck:
	    deck.remove(card)
	return deck, card
	
	
	
