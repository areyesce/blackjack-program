import random
# Online Python - IDE, Editor, Compiler, Interpreter

def createDeck():
    deck = []
    for _ in range(4):
        deck.extend([x for x in range(2,11)])
        deck.extend(['J', 'Q', 'K', 'A'])
    return deck

def generateRandomCard(deck):
	print("DECK!!!!: ",deck)
	print("TYPE: ",type(deck))
	card = random.choice(deck)
	print("RANDOM CARD:",card)
	
	if card in deck:
	    deck.remove(card)
	print("NEW DECK!!!!: ",deck) 
	return deck, card

def displayHands(h, d, h_score, d_score, stand=None, hide=False):
    if stand:
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
        print("h: ",h)
        
        print('Dealer has: %d %s = %s' %(d[0],"?", "?")) 
        print('Player has: %s %s = %s'%(h[0], h[1], h_score)) 



def startGame(root=None):
    """ Based on given examples-> {1: dealer wins, 2: blackjack, 3: player wins} """ 
    exampleMoves= {1: [ "H" ], 2: [ ], 3: [ "H", "S", "H", "H", "S" ]}
    exampleCards= {1: [ [ [3, '?'] , [6, 9] ],[10]], 2:[[[3,'?'] ,[10, "A"]]],3:[[['K', 4],["A",5]],[4],["A"],[2]]}
    
    if root:
        moves = exampleMoves[root]
        cards = exampleCards[root]
        # print("Root: ",root)
        # print("Moves:",moves)
        # print("Cards:",cards)
        
    deck = createDeck()
    human_turn, dealer_turn = True, False
    gameNotOver, winner = True,None
    
    """ 1. Deal initial cards (two cards to each player) """
    human_hand, dealer_hand = [],[]
    if root:
        rootCard = cards.pop(0)
        dealer_hand, human_hand = rootCard[0], rootCard[1]
    else:
        for hand in [human_hand, dealer_hand]:
    	    for _ in range(2):
    	        deck, card = generateRandomCard(deck)
    	        hand.append(card)
    human_score, dealer_score = 0, 0
    
    """ 2. Display initial hands (hiding dealer"s second card and score) """
    dealer_card_hidden = True
    if dealer_card_hidden:
        displayHands(human_hand, dealer_hand, human_score, '?',hide=True)
    else:
        displayHands(human_hand, dealer_hand, human_score, dealer_score, hide=True)
        
	

        
    
        
    
# startGame()
startGame(root=1)
# startGame(root=2)
# startGame(root=3)
