from cardModule import *
from playerModule import *

class blackjackGame:

    def __init__(self):
        self.player = gamePlayer()
        self.dealer = gameDealer()

        self.deckOCards = cardDeck()
        
        self.deckOCards.shuffleCards()

        self.pullACard(self.player)
        self.pullACard(self.player)
        self.pullACard(self.dealer)
        self.pullACard(self.dealer)

        if self.checkBlackjack() in (4, 3, 2, 1):
            self.restartTheGame()

    def restartTheGame(self):
        self.player.hand = []
        self.dealer.hand = []
        self.deckOCards = cardDeck()
        self.deckOCards.shuffleCards()
        self.pullACard(self.player)
        self.pullACard(self.player)
        self.pullACard(self.dealer)
        self.pullACard(self.dealer)
        
        if self.checkBlackjack() in (4, 3, 2, 1):
            self.restartTheGame()

    def checkBlackjack(self):
        playerHandCounted = self.countHand(self.player.hand)
        dealerHandCounted = self.countHand(self.dealer.hand)
        if dealerHandCounted >=21:
            return 4
        elif playerHandCounted >=21:
            return 3
        elif playerHandCounted == 21:
            return 2
        elif dealerHandCounted == 21:
            return 1
        else:
            return 0

    def pullACard(self, player):
        card = self.deckOCards.cards.pop()
        player.hand.append(card)
        
        if self.countHand(player.hand) > 21:
            if player == self.player:
                return "01"
            elif player == self.dealer:
                return "02"
        return "00"

    def isBusted(self,hand):
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
    
    def gameSituation(self):
        return f"""Player's Hand [{self.countHand(self.player.hand)}]
{self.deckOCards.printAHand(self.player.hand)}

Dealer's Hand [{self.countHand(self.dealer.hand)}]
{self.deckOCards.printAHand(self.dealer.hand)}
"""

    def endGame(self):
        dealerTotal = self.countHand(self.dealer.hand)
        playerTotal = self.countHand(self.player.hand)

        if self.isBusted(self.player.hand):
            return f'{self.gameSituation()}\n--------------\nPlayer busted, game lost\n'
        elif self.isBusted(self.dealer.hand):
            return f'{self.gameSituation()}\n--------------\nDealer busted, game won\n'
        elif playerTotal > dealerTotal:
            return f'{self.gameSituation()}\n--------------\nPlayer won!\n'
        elif dealerTotal > playerTotal:
            return f'{self.gameSituation()}\n--------------\nDealer won!\n'
        elif dealerTotal == playerTotal:
            return f'{self.gameSituation()}\n--------------\nGame tied!\n'
