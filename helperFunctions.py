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
	
def displayHands(h, d, h_score, d_score, stand=None, hide=False):
    if stand:
        print("stand == 'Player'")
        if stand == 'Player':
            h_cards = 'Player stands with: '
            for i in range(len(h)): 
                h_cards += str(h[i]) + ' '
                h_cards += '= ' + str(h_score) + '\n'
            print(h_cards)
        elif stand == 'Dealer':
            d_cards = 'Dealer stands with: '
            for i in range(len(d)): 
                d_cards += str(d[i]) + ' ' 		#might have to be .to_string( ) 
                d_cards += '= ' + str(d_score) + '\n'
            print(d_cards)
        return
    """ assumption: hide is True only at the start of the game;card revelead doesnt matter """
    if hide: 
        print('Dealer has: %s %s = %s' %(str(d[0]),"?", "?")) 
        print('Player has: %s %s = %s'%(h[0], h[1], h_score)) 
    else:
        if d != []:
            d_cards = 'Dealer has: '
            for i in range(len(d)): 
            		d_cards += str(d[i]) + ' ' 
            d_cards += '= ' + str(d_score) + '\n'
        if h != []:
            h_cards = 'Player has: '
            for i in range(len(h)):
                h_cards += str(h[i]) + ' '
            h_cards += '= ' + str(h_score) + '\n'
        if d != [ ]: print(d_cards)
        if h != [ ]: print(h_cards)
