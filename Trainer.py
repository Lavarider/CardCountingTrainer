import turtle
import time
import random


#below section allows us to access that information anywhere in the codebase
global listofplayeractions
listofplayeractions = []

global numofcardsdealttoplayer
global numofcardsdealttodealer

numofcardsdealttoplayer = 0
numofcardsdealttodealer = 0

global playeraction # this is important for confirmation that person is doing the right thing
playeraction="This is the action the player chooses"

global prevcardsdealt2player
prevcardsdealt2player=[]

global prevcardsdealt2dealer
prevcardsdealt2dealer = []

global prevsuitsdealt2player
prevsuitsdealt2player = []

global cardcolor
global runningcount
global cardsdealttotal
global cardvalue
global countvalue

cardcolor = "fillertext" #this ensures the color is accurate

runningcount = 0

cardsdealttotal = 0 # for purpose of true count

cardvalue = {"A": 11, "K": 10, "Q": 10, "J": 10, "T": 10, "9": 9, "8": 8, "7": 7, # A is defined as 11 bc if goes over
             "6": 6, "5": 5, "4": 4, "3": 3, "2": 2} #                               then decreases by 10
countvalue = {"A": -1, "K": -1, "Q": -1, "J": -1, "T": -1, "9": 0, "8": 0, "7": 0,
              "6": 1, "5": 1, "4": 1, "3": 1, "2": 1}

#below code iniitalizes screen

windowxvalue = 800
windowyvalue = 600

wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(windowxvalue, windowyvalue)
wn.title("Lavarider's Card Counting Adventure!")

#below code initalizes turtle pen object
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Create classes
class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"D": "♦", "C": "♣", "H": "♥", "S": "♠"}

        #{"D": "♦", "C": "♣", "H": "♥", "S": "♠"} literally just a symbol backup incase they get lost cause idk how
        #to make symbols in this app

    def print_card(self):
        print(f"{self.name}{self.symbols[self.suit]}")

    def render(self, x, y, pen):
        global cardcolor

        # Draw border
        pen.penup()
        pen.goto(x, y)
        pen.color("white")
        pen.goto(x - 50, y + 75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x + 50, y + 75)
        pen.goto(x + 50, y - 75)
        pen.goto(x - 50, y - 75)
        pen.goto(x - 50, y + 75)
        pen.end_fill()
        pen.penup()

        pen.color("black")
        pen.pendown()
        pen.goto(x + 50, y + 75)
        pen.goto(x + 50, y - 75)
        pen.goto(x - 50, y - 75)
        pen.goto(x - 50, y + 75)

        #if self.name != "":
        if cardcolor == "Red":
            pen.color("red")
            # Draw suit in the middle

            pen.penup()
            pen.goto(x - 18, y - 30)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))

            # Draw top left
            pen.penup()
            pen.goto(x - 40, y + 45)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x - 40, y + 25)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

            # Draw bottom right
            pen.penup()
            pen.goto(x + 30, y - 60)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x + 30, y - 80)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

        elif cardcolor == "Black":
            # Draw suit in the middle
            pen.color("black")

            pen.penup()
            pen.goto(x - 18, y - 30)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))

            # Draw top left
            pen.penup()
            pen.goto(x - 40, y + 45)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x - 40, y + 25)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

            # Draw bottom right
            pen.penup()
            pen.goto(x + 30, y - 60)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x + 30, y - 80)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

        elif cardcolor == "White":
            # Draw suit in the middle
            pen.color("white")

            pen.penup()
            pen.goto(x - 18, y - 30)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))

            # Draw top left
            pen.penup()
            pen.goto(x - 40, y + 45)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x - 40, y + 25)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

            # Draw bottom right
            pen.penup()
            pen.goto(x + 30, y - 60)
            pen.pendown()
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.penup()
            pen.goto(x + 30, y - 80)
            pen.pendown()
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

# below makes the button for hit

x=350
y=125

pen.penup()
pen.goto(x, y)
pen.color("blue")
pen.goto(x - 50, y + 25)
pen.begin_fill()
pen.pendown()
pen.goto(x + 50, y + 25)
pen.goto(x + 50, y - 25)
pen.goto(x - 50, y - 25)
pen.goto(x - 50, y + 25)
pen.end_fill()
pen.penup()
FONT = ('Arial', 22, 'bold')
pen.goto(345, 110)
pen.color('white')
pen.write("Hit", align='center', font=(FONT))

#below makes the button for stand
y=125 - 60

