from blackjackModule import blackjackGame
from textual.app import App
from textual import on
from textual.widgets import Static, Button, Footer, Header, _toast, Input
from textual.theme import Theme
from textual.screen import Screen
from textual.containers import Horizontal, Container, Center, Middle
from textual.reactive import reactive

pokerTheme = Theme(name="poker", primary="#FFD700", secondary="#228B22", accent="#DC143C", foreground="#FFFFFF", background="#0F5132", success="#32CD32", warning="#FFA500", error="#FF0000", surface="#1B5E20", panel="#2E7D32", dark=True,)
game = blackjackGame()

# ███████ ███    ██ ██████      ███████  ██████ ██████  ███████ ███████ ███    ██ 
# ██      ████   ██ ██   ██     ██      ██      ██   ██ ██      ██      ████   ██ 
# █████   ██ ██  ██ ██   ██     ███████ ██      ██████  █████   █████   ██ ██  ██ 
# ██      ██  ██ ██ ██   ██          ██ ██      ██   ██ ██      ██      ██  ██ ██ 
# ███████ ██   ████ ██████      ███████  ██████ ██   ██ ███████ ███████ ██   ████ 

class EndScreen(Screen):
    CSS_PATH = "tcss/endScreen.tcss"
    def compose(self):
        yield Header()
        yield CustomFooter()

        with Container(classes="endingContainer", id="endingContainer"):
            yield EndingScreenTitle(classes="endingTextContainer")
            yield PlayerCards()
            yield DealerCards()
            yield Button("Play Again!", id="playAgainButton")
            yield Button("Main Menu", id="backToMainMenu")

    def on_mount(self):
        self.sub_title = "Game Over!"
        self.query_one("#endingContainer").border_title = "Game Over"

    @on(Button.Pressed, "#playAgainButton")
    def playAgain(self):
        game.restartTheGame()
        mainApp.switch_screen(BetScreen())
    
    @on(Button.Pressed, "#backToMainMenu")
    def backToMainMenu(self):
        game.restartTheGame()
        mainApp.pop_screen()

class EndingScreenTitle(Static):

    endingTitle = reactive(game.endGame(changePlayer=False)[1])

    def compose(self):
        with Horizontal(id="hand-container"):
            self.stats_display = Static(self.cardsText(), classes="endingText")
            yield self.stats_display

    def cardsText(self):
        return f"{game.endGame(changePlayer=False)[1]}"

    def on_mount(self):
        self.set_interval(0.1, self.refresh_stats)
        self.refresh_stats()

    def refresh_stats(self):
        """Refresh stats from game object"""
        old_endingTitle = self.endingTitle

        new_endingTitle = game.endGame(changePlayer=False)[1]

        if (old_endingTitle != new_endingTitle):
            self.endingTitle = new_endingTitle

    def watch_endingTitle(self):
        self.update_stats_display()

    def update_stats_display(self):
        if hasattr(self, 'stats_display'):
            self.stats_display.update(self.cardsText())

#  ██████   █████  ███    ███ ███████     ███████  ██████ ██████  ███████ ███████ ███    ██ 
# ██       ██   ██ ████  ████ ██          ██      ██      ██   ██ ██      ██      ████   ██ 
# ██   ███ ███████ ██ ████ ██ █████       ███████ ██      ██████  █████   █████   ██ ██  ██ 
# ██    ██ ██   ██ ██  ██  ██ ██               ██ ██      ██   ██ ██      ██      ██  ██ ██ 
#  ██████  ██   ██ ██      ██ ███████     ███████  ██████ ██   ██ ███████ ███████ ██   ████ 

