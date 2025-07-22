from cardModule import cardDeck

class blackjackGame:

    def __init__(self):
        pass

    def isBusted(hand):
        total = 0
        for x in hand:
            total += x[1]
        if total <= 21:
            return False
        else:
            return True

    def countHand(self,hand):
        total = 0
        for x in hand:
            total += x[1]
        return total
    
    def gameSituation(self,dealerHand,playerHand,currentDeck):
        return f"""\n------------\nPlayer's Hand [{self.countHand(blackjackGame,playerHand)}]
{currentDeck.printAHand(playerHand)}

Dealer's Hand [{self.countHand(blackjackGame,dealerHand)}]
{currentDeck.printAHand(dealerHand)}
"""

    def endGame(self,dealer,player,currentDeck):
        dealerTotal = self.countHand(blackjackGame,dealer.hand)
        playerTotal = self.countHand(blackjackGame,player.hand)

        if blackjackGame.isBusted(player.hand):
            return "Player busted, game lost"+self.gameSituation(blackjackGame,dealer.hand,player.hand,currentDeck)
        elif blackjackGame.isBusted(dealer.hand):
            return "Dealer busted, game won"+self.gameSituation(blackjackGame,dealer.hand,player.hand,currentDeck)
        elif playerTotal > dealerTotal:
            return "Player won!"+self.gameSituation(blackjackGame,dealer.hand,player.hand,currentDeck)
        elif dealerTotal > playerTotal:
            return "Dealer won!"+self.gameSituation(blackjackGame,dealer.hand,player.hand,currentDeck)
        elif dealerTotal == playerTotal:
            return "Game tie!"+self.gameSituation(blackjackGame,dealer.hand,player.hand,currentDeck)
