import random

# ██████  ██       █████  ██    ██ ███████ ██████       ██████ ██       █████  ███████ ███████ ███████ ███████ 
# ██   ██ ██      ██   ██  ██  ██  ██      ██   ██     ██      ██      ██   ██ ██      ██      ██      ██      
# ██████  ██      ███████   ████   █████   ██████      ██      ██      ███████ ███████ ███████ █████   ███████ 
# ██      ██      ██   ██    ██    ██      ██   ██     ██      ██      ██   ██      ██      ██ ██           ██ 
# ██      ███████ ██   ██    ██    ███████ ██   ██      ██████ ███████ ██   ██ ███████ ███████ ███████ ███████ 

class gamePlayer:
    def __init__(self):
        self.hand = []
        self.money = 500
        self.bet = 0
        self.gameInfo = {
            "gamesPlayed": 0,
            "gamesLost": 0,
            "gamesWon": 0,
        }

    def playerWon(self):
        self.gameInfo["gamesWon"]+=1
        self.gameInfo["gamesPlayed"]+=1

    def playerLost(self):
        self.gameInfo["gamesLost"]+=1
        self.gameInfo["gamesPlayed"]+=1

# ------------------------------------------------------------------------------------------------------

#  ██████   █████  ███    ███ ███████      ██████ ██       █████  ███████ ███████ 
# ██       ██   ██ ████  ████ ██          ██      ██      ██   ██ ██      ██      
# ██   ███ ███████ ██ ████ ██ █████       ██      ██      ███████ ███████ ███████ 
# ██    ██ ██   ██ ██  ██  ██ ██          ██      ██      ██   ██      ██      ██ 
#  ██████  ██   ██ ██      ██ ███████      ██████ ███████ ██   ██ ███████ ███████ 

class blackjackGame:

    def __init__(self):
        self.player = gamePlayer()
        self.loadGame()
        self.restartTheGame()

    def restartTheGame(self):
        """Раздать всю колоду заново"""
        self.player.hand = []
        self.dealer_hand = []
        self.deckOCards = cardDeck()
        self.deckOCards.shuffleCards()
        self.pullACard(self.player)
        self.pullACard(self.player)
        self.pullCardToDealer()
        self.pullCardToDealer()
        
        if self.checkHand(self.player.hand)[0] != "continue" or self.checkHand(self.dealer_hand)[0] != "continue":
            self.restartTheGame()

    def saveGame(self):
        """Сохранить данные сохранения в файл gameSave.json"""
        import json

        save_data = {
            "money": self.player.money,
            "gameInfo": self.player.gameInfo,
        }
        
        try:
            with open("gameSave.json", "w") as file:
                json.dump(save_data, file, indent=4)
            return True, "Game saved successfully!"
        except Exception as e:
            return False, f"Error saving game: {e}"
    
    def loadGame(self):
        """Подгрузить данные сохранения из файла gameSave.json"""
        import json
        import os
        
        if not os.path.exists("gameSave.json"):
            return False, "No save file found!"
        
        try:
            with open("gameSave.json", "r") as file:
                save_data = json.load(file)
            
            self.player.money = save_data.get("money", 500)
            self.player.gameInfo = save_data.get("gameInfo", {
                "gamesPlayed": 0,
                "gamesLost": 0,
                "gamesWon": 0,
            })
            
            return True, f"Game loaded!\nMoney: ${self.player.money}"
        except Exception as e:
            return False, f"Error loading game: {e}"
    
    def checkHand(self, hand):
        """Универсальная проверка руки - возвращает статус любой руки"""
        total = self.countHand(hand)
        if total > 21:
            return "busted", total
        elif total == 21 and len(hand) == 2:
            return "blackjack", total
        elif total == 21:
            return "twenty_one", total
        else:
            return "continue", total

    def pullACard(self, player):
        """Достаёт карту из колоды и рассказывает если игрок прогорел"""
        card = self.deckOCards.cards.pop()
        player.hand.append(card)
        
        if self.countHand(player.hand) > 21:
            return "busted"
        return "continue"

    def endGame(self, changePlayer=True):
        """Оканчивает игру и рассказывает кто выиграл или проиграл"""
        dealerTotal = self.checkHand(self.dealer_hand)
        playerTotal = self.checkHand(self.player.hand)

        if playerTotal[0] == "busted":
            if changePlayer:
                self.player.playerLost()
            return "player_busted", "The player busted"
        elif dealerTotal[1] > playerTotal[1]:
            if changePlayer:
                self.player.playerLost()
            return "dealer_wins", "Dealer Won!"
        elif dealerTotal[0] == "busted":
            if changePlayer:
                self.player.playerWon()
                self.player.money += self.player.bet * 2
            return "dealer_busted", "The dealer busted"
        elif playerTotal[1] > dealerTotal[1]:
            if changePlayer:
                self.player.playerWon()
                self.player.money += self.player.bet * 2
            return "player_wins", "Player won!"
        else:
            if changePlayer:
                self.player.gameInfo["gamesPlayed"] += 1
                self.player.money += self.player.bet
            return "tie", "Tie"

    def pullCardToDealer(self):
        """Взять карту из колоды и добавить в руку дилера"""
        card = self.deckOCards.cards.pop()
        self.dealer_hand.append(card)
        return card

    def countHand(self, hand, isDealer=False):
        """Подсчитать общую стоимость руки"""
        total = 0
        aces = 0
        if len(hand) == 2 and isDealer:
            card = hand[1]
            if card[0]["fakeValue"] == "A":
                return 11
            return card[1]
        for card in hand:
            if card[0]["fakeValue"] == "A":
                aces += 1
                total += 11
            else:
                total += card[1]
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
            
        return total

    def hit(self):
        """Игрок бьет - берет еще одну карту"""
        self.pullACard(self.player)
        if self.checkHand(self.player.hand)[0] == "busted":
            return "busted"
        return "continue"

    def dealerTurn(self):
        """Дилер играет"""
        while self.countHand(self.dealer_hand) < 17:
            self.pullCardToDealer()
        return self.endGame()

    def canPlayerAffordBet(self, amount):
        """Проверить, достаточно ли у игрока денег для ставки"""
        return self.player.money >= amount

    def placeBet(self, amount):
        """Поставить ставку, если у игрока достаточно денег"""
        if self.canPlayerAffordBet(amount):
            self.player.bet = amount
            self.player.money -= amount
            return True
        return False

# ------------------------------------------------------------------------------------------------------

#  ██████  █████  ██████  ██████  ███████      ██████ ██       █████  ███████ ███████ 
# ██      ██   ██ ██   ██ ██   ██ ██          ██      ██      ██   ██ ██      ██      
# ██      ███████ ██████  ██   ██ ███████     ██      ██      ███████ ███████ ███████ 
# ██      ██   ██ ██   ██ ██   ██      ██     ██      ██      ██   ██      ██      ██ 
#  ██████ ██   ██ ██   ██ ██████  ███████      ██████ ███████ ██   ██ ███████ ███████ 

class cardDeck:

    def __init__(self):
        self.cards = []
        suits = ['h', 'd', 'c', 's'] # Hearts, Diamonds, Clubs, Spades
        possibleFakeValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in range(1, 14):

                if value == 1:
                    card_value = 1
                else:
                    card_value = min(value, 10)
                
                self.cards.append([
                    {
                        "suit": suit,
                        "fakeValue": possibleFakeValues[value-1]
                    },
                    card_value
                    ])
    
    def shuffleCards(self):
        random.shuffle(self.cards)

    def takeACard(self):
        return self.cards.pop()

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