pen.penup()
pen.goto(x, y)
#pen.color("#FFC300") #hash for dark yellow
pen.color("blue")
pen.goto(x - 50, y + 25)
pen.begin_fill() # this is needed to put the cards in
pen.pendown()
pen.goto(x + 50, y + 25)
pen.goto(x + 50, y - 25)
pen.goto(x - 50, y - 25)
pen.goto(x - 50, y + 25)
pen.end_fill()
pen.penup()
FONT = ('Arial', 22, 'bold')
pen.goto(345, 110 - 62) #i cant do math ok
pen.color('white')
pen.write("Stand", align='center', font=(FONT))

# below makes function for double down

y=125 - 60 - 60

pen.penup()
pen.goto(x, y)
#pen.color("#FF00FF") hash for majenta
pen.color("blue")
pen.goto(x - 50, y + 25)
pen.begin_fill() # this is needed to put the cards in
pen.pendown()
pen.goto(x + 50, y + 25)
pen.goto(x + 50, y - 25)
pen.goto(x - 50, y - 25)
pen.goto(x - 50, y + 25)
pen.end_fill()
pen.penup()
FONT = ('Arial', 22, 'bold')
pen.goto(345, 110 - 62 - 62 + 1) #i cant do math ok
pen.color('white')
pen.write("DBL", align='center', font=(FONT))

# below makes function for split
y=125 - 60 * 3

pen.penup()
pen.goto(x, y)
pen.color("blue")
pen.goto(x - 50, y + 25)
pen.begin_fill() # this is needed to put the cards in
pen.pendown()
pen.goto(x + 50, y + 25)
pen.goto(x + 50, y - 25)
pen.goto(x - 50, y - 25)
pen.goto(x - 50, y + 25)
pen.end_fill()
pen.penup()
FONT = ('Arial', 22, 'bold')
pen.goto(345, 110 - 61.75 * 3) #i cant do math ok
pen.color('white')
pen.write("Split", align='center', font=(FONT))

# below makes button for surrender
y=125 - 60 * 4

pen.penup()
pen.goto(x, y)
#pen.color("#ff8c00") hex for dark orange
pen.color("blue")
pen.goto(x - 50, y + 25)
pen.begin_fill() # this is needed to put the cards in
pen.pendown()
pen.goto(x + 50, y + 25)
pen.goto(x + 50, y - 25)
pen.goto(x - 50, y - 25)
pen.goto(x - 50, y + 25)
pen.end_fill()
pen.penup()
FONT = ('Arial', 22, 'bold')
pen.goto(345, 110 - 61.5 * 4 + 1) #i cant do math ok
pen.color('white')
pen.write("Sur", align='center', font=(FONT))

class Deck():
    def __init__(self):
        self.cards = []

        names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        global runningcount
        global cardsdealttotal
        global countvalue

        card = self.cards.pop()

        cardsdealttotal = cardsdealttotal + 1 # for purpose of true count

        # below code updates the running count with the counting value of the most recent card dealt
        runningcount = runningcount + countvalue[card.name]

        return card

    def reset(self):
        self.cards = []

        names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "H", "C", "S")

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

        self.shuffle()

# Create deck
deck = Deck()

# Shuffle deck
deck.reset()

# defines the value of the players hand and the dealers hand
global playertotvalue
global dealertotvalue

playertotvalue = 0
dealertotvalue = 0

global hasplayersacebeendecreased
hasplayersacebeendecreased = 0

global tempdealervarforshowingofcard # this is needed for making sure the correct color is shown on dealers down card
tempdealervarforshowingofcard = "placeholder"

start_x_dealer = -200
start_y_dealer = 200 # needed here for future rendering of dealer upcard

