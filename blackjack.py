from blackjackModule import cardDeck
import random


currentCardSet = cardDeck()

randomCard = currentCardSet.cards[random.randint(0,51)]

print(currentCardSet.getCardSuite(randomCard))
