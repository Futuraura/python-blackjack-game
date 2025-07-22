import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cardModule import cardDeck

class TestCardDeck(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.deck = cardDeck()
    
    def test_deck_initialization(self):
        """Test that deck is properly initialized with 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_deck_has_all_suits(self):
        """Test that deck contains all four suits"""
        suits = set()
        for card in self.deck.cards:
            suits.add(card[0]["suit"])
        self.assertEqual(suits, {'h', 'd', 'c', 's'})
    
    def test_deck_has_correct_values(self):
        """Test that deck has correct card values"""
        values = [card[1] for card in self.deck.cards]
        # Should have 4 aces (value 1), 4 cards each of 2-9, and 16 face cards (value 10)
        self.assertEqual(values.count(1), 4)  # Aces
        self.assertEqual(values.count(10), 16)  # 10, J, Q, K (all worth 10)
        for i in range(2, 10):
            self.assertEqual(values.count(i), 4)  # 2-9 should appear 4 times each
    
    def test_deck_has_correct_fake_values(self):
        """Test that deck has correct display values"""
        fake_values = [card[0]["fakeValue"] for card in self.deck.cards]
        expected_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        for value in expected_values:
            self.assertEqual(fake_values.count(value), 4)  # Each value should appear 4 times
    
    def test_shuffle_cards_changes_order(self):
        """Test that shuffling changes the card order"""
        original_order = self.deck.cards.copy()
        self.deck.shuffleCards()
        # Very unlikely that shuffle produces same order (probability is 1/52!)
        self.assertNotEqual(original_order, self.deck.cards)
    
    def test_shuffle_cards_preserves_count(self):
        """Test that shuffling doesn't lose or add cards"""
        original_count = len(self.deck.cards)
        self.deck.shuffleCards()
        self.assertEqual(len(self.deck.cards), original_count)
    
    def test_print_empty_hand(self):
        """Test printing an empty hand"""
        empty_hand = []
        result = self.deck.printAHand(empty_hand)
        expected = "\n".join([""] * 9)  # 9 empty lines
        self.assertEqual(result, expected)
    
    def test_jack_queen_king_value_10(self):
        """Test that J, Q, K all have value 10"""
        face_cards = [card for card in self.deck.cards if card[0]["fakeValue"] in ['J', 'Q', 'K']]
        for card in face_cards:
            self.assertEqual(card[1], 10)
    
    def test_ace_value_1(self):
        """Test that Aces have value 1"""
        aces = [card for card in self.deck.cards if card[0]["fakeValue"] == 'A']
        for ace in aces:
            self.assertEqual(ace[1], 1)
    
    def test_ten_value_10(self):
        """Test that 10s have value 10"""
        tens = [card for card in self.deck.cards if card[0]["fakeValue"] == '10']
        for ten in tens:
            self.assertEqual(ten[1], 10)

if __name__ == '__main__':
    unittest.main()
