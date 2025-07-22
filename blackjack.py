from cardModule import cardDeck
from playerModule import gamePlayer
from blackjackModule import blackjackGame
import random

currentCardSet = cardDeck()
player = gamePlayer()
dealer = gamePlayer()

currentCardSet.shuffleCards()

player.pullACard(currentCardSet)
player.pullACard(currentCardSet)
dealer.pullACard(currentCardSet)
dealer.pullACard(currentCardSet)

print("Player's hand")
print(currentCardSet.printAHand(player.hand))

print("Dealer's hand")
print(currentCardSet.printAHand(dealer.hand))

if blackjackGame.isBusted(player.hand):
    print("Player busted, game lost")
elif blackjackGame.isBusted(dealer.hand):
    print("Dealer busted, game won")

# The corner of my amnesia
# randomCard = currentCardSet.cards[random.randint(0,51)]
# print(currentCardSet.getCardSuite(randomCard))
# currentCardSet.shuffleCards()
# print(currentCardSet.getCardSuite(currentCardSet.pullACard()))
# print(currentCardSet.cards)
