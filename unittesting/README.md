# Blackjack Game Unit Tests

This directory contains comprehensive unit tests for the Python Blackjack Game.

## Test Files

### `test_cardModule.py`
Tests the `cardDeck` class functionality:
- Deck initialization (52 cards)
- Correct suits and values
- Shuffling functionality
- Card display methods
- Face card values (J, Q, K = 10)
- Ace values (A = 1)

### `test_playerModule.py`
Tests the player-related classes:
- `gamePlayer` initialization and attributes
- `gameDealer` initialization and attributes
- Player-dealer independence
- Hand management

### `test_blackjackModule.py`
Tests the main game logic:
- Game initialization
- Card counting logic
- Bust detection
- Card drawing mechanics
- Game status checking
- Hand evaluation

### `run_all_tests.py`
Master test runner that:
- Runs all test suites
- Provides detailed output
- Shows summary statistics
- Reports failures and errors

## Running Tests

### Run All Tests
```bash
cd unittesting
python run_all_tests.py
```

### Run Individual Test Files
```bash
cd unittesting
python -m unittest test_cardModule.py
python -m unittest test_playerModule.py
python -m unittest test_blackjackModule.py
```

### Run Specific Test Classes
```bash
cd unittesting
python -m unittest test_cardModule.TestCardDeck
python -m unittest test_playerModule.TestGamePlayer
python -m unittest test_blackjackModule.TestBlackjackGame
```

### Run with Verbose Output
```bash
cd unittesting
python -m unittest -v test_cardModule.py
```

## Test Coverage

The tests cover:
- ✅ Card deck creation and management
- ✅ Card shuffling
- ✅ Player and dealer initialization
- ✅ Hand counting logic
- ✅ Bust detection
- ✅ Card drawing mechanics
- ✅ Face card values (10 for J, Q, K)
- ✅ Ace handling (value of 1)
- ✅ Game state management
- ✅ Basic blackjack logic

## Notes

- Tests use mock data where needed to ensure deterministic results
- Some tests may need adjustment if the main game logic changes
- The shuffle test verifies that card order changes but doesn't test randomness quality
- Tests assume the current card structure: `[{"suit": "x", "fakeValue": "y"}, numerical_value]`

## Future Improvements

Consider adding tests for:
- Ace high/low logic (if implemented)
- Betting system
- Advanced dealer logic
- Game end conditions
- Error handling edge cases
