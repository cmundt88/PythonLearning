# Poor man's blackjack simulation - simple randomization and every hand shuffle

from random import randint
from sys import exit

#global deck
#global dealer_hand
#global player_hand

class Engine(object):

    def deal(self):

        deck = range(1, 53)
        player_hand = []
        dealer_hand = []

        for i in range(0, 2):
            player_pull = randint(0,51)
            dealer_pull = randint(0,51)

            while (deck[player_pull] == 0) or (deck[dealer_pull] == 0) or (
                    player_pull == dealer_pull):
                player_pull = randint(0,51)
                dealer_pull = randint(0,51)
                
            player_hand.append(deck[player_pull])
            dealer_hand.append(deck[dealer_pull])
            
            deck[player_pull] = 0
            deck[dealer_pull] = 0
            
        return player_hand, dealer_hand
    
    def hit(self):
        pass
        
    def stand(self):
        pass
    
    def split(self):
        pass
        
    def double_down(self):
        pass
        
    def translate_card(self, card):

        if card <= 13:
            suit = "Hearts"
            value = card
        elif 13 < card <= 26:
            suit = "Diamonds"
            value = card - 13
        elif 26 < card <= 39:
            suit = "Spades"
            value = card - 26
        elif 39 < card <= 52:
            suit = "Clubs"
            value = card - 39            
    
        if value == 1:
            name = "Ace"
        elif value < 11:
            name = str(value)
        elif value == 11:
            name = "Jack"
        elif value == 12:
            name = "Queen"
        else:
            name = "King"
        
        return name, value, suit
        
    def play(self):
    
        player, dealer = self.deal()

        d1card, d1value, d1suit = self.translate_card(dealer[0])
        p1card, p1value, p1suit = self.translate_card(player[0])
        p2card, p2value, p2suit = self.translate_card(player[1])
        
        print "\nThe Dealer has drawn a %s of %s and a hole card." % (d1card, 
            d1suit)
        print "\nYou have drawn a %s of %s and a %s of %s.\n" % (p1card, 
            p1suit, p2card, p2suit)
        user_input = raw_input("Hit(h), Stand(s), Double Down(d), or Quit(q) > ")
        
    
    
class Bank(object):
    
    wager = 0
    
    def __init__(self):
        opening_balance = 1000
        
    def take_bet(wager):
        pass

    def update_bankroll(wager):
        pass
       
agame = Engine()
agame.play()