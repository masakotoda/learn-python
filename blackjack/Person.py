def print_card(card, public_card = True):
    pict, sym, num = card
    if public_card:
        print '    [{0}-{1}]'.format(pict, sym)
    else:       
        print '    [*Secret card*]'


class Person(object):
    def __init__(self):
        self.cards = []
        self.double_down = False

    def throw_cards(self):
        self.cards = []
        self.double_down = False
    
    def busted(self):
        return self.score() > 21

    def blackjack(self):
        return self.score() == 21
    
    def score(self):
        total = 0
        for x in self.cards:
            total += x[2]

        # you can treat A as 11 only once (2 * 11 is greater than 21!)
        alternate = 0
        treat_A_as_11 = False
        for x in self.cards:
            if x[2] == 1 and treat_A_as_11 == False:
                alternate += 11
                treat_A_as_11 = True
            else:
                alternate += x[2]
        if alternate > 21:
            return total
        elif total > 21:
            return alternate
        elif alternate < total:
            return total
        else:
            return alternate

    def add_card(self, card):
        self.cards.append(card)
 
    def print_cards(self, count_public = -1):
        if count_public < 0:
            count_public = len(self.cards)
        for i in xrange(0, len(self.cards)):
            print_card(self.cards[i], i < count_public)

            
class Dealer(Person):
    def __init__(self):
        Person.__init__(self)

    def is_done(self):
        return self.score() >= 17

    
class Player(Person):
    def __init__(self, bankroll = 100):
        Person.__init__(self)
        self.bankroll = bankroll
        self.double_down = False
    
    def add_bankroll(self, amount):
        self.bankroll += amount
        print 'Player\'s bankroll is now $%d' %(self.bankroll)
        
    def try_double_down(self, bet):
        if bet <= self.bankroll:
            in_text = raw_input('Do you want to double down? y or n: ')
            if in_text.lower() == 'y':
                self.double_down = True
                self.add_bankroll(-bet)
                return True
        return False

    def is_double_down(self):
        return self.double_down
 
    def is_done(self):
        in_text = raw_input('Hit? y or n: ')
        if in_text.lower() == 'y':
            return False
        else:
            return True
