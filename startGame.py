import random
from helperFunctions import *

# LAST LEFT OFF TRYING TO SEE WHY INPUT 'S' DOES NOT FUNCTION

def startGame(root=None):
    """ Based on given examples-> {1: dealer wins, 2: blackjack, 3: player wins} """ 
    exampleMoves= {1: [ "H" ], 2: [ ], 3: [ "H", "S", "H", "H", "S" ]}
    exampleCards= {1: [ [ [3, '?'] , [6, 9] ],[10]], 2:[[[3,'?'] ,[10, "A"]]],3:[[['K', 4],["A",5]],[4],["A"],[2]]}
    
    if root:
        print("Root: ",root)
        if exampleMoves[root] != []: 
            moves = exampleMoves[root]
            print("Moves:",moves)
        else: moves = ['*']
        if exampleCards[root] != []: 
            cards = exampleCards[root]
            print("Cards:",cards)
        else: cards = [None,None]
        
        
        
        
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
    print("$$$$$$$$$$$$$")
    # if root == 2: human_score = 21 #TODO: remove after testing
    if human_score == 21:
        print("Player wins!\nBlackJack!")
        return
    
        
    while gameNotOver:
	    """ 3. Prompt user (Hit or Stand?) until player has stood, won, or busted"""
	    
	    if human_turn:
	        if not root:
	            user_input = input("Would you like to (H)it or (S)tand?")
	        if root: 
	            if moves: user_input = moves.pop(0)
	        print("POPPED USER INPUT: ",user_input)
	        if user_input == 'H':
	            print("*************")
	            if root:
	                saved = cards.pop(0)
	                card = saved[0]
	                print("saved = cards.pop(0)", card)
	            else: deck, card = generateRandomCard(deck)
	            human_hand.append(card)
	            human_score = scoreHand(human_hand)
	            displayHands(human_hand, dealer_hand, human_score, dealer_score)
	            if human_score >= 21: 	# (check if busted) 
	                human_turn, dealer_turn = False, True
	                winner, gameNotOver = "dealer", False
	                print("Player busts with: ",human_score)
	                break
	        elif user_input == 'S':
	            print(" user_input == 'S'")
	            human_turn, dealer_turn = False, True
	            displayHands(human_hand, dealer_hand, human_score, dealer_score,stand='Player',hide=dealer_card_hidden)
           
        
    
# startGame()
# startGame(root=1)

# startGame(root=2)
print("************** ")
startGame(root=3)