class GameScreen(Screen):
    CSS_PATH = "tcss/gameScreen.tcss"

    def compose(self):
        yield Header()
        yield CustomFooter()

        yield PlayerCards(classes="cardsDisplay")
        yield DealerCards(classes="cardsDisplay")

        yield Button("Hit", id="hitButton")
        yield Button("Stand", id="standButton")
        yield Static()
        yield Static()

    def on_mount(self):
        self.sub_title = "In game"

    @on(Button.Pressed, "#hitButton")
    def hitACard(self):
        if game.hit() == "busted":
            mainApp.switch_screen(EndScreen())
    
    @on(Button.Pressed, "#standButton")
    def stand(self):
        game.dealerTurn()
        mainApp.switch_screen(EndScreen())

# ██████  ██       █████  ██    ██ ███████ ██████       ██████  █████  ██████  ██████  ███████ 
# ██   ██ ██      ██   ██  ██  ██  ██      ██   ██     ██      ██   ██ ██   ██ ██   ██ ██      
# ██████  ██      ███████   ████   █████   ██████      ██      ███████ ██████  ██   ██ ███████ 
# ██      ██      ██   ██    ██    ██      ██   ██     ██      ██   ██ ██   ██ ██   ██      ██ 
# ██      ███████ ██   ██    ██    ███████ ██   ██      ██████ ██   ██ ██   ██ ██████  ███████ 

class PlayerCards(Static):

    playerHand = reactive(game.player.hand)
    playerCards = reactive(game.deckOCards.printAHand(game.player.hand, False))

    def compose(self):
        with Horizontal(id="hand-container"):
            self.stats_display = Static(self.cardsText(), classes="playerCardsText")
            yield self.stats_display

    def cardsText(self):
        return f"Player's Hand: [{game.countHand(game.player.hand,False)}]\n{self.playerCards}"

    def on_mount(self):
        self.set_interval(0.1, self.refresh_stats)
        self.refresh_stats()

    def refresh_stats(self):
        """Refresh stats from game object"""
        old_hand = self.playerHand
        old_cards = self.playerCards
        
        new_hand = game.player.hand
        new_cards = game.deckOCards.printAHand(game.player.hand, False)

        if (old_hand != new_hand or 
            old_cards != new_cards):
            self.playerHand = new_hand
            self.playerCards = new_cards

    def watch_playerHand(self):
        self.update_stats_display()

    def watch_playerCards(self):
        self.update_stats_display()

    def update_stats_display(self):
        if hasattr(self, 'stats_display'):
            self.stats_display.update(self.cardsText())

# ██████  ███████  █████  ██      ███████ ██████       ██████  █████  ██████  ██████  ███████ 
# ██   ██ ██      ██   ██ ██      ██      ██   ██     ██      ██   ██ ██   ██ ██   ██ ██      
# ██   ██ █████   ███████ ██      █████   ██████      ██      ███████ ██████  ██   ██ ███████ 
# ██   ██ ██      ██   ██ ██      ██      ██   ██     ██      ██   ██ ██   ██ ██   ██      ██ 
# ██████  ███████ ██   ██ ███████ ███████ ██   ██      ██████ ██   ██ ██   ██ ██████  ███████ 

class DealerCards(Static):

    dealerHand = reactive(game.dealer_hand)
    dealerCards = reactive(game.deckOCards.printAHand(game.dealer_hand, True))

    def compose(self):
        with Horizontal(id="hand-container"):
            self.stats_display = Static(self.cardsText(), classes="dealerCardsText")
            yield self.stats_display

    def cardsText(self):
        return f"Dealer's Hand: [{game.countHand(game.dealer_hand,True)}]\n{self.dealerCards}"

    def on_mount(self):
        self.set_interval(0.1, self.refresh_stats)
        self.refresh_stats()

    def refresh_stats(self):
        """Refresh stats from game object"""
        old_hand = self.dealerHand
        old_cards = self.dealerCards

        new_hand = game.dealer_hand
        new_cards = game.deckOCards.printAHand(game.dealer_hand, True)

        if (old_hand != new_hand or 
            old_cards != new_cards):
            self.dealerHand = new_hand
            self.dealerCards = new_cards

    def watch_dealerHand(self):
        self.update_stats_display()

    def watch_dealerCards(self):
        self.update_stats_display()

    def update_stats_display(self):
        if hasattr(self, 'stats_display'):
            self.stats_display.update(self.cardsText())

