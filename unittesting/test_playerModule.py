import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playerModule import gamePlayer, gameDealer

class TestGamePlayer(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = gamePlayer()
    
    def test_player_initialization(self):
        """Test that player is properly initialized"""
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.money, 500)
        self.assertIsInstance(self.player.inventory, list)
        self.assertEqual(len(self.player.inventory), 1)
    
    def test_player_initial_inventory(self):
        """Test that player has correct initial inventory"""
        expected_item = {
            "id": "example-object",
            "name": "Example Object",
            "quantity": 15,
        }
        self.assertEqual(self.player.inventory[0], expected_item)
    
    def test_player_hand_is_empty_initially(self):
        """Test that player starts with empty hand"""
        self.assertEqual(len(self.player.hand), 0)
        self.assertIsInstance(self.player.hand, list)
    
    def test_player_money_is_500_initially(self):
        """Test that player starts with 500 money"""
        self.assertEqual(self.player.money, 500)
        self.assertIsInstance(self.player.money, int)


class TestGameDealer(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.dealer = gameDealer()
    
    def test_dealer_initialization(self):
        """Test that dealer is properly initialized"""
        self.assertEqual(self.dealer.hand, [])
        self.assertIsInstance(self.dealer.hand, list)
    
    def test_dealer_hand_is_empty_initially(self):
        """Test that dealer starts with empty hand"""
        self.assertEqual(len(self.dealer.hand), 0)
    
    def test_dealer_has_no_money_attribute(self):
        """Test that dealer doesn't have money attribute (unlike player)"""
        self.assertFalse(hasattr(self.dealer, 'money'))
    
    def test_dealer_has_no_inventory_attribute(self):
        """Test that dealer doesn't have inventory attribute (unlike player)"""
        self.assertFalse(hasattr(self.dealer, 'inventory'))


class TestPlayerDealerInteraction(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = gamePlayer()
        self.dealer = gameDealer()
    
    def test_player_and_dealer_are_different_objects(self):
        """Test that player and dealer are separate instances"""
        self.assertNotEqual(self.player, self.dealer)
        self.assertIsNot(self.player.hand, self.dealer.hand)
    
    def test_both_can_have_cards_independently(self):
        """Test that player and dealer can have different hands"""
        # Mock card structure
        mock_card1 = [{"suit": "h", "fakeValue": "A"}, 1]
        mock_card2 = [{"suit": "s", "fakeValue": "K"}, 10]
        
        self.player.hand.append(mock_card1)
        self.dealer.hand.append(mock_card2)
        
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(len(self.dealer.hand), 1)
        self.assertNotEqual(self.player.hand, self.dealer.hand)

if __name__ == '__main__':
    unittest.main()
