import unittest
import sys
import os

# Add the parent directory to the Python path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all test modules
from test_cardModule import TestCardDeck
from test_playerModule import TestGamePlayer, TestGameDealer, TestPlayerDealerInteraction
from test_blackjackModule import TestBlackjackGame, TestBlackjackGameLogic

def create_test_suite():
    """Create a test suite combining all test cases."""
    test_suite = unittest.TestSuite()
    
    # Add CardModule tests
    test_suite.addTest(unittest.makeSuite(TestCardDeck))
    
    # Add PlayerModule tests
    test_suite.addTest(unittest.makeSuite(TestGamePlayer))
    test_suite.addTest(unittest.makeSuite(TestGameDealer))
    test_suite.addTest(unittest.makeSuite(TestPlayerDealerInteraction))
    
    # Add BlackjackModule tests
    test_suite.addTest(unittest.makeSuite(TestBlackjackGame))
    test_suite.addTest(unittest.makeSuite(TestBlackjackGameLogic))
    
    return test_suite

def run_all_tests():
    """Run all tests and display results."""
    print("=" * 70)
    print("RUNNING BLACKJACK GAME UNIT TESTS")
    print("=" * 70)
    
    # Create test suite
    suite = create_test_suite()
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! 🎉")
    else:
        print(f"\n❌ {len(result.failures + result.errors)} test(s) failed")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_tests()