# ██████  ███████ ████████     ███████  ██████ ██████  ███████ ███████ ███    ██ 
# ██   ██ ██         ██        ██      ██      ██   ██ ██      ██      ████   ██ 
# ██████  █████      ██        ███████ ██      ██████  █████   █████   ██ ██  ██ 
# ██   ██ ██         ██             ██ ██      ██   ██ ██      ██      ██  ██ ██ 
# ██████  ███████    ██        ███████  ██████ ██   ██ ███████ ███████ ██   ████ 

class BetScreen(Screen):
    BINDINGS = [
        ("ctrl+b", "backToMainMenuFromBetScreen", "Back to Main Menu"),
    ]
    CSS_PATH="tcss/BetScreen.tcss"

    def action_backToMainMenuFromBetScreen(self):
        mainApp.pop_screen()

    def on_mount(self):
        self.sub_title = "Placing a Bet..."

    def compose(self):
        yield Header()
        yield CustomFooter()

        yield Static("Please, input your bet!")
        yield Input( type="integer", placeholder="100", id="betTextField" )
        yield Static("Press enter to place the bet!")
        yield Button("Cancel", id="cancelBetButton")

    @on(Button.Pressed, "#cancelBetButton")
    def cancelBet(self):
        self.app.pop_screen()

    @on(Input.Submitted, '#betTextField')
    def placeABet(self, event: Input.Submitted):
        bet_input = event
        bet_value = event.value

        if not bet_value:
            self.notify(
                "Please enter a bet amount.",
                severity="error"
            )
        
        validation_result = bet_input.validation_result
        if not validation_result.is_valid:
            errors = "\n".join(validation_result.failure_descriptions)
            self.notify(f"Invalid bet:\n{errors}", severity="error")
        try:
            bet_amount = int(bet_value)
            
            if bet_amount <= 0:
                self.notify("Bet must be greater than 0", severity="error")
            elif bet_amount > game.player.money:
                self.notify(f"Insufficient funds! You only have ${game.player.money}", severity="error")
            else:
                game.player.bet = bet_amount
                game.player.money -= game.player.bet
                self.notify(f"Bet placed: ${bet_amount}", severity="success")
                
                self.app.switch_screen(GameScreen())
        except ValueError:
            self.notify("Please enter a valid number", severity="error")
            return

    def on_mount(self):
        self.sub_title = "Betting screen"
        self.add_class("bet-screen")

# ███    ███  █████  ██ ███    ██     ███    ███ ███████ ███    ██ ██    ██     ███████  ██████   ██████  ████████ ███████ ██████  
# ████  ████ ██   ██ ██ ████   ██     ████  ████ ██      ████   ██ ██    ██     ██      ██    ██ ██    ██    ██    ██      ██   ██ 
# ██ ████ ██ ███████ ██ ██ ██  ██     ██ ████ ██ █████   ██ ██  ██ ██    ██     █████   ██    ██ ██    ██    ██    █████   ██████  
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██  ██  ██ ██      ██  ██ ██ ██    ██     ██      ██    ██ ██    ██    ██    ██      ██   ██ 
# ██      ██ ██   ██ ██ ██   ████     ██      ██ ███████ ██   ████  ██████      ██       ██████   ██████     ██    ███████ ██   ██ 