def drawplayercard():
    global cardcolor
    global numofcardsdealttoplayer
    global playertotvalue
    global prevcardsdealt2player
    global hasplayersacebeendecreased

    start_x_player = -50
    start_y_player = -200

    time.sleep(.1)
    card = deck.get_card()
    suitval = str(card.suit)

    prevsuitsdealt2player.append(suitval)
    prevcardsdealt2player.append(str(card.name))

    playertotvalue = playertotvalue + cardvalue[card.name]
    playertotvalue = int(playertotvalue)

    if playertotvalue > 21 and prevcardsdealt2player.count("A") >= 1: # this part is still kinda buggy
        if hasplayersacebeendecreased == 0:
            playertotvalue = playertotvalue - 10
            hasplayersacebeendecreased = 1
        else:
            if playertotvalue > 21 and prevcardsdealt2player.count("A") == 2 and hasplayersacebeendecreased == 1:
                playertotvalue = playertotvalue - 10
                hasplayersacebeendecreased = 2
            if playertotvalue > 21 and prevcardsdealt2player.count("A") == 3:
                playertotvalue = playertotvalue - 10
                hasplayersacebeendecreased = 3
            if playertotvalue > 21 and prevcardsdealt2player.count("A") == 4:
                playertotvalue = playertotvalue - 10
                hasplayersacebeendecreased = 4

    if suitval == "D":
        cardcolor = "Red"
    elif suitval == "H":
        cardcolor = "Red"
    elif suitval == "C" or "S":
        cardcolor = "Black"

    # below is 70 and 80 because iterated once from the start and once from second time in first loop
    card.render(start_x_player + numofcardsdealttoplayer * 35, start_y_player + numofcardsdealttoplayer * 40, pen)

    numofcardsdealttoplayer = numofcardsdealttoplayer + 1

    if playertotvalue >= 21: # so player doesnt have to click stand every time
        time.sleep(.5)
        determinewhowins()

def drawdealercard():
    global cardcolor
    global numofcardsdealttodealer
    global dealertotvalue
    global prevcardsdealt2dealer
    global tempdealervarforshowingofcard

    start_x_dealer = -200
    start_y_dealer = 200

    time.sleep(.1)
    card = deck.get_card()
    suitval = str(card.suit)
    tempdealervarforshowingofcard = suitval

    prevcardsdealt2dealer.append(str(card.name))

    dealertotvalue = dealertotvalue + cardvalue[card.name]
    dealertotvalue = int(dealertotvalue)

    if numofcardsdealttodealer == 1:
        cardcolor = "White"
    elif suitval == "D":
        cardcolor = "Red"
    elif suitval == "H":
        cardcolor = "Red"
    elif suitval == "C" or "S":
        cardcolor = "Black"

    card.render(start_x_dealer + numofcardsdealttodealer * 110, start_y_dealer, pen)
    numofcardsdealttodealer = numofcardsdealttodealer + 1

def splitplayeractions(cardlist, suitlist, count, xplace):
    playeraction = "Filler eat a dick"
    if y > (125 - 25) and y < (125 + 25) and x > (350 - 50) and x < (350 + 50):  # hit
        playeraction = "Hit"
        card = deck.get_card()
        suitval = str(card.suit)
        cardcolor = suitval

        suitlist.append(suitval)
        cardlist.append(str(card.name))

        splitxcount = int(count + cardvalue[card.name])
        hasplayersacebeendecreasedforsplitx = 0

        if splitxcount > 21 and cardlist.count("A") >= 1:  # this part is still kinda buggy
            if hasplayersacebeendecreasedforsplitx == 0:
                splitxcount = splitxcount - 10
                hasplayersacebeendecreasedforsplitx = 1
            else:
                if splitxcount > 21 and cardlist.count("A") == 2 and hasplayersacebeendecreased == 1:
                    splitxcount = splitxcount - 10
                    hasplayersacebeendecreasedforsplitx = 2
                if playertotvalue > 21 and cardlist.count("A") == 3:
                    splitxcount = splitxcount - 10
                    hasplayersacebeendecreasedforsplitx = 3
                if playertotvalue > 21 and cardslist.count("A") == 4:
                    playertotvalue = playertotvalue - 10
                    hasplayersacebeendecreasedforsplitx = 4

        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"

        if xplace == 1: # add something here about what do do if more than 1 split
            xlocation = -200
        elif xplace == 2:
            xlocation = 100
        card.render(xlocation, start_y_player + 80, 1, pen) # ToDo generalize this
        playeraction = "Hit"

        print(split1cards)
        print(split2cards)

    if y > (60 - 25) and y < (60 + 25) and x > (350 - 50) and x < (350 + 50):  # stand
        determinewhowins()
        playeraction = "Stand"

    if y > (-5 - 25) and y < (-5 + 25) and x > (350 - 50) and x < (350 + 50):  # DD
        drawplayercard()
        determinewhowins()
        playeraction = "Double Down"

    # add function make sure all vars are the same
    if y > (-5 - 65 - 25) and y < (-5 - 65 + 25) and x > (350 - 50) and x < (350 + 50):  # Split
        # add split function
        splitcards()
        playeraction = "Split"

    if y > (-5 - 65 - 65 - 25) and y < (-5 - 65 - 65 + 25) and x > (350 - 50) and x < (350 + 50):  # surrender
        determinewhowins()  # but do this without completing dealer because thats not nessicary
        playeraction = "Surrender"

    listofplayeractions.append(playeraction)

