class cardDeck:

    def __init__(self):
        self.cards = []
        suits = ['h', 'd', 'c', 's'] # Hearts, Diamonds, Clubs, Spades
        for suit in suits:
            for value in range(1, 14):
                self.cards.append([suit,value])

    def getCardSuite(self, card):
        """
        For now I'll use this pattern:
        ♠ ♥ ♣ ♦
        ._________.
        |K        |
        |♠        |
        |         |
        |    :)   |
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
            return f"""
._________.
|{rank}       |
|{asciiSuit}        |
|         |
|    :)   |
|         |
|        {asciiSuit}|
|       {rank}|
˙‾‾‾‾‾‾‾‾‾˙
        """
        else:
            return f"""
._________.
|{rank}        |
|{asciiSuit}        |
|         |
|    :)   |
|         |
|        {asciiSuit}|
|        {rank}|
˙‾‾‾‾‾‾‾‾‾˙
            """
