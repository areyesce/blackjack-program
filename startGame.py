import random
# Online Python - IDE, Editor, Compiler, Interpreter

def createDeck():
    deck = []
    for _ in range(4):
        deck.extend([x for x in range(2,11)])
        deck.extend(['J', 'Q', 'K', 'A'])
    return deck

def generateRandomCard(deck):
# 	print("DECK!!!!: ",deck)
# 	print("TYPE: ",type(deck))
	card = random.choice(deck)
# 	print("RANDOM CARD:",card)
	
	if card in deck:
	    deck.remove(card)
# 	print("NEW DECK!!!!: ",deck) 
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
        pass
		# TODO: might have to do permutations? to present optimal value
		# find least difference to 17 && < 21
		# if total w one permutation == 21 return	
    return total

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
    human_score, dealer_score = scoreHand(human_hand), scoreHand(dealer_hand)
    
    """ 2. Display initial hands (hiding dealer"s second card and score) """
    dealer_card_hidden = True
    if dealer_card_hidden:
        displayHands(human_hand, dealer_hand, human_score, '?',hide=True)
    else:
        displayHands(human_hand, dealer_hand, human_score, dealer_score)
        
    while gameNotOver:
	    """ 3. Prompt user (Hit or Stand?) until player has stood, won, or busted"""
	    
	    if human_turn:
	        user_input = input("Would you like to (H)it or (S)tand?")
	        #TODO: add validity checks for user_input
	        if user_input == 'H':
	            if root:
	                saved = cards.pop(0)
	                card = saved[0]
	            else: deck, card = generateRandomCard(deck)
	            human_hand.append(card)
	            human_score = scoreHand(human_hand)
	            print("new human score:",human_score)
	            displayHands(human_hand, dealer_hand, human_score, dealer_score)
	            if human_score >= 21: 	# (check if busted) 
	                human_turn, dealer_turn = False, True
	                winner, gameNotOver = "dealer", False
	                break
	        elif user_input == 'S':
	            human_turn, dealer_turn = False, True
	            displayHands(human_hand, dealer_hand, human_score, dealer_score,hide=dealer_card_hidden)
           
        
    
# startGame()
startGame(root=1)
# startGame(root=2)
# startGame(root=3)