def splitcards(): #entire function is within function
    global prevcardsdealt2player
    global prevsuitsdealt2player
    global cardcolor

    if 1 == 1: #done to reduce space
        split1cards = []
        split1suits = []
        split2cards = []
        split2suits = []
        split3cards = []
        split3suits = []
        split4cards = []
        split4suits = []

        x=0
        y=0
        pen.penup()
        pen.goto(x, y)
        pen.color("Green")
        pen.goto(x, y)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x + 295, y)
        pen.goto(x + 295, y - 350)
        pen.goto(x - 300, y - 350)
        pen.goto(x - 300, y)
        pen.end_fill()
        pen.penup()

    start_y_player = -200

    split1cards.append(prevcardsdealt2player[0])
    split1suits.append(prevsuitsdealt2player[0]) #this is always here because always will have 2 cards
    split2cards.append(prevcardsdealt2player[1])
    split2suits.append(prevsuitsdealt2player[1])

    card1=Card(split1cards[0], split1suits[0])
    card2=Card(split2cards[0], split2suits[0])

    split1count = 0
    split2count = 0
    split3count = 0
    split4count = 0

    for i in split1cards:
        split1count = split1count + cardvalue[i]
    for i in split2cards:
        split2count = split2count + cardvalue[i]

    if len(prevcardsdealt2player) == 2: # 2 card function
        x = -200
        suitval = str(split1suits[0])
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"

        card1.render(x, start_y_player, pen)

        x = 100
        suitval = str(split2suits[0])
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card2.render(x, start_y_player, pen)

        x = -200 # this second card dealt to first hand
        card = deck.get_card()
        suitval = str(card.suit)
        split1suits.append(suitval)
        split1cards.append(str(card.name))
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card.render(x + 35, start_y_player + 40, pen)

        x = 100 # this second card dealt to second hand
        card = deck.get_card()
        suitval = str(card.suit)
        split2suits.append(suitval)
        split2cards.append(str(card.name))
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card.render(x + 35, start_y_player + 40, pen)

        for i in split1cards:
            split1count = split1count + cardvalue[i]
        for i in split2cards:
            split2count = split2count + cardvalue[i]

    if split1count < 21: # need to add something for blackjack
        turtle.listen()  # might need to add wn.mainloop() somewhere here
        turtle.onscreenclick(splitplayeractions(split1cards, split1suits, split1count, 1), 1, add=False)
    elif split1count == 21:
        print("Blackjack!")

    if split2count < 21:
        turtle.listen()  # might need to add wn.mainloop() somewhere here
        turtle.onscreenclick(splitplayeractions(split2cards, split2suits, split2count, 2), 1, add=False)
    elif split2count == 21:
        print("Blackjack!")

    elif len(prevcardsdealt2player) == 3: # 3 card function
        split3cards.append(prevcardsdealt2player[2])
        split3suits.append(prevsuitsdealt2player[2])
        card3=Card(split3cards[0], split3suits[3])

        x = -250
        suitval = split1suits[0]
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card1.render(x, start_y_player, pen)

        x = 0
        suitval = split2suits[0]
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card2.render(x, start_y_player, pen)

        x = 250
        suitval = split3suits[0]
        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"
        card3.render(x, start_y_player, pen)

    elif len(prevcardsdealt2player) == 4: # 4 card function
        split3cards.append(prevcardsdealt2player[2])
        split3suits.append(prevsuitsdealt2player[2])
        split4cards.append(prevcardsdealt2player[3])
        split4suits.append(prevsuitsdealt2player[3])
        card3=Card(split3cards[0], split3suits[0])
        card4=Card(split4cards[0], split4suits[0])

    wn.mainloop()
    determinewhowins() # this is an entirely self-inclusive function so here it ends

#determines who wins and ends a round

