

# This is the command line interface version of the BlackJack game


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True





class Card:
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit




class Deck:
    def __init__ (self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                createdcard = Card(suit,rank)
                self.allcards.append(createdcard)
    def shuffle(self):
        random.shuffle(self.allcards)
        
    def deal_one (self):
        return self.allcards.pop()

testdeck = Deck()
deckcards = testdeck.allcards
cardlist=[]
for card in deckcards:
    cardlist.append(card)


class Hand:
    def __init__ (self):
        self.cards = []
        self.aces = []
        self.allcards = []
        acevalue = 0
        cardvalue = 0
        totalvalue = 0
    
    def addcard (self,card):
        if card.rank == "Ace":
            self.aces.append(card)
            self.allcards.append(card)
        else:
            self.cards.append(card)
            self.allcards.append(card)
        
        
        
 
    def showhand (self):
      
        
        for card in range(len(self.allcards)):
            print (self.allcards[card])
    
    def handvalue (self):
        acevalue = 0
        cardvalue = 0
        totalvalue = 0 
        
        possibleace = []
        cardvaluecollect = []
        
        for card in self.cards:
            cardvaluecollect.append(card.value)
        
        cardvalue = sum(cardvaluecollect)
    
        
        
        if len (self.aces) == 1:
            possibleace.append(1)
            possibleace.append(11)
        
        elif len (self.aces) == 2:
            possibleace.append(2)
            possibleace.append(12)
        
        elif len (self.aces) == 3:
            possibleace.append (3)
            possibleace.append (13)
        
        elif len (self.aces) == 4:
            possibleace.append (4)
            possibleace.append (14)
        
        else:
            pass
        
        
        if len (possibleace) == 0:
            totalvalue = cardvalue 
            
        
        elif len (possibleace) == 2:
            if cardvalue + possibleace[0] > 21 and cardvalue + possibleace[1] > 21:
                totalvalue = cardvalue + min(possibleace)
                
                
            elif cardvalue + possibleace[0] > 21 or cardvalue + possibleace[1] > 21:
                totalvalue = cardvalue + min(possibleace)
                
            
            else:
                totalvalue = cardvalue + max(possibleace)
                
        
        return  int (totalvalue)

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet
        
    def naturalblackjack (self):
        self.total = self.total * (1.5)



def betinput(chips):
    
    total = chips.total
    
    while True:
        try:
            chips.bet = int(input('Please input how many chips you want to bet: '))
        except:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, your bet cannot exceed {total}')
                continue 
            else:
                break

    
def hit(deck,hand):
    dealcard = deck.deal_one()
    hand.addcard(dealcard)

    
def hitorstand (deck,hand):
    global playing
    acceptablechoices = ["hit", "stand"]
    choice = "Invalid"
    
    while choice not in acceptablechoices:
        
        choice = input ("Would you like to hit or stand?: ")
        
        if choice not in acceptablechoices:
            print ("Sorry, your choice was invalid.")
            continue 
        
        elif choice.lower() == "hit":
            hit(deck,hand)
            break 
        
        elif choice.lower() == "stand":
            print ("Player will now stand, dealer's turn to play.")
            playing = False
        break 
        




def showsome(hand,dealer):
    print("\nThe Dealer's Hand:")
    print(" |hidden card|")
    print(dealer.allcards[1])
    print("\n The Player's Hand:" )
    hand.showhand()
    
    
    
    
    
def showall(hand,dealer):
    print("\nThe Dealer's Hand:")
    dealer.showhand()
    
    print("\n The Player's Hand:" )
    hand.showhand()


def playerbust(hand,chips):
    chips.lose_bet()
    print ("Player has encountered a bust. Player loses their bet.")


def playerwins(hand,chips):
    chips.win_bet()
    print ("Player has won!. Player wins their bet.")
    

def dealerbusts(hand,chips):
    chips.win_bet()
    print ("Looks like the dealer has bust. Player wins their bet!")
    
    
def dealerwins(hand,chips):
    chips.lose_bet()
    print ("Looks like the dealer has won. Player loosers their bet!")
    
    
def push(hand,chips):
    print ("Both hands have the same value. We have a push scenario.")
    
def natblackjack (hand,chips):
    chips.naturalblackjack()
    print ("Player hand is worth exactly 21, Player wins with a natural blackjack!")
    


while True:
    print ("Welcome to Blackjack!, the round will now commence. Player starts with 100 chips.")
    
    playing = True
    
    gamedeck = Deck()
    playerchips = Chips()
    gamedeck.shuffle()
    
    player1 = Hand()
    dealer = Hand()
    player1.addcard(gamedeck.deal_one())
    player1.addcard(gamedeck.deal_one())
    dealer.addcard(gamedeck.deal_one())
    dealer.addcard(gamedeck.deal_one())

    
   
    
    betinput(playerchips)

    
    
    showsome(player1,dealer)
    
    if player1.handvalue() == 21:
            playing = False
            showall(player1,dealer)
            natblackjack (player1, playerchips)
            
            print(f'The Player now has {playerchips.total} chips after this round')
            
            morerounds = input("Do you wish to play another round? Enter 'yes' or 'no' ")
            if morerounds.lower() == "yes":
                playing = True
                continue
            else:
                print ("Game will now end!")
                break 

    while playing:  
        
        
        hitorstand (gamedeck, player1)
        showsome(player1,dealer)
 
        
        
        if player1.handvalue() > 21:
            playerbust (player1, playerchips)

            break

    
    if player1.handvalue() < 21:
            while dealer.handvalue() < 17:
                hit (gamedeck,dealer)
            
            showall(player1,dealer)
            
            if dealer.handvalue() > 21:
                dealerbusts (player1, playerchips)

            elif player1.handvalue() < dealer.handvalue():
                dealerwins (player1, playerchips)
            elif player1.handvalue() > dealer.handvalue():
                playerwins (player1, playerchips)
            elif player1.handvalue() == dealer.handvalue():
                push (player1, playerchips)

    print(f'The Player now has {playerchips.total} chips after this round')
    
    morerounds = input("Do you wish to play another round? Enter 'yes' or 'no' ")
    if morerounds.lower() == "yes":
        playing = True
        continue
    else:
        print ("Game will now end!")
        break 