class CustomFooter(Static):

    playerMoney = reactive(game.player.money)
    playerWins = reactive(game.player.gameInfo["gamesWon"])
    playerLosses = reactive(game.player.gameInfo["gamesLost"])

    def compose(self):
        with Horizontal(id="footer-container"):
            self.stats_display = Static(self.footer_text(), id="textDisplay")
            yield self.stats_display

    def footer_text(self):
        return f"Available Money: ${self.playerMoney} | Games Won: {self.playerWins} | Games Lost: {self.playerLosses}"

    def updateFooterStats(self):
        self.playerMoney = game.player.money
        self.playerWins = game.player.gameInfo["gamesWon"]
        self.playerLosses = game.player.gameInfo["gamesLost"]
        self.update_stats_display()

    def on_mount(self):
        self.set_interval(0.1, self.refresh_stats)
        self.refresh_stats()

    def refresh_stats(self):
        """Refresh stats from game object"""
        old_money = self.playerMoney
        old_wins = self.playerWins
        old_losses = self.playerLosses
        
        new_money = game.player.money
        new_wins = game.player.gameInfo["gamesWon"]
        new_losses = game.player.gameInfo["gamesLost"]
        
        if (old_money != new_money or 
            old_wins != new_wins or 
            old_losses != new_losses):
            self.playerMoney = new_money
            self.playerWins = new_wins
            self.playerLosses = new_losses

    def watch_playerMoney(self):
        self.update_stats_display()

    def watch_playerWins(self):
        self.update_stats_display()

    def watch_playerLosses(self):
        self.update_stats_display()

    def update_stats_display(self):
        if hasattr(self, 'stats_display'):
            self.stats_display.update(self.footer_text())

# ███    ███  █████  ██ ███    ██     ███    ███ ███████ ███    ██ ██    ██ 
# ████  ████ ██   ██ ██ ████   ██     ████  ████ ██      ████   ██ ██    ██ 
# ██ ████ ██ ███████ ██ ██ ██  ██     ██ ████ ██ █████   ██ ██  ██ ██    ██ 
# ██  ██  ██ ██   ██ ██ ██  ██ ██     ██  ██  ██ ██      ██  ██ ██ ██    ██ 
# ██      ██ ██   ██ ██ ██   ████     ██      ██ ███████ ██   ████  ██████ 

class MainMenu(Screen):
    CSS_PATH = "tcss/mainmenu.tcss"
    def compose(self):
        yield Header()
        yield CustomFooter()

        with Container(classes="titleContainer"):
            yield Static("BlackJack", classes="title")
            yield Static("By Futuraura :3", classes="title")

        yield Button("Start", id="startTheGame")
        yield Button("Save the game", id="saveTheGame")
        yield Button("Load the game", id="loadTheGame")

    def on_mount(self):
        self.sub_title = "Main Menu"

    @on(Button.Pressed, "#startTheGame")
    def startTheGame(self):
        mainApp.push_screen(BetScreen())

    @on(Button.Pressed, "#saveTheGame")
    def saveTheGame(self):
        success, message = game.saveGame()
        if success:
            mainApp.notify(
                message,
                title="Save Game",
                severity="information"
            )
        else:
            mainApp.notify(
                message,
                title="Save Game Error",
                severity="error"
            )

    @on(Button.Pressed, "#loadTheGame")    
    def loadTheGame(self):
        success, message = game.loadGame()
        if success:
            mainApp.notify(
                message,
                title="Load Game",
                severity="information"
            )
        else:
            mainApp.notify(
                message,
                title="Load Game Error",
                severity="error"
            )

# ████████ ██   ██ ███████      █████  ██████  ██████       ██████ ██       █████  ███████ ███████ 
#    ██    ██   ██ ██          ██   ██ ██   ██ ██   ██     ██      ██      ██   ██ ██      ██      
#    ██    ███████ █████       ███████ ██████  ██████      ██      ██      ███████ ███████ ███████ 
#    ██    ██   ██ ██          ██   ██ ██      ██          ██      ██      ██   ██      ██      ██ 
#    ██    ██   ██ ███████     ██   ██ ██      ██           ██████ ███████ ██   ██ ███████ ███████ 

class blackjackApp(App):
    ENABLE_COMMAND_PALETTE = True
    CSS_PATH="tcss/CustomFooter.tcss"

    def compose(self):
        self.register_theme(pokerTheme)
        self.theme = "poker"

        yield Header()
        self.title = "Blackjack Game"

        self.push_screen(MainMenu())

if __name__ == "__main__":
    mainApp = blackjackApp()
    mainApp.run()
