from IPython.display import clear_output
import Deck
import Person

class Game(object):

    def __init__(self, player):
        self.player = player
        self.bet = 0
        self.deck = Deck.Deck()
        self.dealer = Person.Dealer()

    def play(self):
        print 'Let\'s play BlackJack.'
        while True:
            try:
                text = raw_input('Dealer: How much would you like to bet? Type \'bye\' to exit: ')
                if text.lower() == 'bye':
                    break;
                amount = int(text)
            except:
                print 'Dealer: Sorry, I don\'t understand it. Try again.'
                continue
            if amount <= 0:
                print 'You can\'t bet 0 or negative.'
            elif amount > self.player.bankroll:
                print 'You can\'t bet more than you have.'
            else:
                self.bet = amount
                self.play_one_game(amount)
                text = raw_input("Continue? y or n: ")
                if text.lower() == 'y':
                    clear_output()
                else:
                    break


    def deal(self):
        self.player.add_card(self.deck.get_next())
        self.player.add_card(self.deck.get_next())
        print "Player's cards:"
        self.player.print_cards(2)

        self.dealer.add_card(self.deck.get_next())
        self.dealer.add_card(self.deck.get_next())
        print "Dealer's cards:"
        self.dealer.print_cards(1)

    def play_one_game(self, amount):
        self.player.add_bankroll(-amount)
        self.deal()
        
        # player's turn
        if not self.player.blackjack():
            if self.player.try_double_down(self.bet):
                self.bet *= 2            

        while True:
            if self.player.busted():
                print "busted"
                break
            elif self.player.blackjack():
                print "black jack"
                break
            elif self.player.is_double_down() and len(self.player.cards) == 3:
                break
            elif self.player.is_done():
                break
            else:
                self.player.add_card(self.deck.get_next())
                self.player.print_cards()

        # dealer's turn
        payment = 0
        print "Dealer's cards:"
        self.dealer.print_cards()
        if self.player.busted():
            pass
        else:
            while True:
                if self.dealer.busted():
                    print "dealer busted."
                    payment = self.bet * 2
                    break
                elif self.dealer.blackjack() and self.player.blackjack():
                    payment = self.bet
                    break
                elif self.dealer.is_done():
                    player = self.player.score()
                    dealer = self.dealer.score()
                    if player == dealer:
                        payment = self.bet
                    elif dealer < player:
                        payment = self.bet * 2
                    break
                else:
                    self.dealer.add_card(self.deck.get_next())                    
                    print "Dealer hits:"
                    self.dealer.print_cards()

        print "Player: %d" %(self.player.score())
        print "Dealer: %d" %(self.dealer.score())

        if payment > 0:
            self.player.add_bankroll(payment)
        else:
            print "Player lost."

        self.dealer.throw_cards()
        self.player.throw_cards()
        self.bet = 0
        
