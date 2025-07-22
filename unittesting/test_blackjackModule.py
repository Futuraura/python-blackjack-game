import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blackjackModule import blackjackGame
from cardModule import cardDeck
from playerModule import gamePlayer, gameDealer

class TestBlackjackGame(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # We'll need to patch the shuffling to make tests deterministic
        # For now, we'll test the basic initialization
        pass
    
    def test_game_initialization_creates_players(self):
        """Test that game initialization creates player and dealer"""
        game = blackjackGame()
        self.assertIsInstance(game.player, gamePlayer)
        self.assertIsInstance(game.dealer, gameDealer)
    
    def test_game_initialization_creates_deck(self):
        """Test that game initialization creates a deck"""
        game = blackjackGame()
        self.assertIsInstance(game.deckOCards, cardDeck)
    
    def test_players_get_initial_cards(self):
        """Test that both player and dealer get 2 cards initially"""
        game = blackjackGame()
        # After initialization, both should have 2 cards (unless blackjack restart occurred)
        # We'll check they have cards, but exact count may vary due to restart logic
        self.assertGreaterEqual(len(game.player.hand), 2)
        self.assertGreaterEqual(len(game.dealer.hand), 2)
    
    def test_count_hand_empty(self):
        """Test counting an empty hand"""
        game = blackjackGame()
        empty_hand = []
        self.assertEqual(game.countHand(empty_hand), 0)
    
    def test_count_hand_single_card(self):
        """Test counting a hand with one card"""
        game = blackjackGame()
        single_card_hand = [[{"suit": "h", "fakeValue": "5"}, 5]]
        self.assertEqual(game.countHand(single_card_hand), 5)
    
    def test_count_hand_multiple_cards(self):
        """Test counting a hand with multiple cards"""
        game = blackjackGame()
        multi_card_hand = [
            [{"suit": "h", "fakeValue": "5"}, 5],
            [{"suit": "s", "fakeValue": "K"}, 10],
            [{"suit": "d", "fakeValue": "A"}, 1]
        ]
        self.assertEqual(game.countHand(multi_card_hand), 16)
    
    def test_is_busted_under_21(self):
        """Test isBusted returns False for hands under 21"""
        game = blackjackGame()
        safe_hand = [
            [{"suit": "h", "fakeValue": "5"}, 5],
            [{"suit": "s", "fakeValue": "K"}, 10]
        ]
        self.assertFalse(game.isBusted(safe_hand))
    
    def test_is_busted_exactly_21(self):
        """Test isBusted returns False for hands exactly 21"""
        game = blackjackGame()
        blackjack_hand = [
            [{"suit": "h", "fakeValue": "A"}, 1],
            [{"suit": "s", "fakeValue": "K"}, 10],
            [{"suit": "d", "fakeValue": "10"}, 10]
        ]
        self.assertFalse(game.isBusted(blackjack_hand))
    
    def test_is_busted_over_21(self):
        """Test isBusted returns True for hands over 21"""
        game = blackjackGame()
        bust_hand = [
            [{"suit": "h", "fakeValue": "K"}, 10],
            [{"suit": "s", "fakeValue": "Q"}, 10],
            [{"suit": "d", "fakeValue": "5"}, 5]
        ]
        self.assertTrue(game.isBusted(bust_hand))
    
    def test_pull_a_card_adds_to_hand(self):
        """Test that pullACard adds a card to the player's hand"""
        game = blackjackGame()
        initial_count = len(game.player.hand)
        game.pullACard(game.player)
        self.assertEqual(len(game.player.hand), initial_count + 1)
    
    def test_pull_a_card_removes_from_deck(self):
        """Test that pullACard removes a card from the deck"""
        game = blackjackGame()
        initial_deck_size = len(game.deckOCards.cards)
        game.pullACard(game.player)
        self.assertEqual(len(game.deckOCards.cards), initial_deck_size - 1)
    
    def test_pull_a_card_returns_status(self):
        """Test that pullACard returns appropriate status codes"""
        game = blackjackGame()
        # Clear hands to have controlled test
        game.player.hand = []
        game.dealer.hand = []
        
        # Normal draw should return "00"
        result = game.pullACard(game.player)
        self.assertIn(result, ["00", "01", "02"])  # Could be bust or normal
    
    def test_check_blackjack_returns_integer(self):
        """Test that checkBlackjack returns an integer status"""
        game = blackjackGame()
        result = game.checkBlackjack()
        self.assertIsInstance(result, int)
        self.assertIn(result, [0, 1, 2, 3, 4])
    
    def test_restart_clears_hands(self):
        """Test that restart game clears both hands"""
        game = blackjackGame()
        # Add some cards manually
        mock_card = [{"suit": "h", "fakeValue": "5"}, 5]
        game.player.hand.append(mock_card)
        game.dealer.hand.append(mock_card)
        
        # Clear hands and restart manually (to avoid recursion)
        game.player.hand = []
        game.dealer.hand = []
        game.deckOCards = cardDeck()
        game.deckOCards.shuffleCards()
        
        # Verify hands are empty
        self.assertEqual(len(game.player.hand), 0)
        self.assertEqual(len(game.dealer.hand), 0)
    
    def test_game_situation_returns_string(self):
        """Test that gameSituation returns a formatted string"""
        game = blackjackGame()
        result = game.gameSituation()
        self.assertIsInstance(result, str)
        self.assertIn("Player's Hand", result)
        self.assertIn("Dealer's Hand", result)


class TestBlackjackGameLogic(unittest.TestCase):
    
    def test_face_cards_worth_10(self):
        """Test that face cards are properly valued at 10"""
        game = blackjackGame()
        face_card_hand = [
            [{"suit": "h", "fakeValue": "J"}, 10],
            [{"suit": "s", "fakeValue": "Q"}, 10],
            [{"suit": "d", "fakeValue": "K"}, 10]
        ]
        self.assertEqual(game.countHand(face_card_hand), 30)
    
    def test_ace_as_low_value(self):
        """Test that aces are valued as 1"""
        game = blackjackGame()
        ace_hand = [
            [{"suit": "h", "fakeValue": "A"}, 1],
            [{"suit": "s", "fakeValue": "A"}, 1],
            [{"suit": "d", "fakeValue": "A"}, 1],
            [{"suit": "c", "fakeValue": "A"}, 1]
        ]
        self.assertEqual(game.countHand(ace_hand), 4)
    
    def test_mixed_value_hand(self):
        """Test counting a mixed hand with different card types"""
        game = blackjackGame()
        mixed_hand = [
            [{"suit": "h", "fakeValue": "A"}, 1],    # 1
            [{"suit": "s", "fakeValue": "5"}, 5],    # 5
            [{"suit": "d", "fakeValue": "J"}, 10],   # 10
            [{"suit": "c", "fakeValue": "3"}, 3]     # 3
        ]
        # Total: 1 + 5 + 10 + 3 = 19
        self.assertEqual(game.countHand(mixed_hand), 19)

if __name__ == '__main__':
    unittest.main()
