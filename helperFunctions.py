import random
from itertools import permutations

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

def scoreHand(hand):
    number_cards = {2, 3, 4, 5, 6, 7, 8, 9, 10}
    face_cards = {"J", "Q", "K"}
    total = 0
    total_aces, poss_values = 0, [ ]
    for card in hand:
        if card in list(number_cards):
            total += card
        elif card in list(face_cards):
            total += 10
        elif card == "A":
            total_aces += 1
    if total_aces > 0:  
        poss_permutations = []
        total_ones = [poss_permutations.append(1) for _ in range(total_aces)]
        total_elevens = [poss_permutations.append(11) for _ in range(total_aces)]
        poss_combos = list(permutations(poss_permutations,total_aces))
        poss_values = [sum(list(x)) for x in poss_combos]
        poss_sums = [int(x)+total for x in poss_values]
        print("POSS VALUES: ",poss_values)
        print("POSS SUMS: ",poss_sums)
        least_difference = {}
        for s in poss_sums:
            difference = abs(s-17)
            least_difference[difference] = s
        closest_to_17 = least_difference[min(list(least_difference.keys()))]
        print("closest: ",closest_to_17)
        return closest_to_17
        pass
		# TODO: might have to do permutations? to present optimal value
		# find least difference to 17 && < 21
		# if total w one permutation == 21 return	
    return total