def determinewhowins():
    global runningcount
    global playertotvalue
    global dealertotvalue
    global cardcolor
    global hasplayersacebeendecreased
    global tempdealervarforshowingofcard
    global numofcardsdealttoplayer
    global numofcardsdealttodealer
    global playeraction
    global prevcardsdealt2player
    global prevcardsdealt2dealer
    global suitval
    global prevsuitsdealt2player

    playertotvalue = int(playertotvalue)
    dealertotvalue = int(dealertotvalue)

    try: # this try_except might cause a fuckup in the running count, come back to it later if that happens
        typeofdowncard = prevcardsdealt2dealer[1]
        card = Card(typeofdowncard, suitval) # this is needed to immediatly render down card

        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"

        card.render(start_x_dealer + 110, start_y_dealer, pen)
    except:
        drawdealercard()
        drawdealercard() #repeated twice so there exists a second element in list
        typeofdowncard = prevcardsdealt2dealer[1]
        card = Card(typeofdowncard, suitval)

        if suitval == "D":
            cardcolor = "Red"
        elif suitval == "H":
            cardcolor = "Red"
        elif suitval == "C" or "S":
            cardcolor = "Black"

        card.render(start_x_dealer + 110, start_y_dealer, pen)

    if dealertotvalue <= 21 and playertotvalue <= 21 and "Surrender" not in listofplayeractions: # this line makes sure they only do this if it will affect something

        for x in range(10):
            if "A" not in prevcardsdealt2dealer:
                if dealertotvalue < 17:
                    drawdealercard()

        for x in range(5): # error earlier with ace and end up with 14 it stopped and with 16
            if "A" in prevcardsdealt2dealer and dealertotvalue < 17:
                drawdealercard()
                if dealertotvalue > 21:
                    dealertotvalue = dealertotvalue - 10
                    drawdealercard()

        if dealertotvalue == 17 and "A" in prevcardsdealt2dealer: # this is here because hit on soft 17
            dealertotvalue = 17-10
            if dealertotvalue < 17:
                drawdealercard()
                if prevcardsdealt2dealer.count("A") == 2 and dealertotvalue == 17:
                    drawdealercard()
                    if prevcardsdealt2dealer.count("A") == 3 and dealertotvalue == 17:
                        drawdealercard()
                        if prevcardsdealt2dealer.count("A") == 4 and dealertotvalue == 17:
                            drawdealercard()

    if dealertotvalue > 21 and prevcardsdealt2dealer.count("A") >= 1:
        dealertotvalue = dealertotvalue - 10
        if dealertotvalue < 17:
            drawdealercard()


    if playertotvalue > 21:
        print("player loses")
    elif playertotvalue <= 21 and playertotvalue > dealertotvalue and dealertotvalue <= 21:
        print("player wins")
    elif playertotvalue <= 21 and playertotvalue < dealertotvalue and dealertotvalue <= 21:
        print("player loses")
    elif dealertotvalue > 21:
        print("player wins")
    elif playertotvalue <= 21 and dealertotvalue <= 21 and playertotvalue == dealertotvalue:
        print("tie bozo")

    print(prevcardsdealt2dealer)

    #below resets the board

    #below ensures all variables are reset before next round
    playertotvalue = 0
    dealertotvalue = 0
    hasplayersacebeendecreased = 0
    tempdealervarforshowingofcard = "placeholder"
    numofcardsdealttoplayer = 0
    numofcardsdealttodealer = 0
    playeraction = "This is the action the player chooses"
    prevcardsdealt2player = []
    prevcardsdealt2dealer = []
    prevsuitsdealt2player = []

    time.sleep(1.2)

    #deck = Deck()
    deck.reset()

    x=0
    y=0
    pen.penup()
    pen.goto(x, y)
    pen.color("Green")
    pen.goto(x + 50, y + 299)
    pen.begin_fill()
    pen.pendown()
    pen.goto(x + 295, y + 390)
    pen.goto(x + 295, y - 350)
    pen.goto(x - 300, y - 350)
    pen.goto(x - 300, y + 390)
    pen.end_fill()
    pen.penup()

    playmultiplerounds()


def makeanaction(x, y):
    global cardcolor
    global playeraction
    global prevcardsdealt2dealer
    global listofplayeractions

    if playertotvalue <= 21 and "Split" not in listofplayeractions:

        if y > (125-25) and y < (125+25) and x > (350-50) and x < (350+50): # hit
            drawplayercard()
            playeraction="Hit"

        if y > (60 - 25) and y < (60 + 25) and x > (350 - 50) and x < (350 + 50): # stand
            determinewhowins()
            playeraction="Stand"

        if y > (-5 - 25) and y < (-5 + 25) and x > (350 - 50) and x < (350 + 50): # DD
            drawplayercard()
            determinewhowins()
            playeraction="Double Down"

        # add function make sure all vars are the same
        if y > (-5 - 65 - 25) and y < (-5 - 65 + 25) and x > (350 - 50) and x < (350 + 50): # Split
            #add split function
            splitcards()
            playeraction="Split"

        if y > (-5 - 65 - 65 - 25) and y < (-5 - 65 - 65 + 25) and x > (350 - 50) and x < (350 + 50): #surrender
            determinewhowins() # but do this without completing dealer because thats not nessicary
            playeraction="Surrender"

        listofplayeractions.append(playeraction)

    else:
        determinewhowins()


