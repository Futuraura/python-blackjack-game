from cardModule import cardDeck
import random

currentCardSet = cardDeck()

randomCard = currentCardSet.cards[random.randint(0,51)]

print(currentCardSet.getCardSuite(randomCard))

currentCardSet.shuffleCards()

print(currentCardSet.getCardSuite(currentCardSet.pullACard()))

print(currentCardSet.cards)
