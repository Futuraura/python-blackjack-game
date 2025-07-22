import numpy

class cardDeck:

    def __init__(self):
        self.cards = []
        suits = ['h', 'd', 'c', 's'] # Hearts, Diamonds, Clubs, Spades
        for suit in suits:
            for value in range(1, 14):
                self.cards.append([suit,value])
    
    def shuffleCards(self):
        numpy.random.shuffle(self.cards)

    def pullACard(self):
        return self.cards.pop()

    def printAHand(self,hand):
        visualHand = ["","","","","","","","",""]
        for x in hand:
            currentCard = self.getCardSuite(x)
            tempCardArray = currentCard.split("\n")
            counter = 0
            for y in tempCardArray:
                visualHand[counter] += y+" "
                counter+=1
        return "\n".join(visualHand)

    def getCardSuite(self, card):
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

        suit = card[0]
        rank = card[1]
        match suit:
            case "h":
                asciiSuit = "♥"
            case "s":
                asciiSuit = "♠"
            case "c":
                asciiSuit = "♣"
            case "d":
                asciiSuit = "♦"

        if len(str(rank))>=2:
            return f"""._________.
|{rank}       |
|{asciiSuit}        |
|         |
|   >:D   |
|         |
|        {asciiSuit}|
|       {rank}|
˙‾‾‾‾‾‾‾‾‾˙"""
        else:
            return f"""._________.
|{rank}        |
|{asciiSuit}        |
|         |
|   >:D   |
|         |
|        {asciiSuit}|
|        {rank}|
˙‾‾‾‾‾‾‾‾‾˙"""
