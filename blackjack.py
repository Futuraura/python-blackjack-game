from cardModule import cardDeck
from playerModule import gamePlayer, gameDealer
from blackjackModule import blackjackGame
import random

while True:
    doesTheUserWantToPlayAGame = input("Would you like to play a game? :>\n[Y] Yes\n[N] No\n> ").lower()
    match doesTheUserWantToPlayAGame:
        case "y":
            gameContinues = True
            while gameContinues:
                currentCardSet = cardDeck()
                player = gamePlayer()
                dealer = gameDealer()

                currentCardSet.shuffleCards()

                player.pullACard(currentCardSet)
                player.pullACard(currentCardSet)
                dealer.pullACard(currentCardSet)
                dealer.pullACard(currentCardSet)
                
                gameContinues2 = True

                while True:
                    print(f"Player's hand {blackjackGame.countHand(blackjackGame,player.hand)}")
                    print(currentCardSet.printAHand(player.hand))

                    print(f"Dealer's hand {blackjackGame.countHand(blackjackGame,dealer.hand)}")
                    print(currentCardSet.printAHand(dealer.hand))

                    if blackjackGame.isBusted(player.hand):
                        print("Player busted, game lost")
                        gameContinues = False
                        gameContinues2 = False
                        break
                    elif blackjackGame.isBusted(dealer.hand):
                        print("Dealer busted, game won")
                        gameContinues = False
                        gameContinues2 = False
                        break

                    userChoice = input("What would you like to do?\n[S] Stand\n[H] Hit\n> ").lower()

                    match userChoice:
                        case "s":
                            dealer.yourTurn(currentCardSet)
                            gameContinues = False
                            gameContinues2 = False
                            print(blackjackGame.endGame(blackjackGame,dealer,player,currentCardSet))
                            break
                        case "h":
                            player.pullACard(currentCardSet)
                        case _:
                            print("Sorry, I didn't get that. It's either [S] Stand or [H] Hit")
        case "n":
            print("Alright then, I'll be here if ya need me!")
        case _:
            print("Huh? It's either [Y] Yes or [N] No")
