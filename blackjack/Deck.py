from random import randint

class Deck(object):
    def __init__(self):
        self.generate_deck()
    
    def generate_deck(self):
        self.cards = []
        pictures = ['Heart', 'Diamond', 'Club', 'Spade']
        for a in pictures:
            for i in xrange(1,14):
                if i == 1:
                    self.cards.append((a, 'A', i))
                elif i == 11:
                    self.cards.append((a, 'J', 10))
                elif i == 12:
                    self.cards.append((a, 'Q', 10))
                elif i == 13:
                    self.cards.append((a, 'K', 10))
                else:
                    self.cards.append((a, str(i), i))

    def __len__(self):
        return len(self.cards)
    
    def get_next(self):
        if len(self.cards) == 0:
            self.generate_deck()

        index = randint(0, len(self) - 1)
        return self.cards.pop(index)
    