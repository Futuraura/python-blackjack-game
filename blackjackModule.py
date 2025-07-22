class blackjackGame:

    def isBusted(hand):
        total = 0
        for x in hand:
            total += x[1]
        if total < 21:
            return False
        else:
            return True