#below section defines cards dealt to player
def playmultiplerounds():
    global playertotvalue
    global dealertotvalue
    global cardcolor
    global hasplayersacebeendecreased
    global tempdealervarforshowingofcard
    global numofcardsdealttoplayer
    global numofcardsdealttodealer
    global playeraction
    global prevcardsdealt2player
    global prevcardsdealt2dealer

    for x in range(2):

        drawplayercard()

    #below section defines dealt to dealer

    #below is first dealer card
    for x in range(2):

        drawdealercard()
        suitval = tempdealervarforshowingofcard

        if 2 == len(prevcardsdealt2dealer):
            typeofdowncard = prevcardsdealt2dealer[1]
            card = Card(typeofdowncard, suitval)

            if suitval == "D":
                cardcolor = "Red"
            elif suitval == "H":
                cardcolor = "Red"
            elif suitval == "C" or "S":
                cardcolor = "Black"

            if "A" in prevcardsdealt2dealer and "K" in prevcardsdealt2dealer: # used to have elif C S D or S in each section
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            elif "A" in prevcardsdealt2dealer and "Q" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            elif "A" in prevcardsdealt2dealer and "J" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            elif "A" in prevcardsdealt2dealer and "T" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()


    #now automated part is done, up to player to decide what to do

    turtle.listen() # was turtle

    turtle.onscreenclick(makeanaction, 1, add=False)
#onscreenclick

    wn.mainloop()

for i in range(1): #this just here so I dont have to reunindent everything
    for x in range(2):

        drawplayercard()

    #below section defines dealt to dealer

    #below is first dealer card
    for x in range(2):

        drawdealercard()
        suitval = tempdealervarforshowingofcard

        if len(prevcardsdealt2dealer) == 2:
            typeofdowncard = prevcardsdealt2dealer[1]
            card = Card(typeofdowncard, suitval)

            if suitval == "D":
                cardcolor = "Red"
            elif suitval == "H":
                cardcolor = "Red"
            elif suitval == "C" or "S":
                cardcolor = "Black"

            if "A" in prevcardsdealt2dealer and "K" in prevcardsdealt2dealer: # used to have elif C S D or S in each section
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            elif "A" in prevcardsdealt2dealer and "Q" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            if "A" in prevcardsdealt2dealer and "J" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()

            if "A" in prevcardsdealt2dealer and "T" in prevcardsdealt2dealer:
                card.render(start_x_dealer + 110, start_y_dealer, pen)
                determinewhowins()


    #now automated part is done, up to player to decide what to do

    turtle.listen() # was turtle

    turtle.onscreenclick(makeanaction, 1, add=False)

    wn.mainloop()


print(playertotvalue)
print(dealertotvalue)

# ToDo create basic strategy checking function, add ending of dealers strategy to determinewhowins function
# ToDo add split function

#list of bugs found:

# possible bug with me dealt 2 aces and other dealt ace and king
# bug: when Player dealt A, K and dealer dealt A, list index Out of range
# player was dealt A, K and dealer had 4, K and drew another card


# code graveyard:

#helpful button guide:

#def button(x,y):
#    if x < 50 and x > -50 and y < 50 and y > -50:
#        print(f"Your coordinates are: ({x}, {y}).")
#turtle.onscreenclick(button, 1, add=False)



#FONT = ('Arial', 22, 'bold')

#button = Turtle()
#button.hideturtle()
#button.shape('square')
#button.fillcolor('red')
#button.penup()

#button.goto(windowxvalue-450, windowyvalue-500)
#button.shapesize(2.5, 6, 1)
#button.onclick(makeactionhit)
#button.showturtle()

#pen.penup()
#pen.goto(260, 80)
#pen.color('white')
#pen.write("Hit", align='center', font=FONT)


# Render 5 cards (back) in a row

#start_x = -250
#for x in range(5):
#    card = Card("", "")
#    card.render(start_x + x * 125, 0, pen)
#    card = deck.get_card()
#    card.render(start_x + x * 125, 0, pen)


