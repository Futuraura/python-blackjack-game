class gamePlayer:

    def __init__(self):
        self.hand = []

    def pullACard(self,cardClass):
        self.hand.append(cardClass.pullACard())
