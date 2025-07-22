from blackjackModule import blackjackGame
import random

game = blackjackGame()

while True:
    doesTheUserWantToPlayAGame = input("Would you like to play a game? :>\n[Y] Yes\n[N] No\n> ").lower()
    match doesTheUserWantToPlayAGame:
        case "y":
            gameContinues = True
            while gameContinues:

                print(game.gameSituation())

                userChoice = input("What would you like to do?\n[S] Stand\n[H] Hit\n> ").lower()

                match userChoice:
                    case "s":
                        game.dealer.yourTurn(game)
                        print(game.endGame())
                        gameContinues = False
                        game.restartTheGame()
                        break
                    case "h":
                        returnedValue = game.pullACard(game.player)
                        if returnedValue == "01":
                            print(game.endGame())
                            gameContinues = False
                            game.restartTheGame()
                            break
                    case _:
                        print("Sorry, I didn't get that. It's either [S] Stand or [H] Hit")
        case "n":
            print("Alright then, I'll be here if ya need me!")
        case _:
            print("Huh? It's either [Y] Yes or [N] No")
