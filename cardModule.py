import numpy

class cardDeck:

    def __init__(self):
        self.cards = []
        suits = ['h', 'd', 'c', 's'] # Hearts, Diamonds, Clubs, Spades
        possibleFakeValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in range(1, 14):
                self.cards.append([
                    {
                        "suit": suit,
                        "fakeValue": possibleFakeValues[value-1]
                    },
                    min(value,10)
                    ])
    
    def shuffleCards(self):
        numpy.random.shuffle(self.cards)

    def printAHand(self,hand,isDealer=False):
        visualHand = ["","","","","","","","",""]
        for i, x in enumerate(hand):
            if isDealer and i == 0:
                currentCard = self.getCardSuite(x,True)
            else:
                currentCard = self.getCardSuite(x)
            tempCardArray = currentCard.split("\n")
            counter = 0
            for y in tempCardArray:
                visualHand[counter] += y+" "
                counter+=1
        return "\n".join(visualHand)

    def getCardSuite(self, card, shouldHideCard=False):
        """
        For now I'll use this pattern:
        ♠ ♥ ♣ ♦
        ._________.
        |K        |
        |♠        |
        |         |
        |   >:D   |
        |         |
        |        ♠|
        |        K|
        ˙‾‾‾‾‾‾‾‾‾˙
        """

        emblem = ">:D"
        
        if shouldHideCard:
            asciiSuit = "XX"
            rank = "XX"
        else:
            suit = card[0]["suit"]
            rank = card[0]["fakeValue"]
            match suit:
                case "h":
                    asciiSuit = "♥"
                case "s":
                    asciiSuit = "♠"
                case "c":
                    asciiSuit = "♣"
                case "d":
                    asciiSuit = "♦"

        return f"""._________.
|{asciiSuit+" "+str(rank):<9}|
|         |
|         |
|{emblem:^9}|
|         |
|         |
|{str(rank)+" "+asciiSuit:>9}|
˙‾‾‾‾‾‾‾‾‾˙"""
