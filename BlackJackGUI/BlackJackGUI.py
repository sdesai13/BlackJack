import tkinter
import random
from PIL import Image,ImageTk
from tkinter import *
import random
import tkinter
from PIL import Image, ImageTk
import pygame
from pygame import mixer
from pygame import mixer_music
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
imgvalues = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace': 1}

#create Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (self.rank + " of " + self.suit)
    def prnt (self):
        return str (self.rank + " of " + self.suit)



#create Deck Class
class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                createdcard = Card(suit, rank)
                self.allcards.append(createdcard)

    def shuffle(self):
        random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()

#create Hand Class

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = []
        self.allcards = []
        acevalue = 0
        cardvalue = 0
        totalvalue = 0

    def addcard(self, card):
        if card.rank == "Ace":
            self.aces.append(card)
            self.allcards.append(card)
        else:
            self.cards.append(card)
            self.allcards.append(card)

    def showhand(self):

        for card in range(len(self.allcards)):
            print(self.allcards[card])

    def handvalue(self):
        acevalue = 0
        cardvalue = 0
        totalvalue = 0

        possibleace = []
        cardvaluecollect = []

        for card in self.cards:
            cardvaluecollect.append(card.value)

        cardvalue = sum(cardvaluecollect)

        if len(self.aces) == 1:
            possibleace.append(1)
            possibleace.append(11)

        elif len(self.aces) == 2:
            possibleace.append(2)
            possibleace.append(12)

        elif len(self.aces) == 3:
            possibleace.append(3)
            possibleace.append(13)

        elif len(self.aces) == 4:
            possibleace.append(4)
            possibleace.append(14)

        else:
            pass

        if len(possibleace) == 0:
            totalvalue = cardvalue


        elif len(possibleace) == 2:
            if cardvalue + possibleace[0] > 21 and cardvalue + possibleace[1] > 21:
                totalvalue = cardvalue + min(possibleace)


            elif cardvalue + possibleace[0] > 21 or cardvalue + possibleace[1] > 21:
                totalvalue = cardvalue + min(possibleace)


            else:
                totalvalue = cardvalue + max(possibleace)

        return int(totalvalue)

playerhand= Hand()
dealer_hand = Hand()
gamedeck = Deck()
def deal_card(frame,hand):

    next_card = gamedeck.deal_one()
    cardname = next_card.prnt()
    hand.addcard(next_card)

    tkinter.Label(frame, image=imgdict[cardname], relief="raised").pack(side="left")

    return next_card



def score_hand(hand):
    score = hand.handvalue()
    return score


def play_dealer():

    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        deal_card(dealer_card_frame, dealer_hand)
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(playerhand)
    if player_score > 21:
        result.config(text="Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        mixer.music.load("cashwin.mp3")
        pygame.mixer.music.play(loops=0)
        result.config(text="Player wins!")

    elif dealer_score > player_score:
        result.config(text="Dealer wins!")
    else:
        result.config(text="Draw!")

def deal_player():

    global playerhand
    global gamedeck
    global player_card_frame
    next_card = gamedeck.deal_one()
    cardname = next_card.prnt()
    playerhand.addcard(next_card)

    mixer.music.load("hit.mp3")
    pygame.mixer.music.play(loops=0)
    tkinter.Label(player_card_frame, image=imgdict[cardname], relief="raised").pack(side="left")

    player_score = score_hand(playerhand)

    player_score_label.set(player_score)
    if player_score > 21:
        result.config(text="Dealer Wins!")



def initial_deal():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global playerhand
    global gamedeck
    gamedeck.shuffle()
    deal_player()
    deal_player()
    deal_card(dealer_card_frame, dealer_hand)

    dealer_score_label.set(score_hand(dealer_hand))
    player_score_label.set(score_hand(playerhand))


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global playerhand
    global gamedeck
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


    dealer_hand = Hand()
    playerhand = Hand()
    gamedeck = Deck()



    result.config(text="")

    initial_deal()

def play():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global playerhand
    global gamedeck
    result.config(text="")

    dealer_hand = Hand()
    playerhand = Hand()
    gamedeck = Deck()

    initial_deal()
    mainWindow.mainloop()

mainWindow = tkinter.Tk()
pygame.mixer.init()
mainWindow.iconphoto(True, PhotoImage(file="logo.png"))
testdeck = Deck()
deckcards = testdeck.allcards
example = deckcards[0]
cardlist=[]

for card in deckcards:
    cardlist.append(card.prnt())

example = cardlist[0]

imgtuple = []

for card in cardlist:
    cardsplit = card.split()

    if imgvalues[cardsplit[0]] > 9:
        imgtuple.append((card, f'Cards/{cardsplit[2][0].lower()}{imgvalues[cardsplit[0]]}.png'))
    else:
        imgtuple.append((card, f'Cards/{cardsplit[2][0].lower()}0{imgvalues[cardsplit[0]]}.png'))



imglist = []

for (card,filepath) in imgtuple:

    img = (Image.open(filepath))


    resized_image = img.resize((74, 107), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    imglist.append((card,new_image))

imgdict = {card:img for (card,img) in imglist}


mainWindow.title("Black Jack")
mainWindow.geometry("800x640")
mainWindow.resizable(False, False)
mainWindow.configure(bg="darkgreen")
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=5)
mainWindow.columnconfigure(5, weight=0)
logoimg = (Image.open("logo.png"))

resized_img = logoimg.resize((300, 300), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(resized_img)

game_screen = tkinter.Canvas(mainWindow, borderwidth=0, highlightthickness=0, bg="darkgreen", width=400, height=400)
game_screen.grid(rowspan=1,row=10,column=2)
game_screen.create_image(200,200,image=logo_image)
result = tkinter.Label(mainWindow, text="")
result.grid(row=0, column=1, columnspan=5)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, bg="black",width=800,height=400)

card_frame.grid(row=1, column=0, sticky='ew', columnspan=8, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", bg="red", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, bg="black", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, bg="black")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2,columnspan=8)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", bg="blue", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, bg="black", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, bg="black", width=1000, height=1000)
player_card_frame.grid(row=2, column=1, sticky='ew' )

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=1, columnspan=3, sticky='w')

player_button = tkinter.Button(button_frame, text="Hit", command=deal_player, padx=8)
player_button.grid(row=0, column=0)

dealer_button = tkinter.Button(button_frame, text="Stay", command=play_dealer, padx=5)
dealer_button.grid(row=0, column=1)

reset_button = tkinter.Button(button_frame, text="New Game", command=new_game)
reset_button.grid(row=0, column=2)


if __name__ == "__main__":
    play()