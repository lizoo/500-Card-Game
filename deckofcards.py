import playingcard
class DeckofCards():
    def __init__(self):
        self.cardsindecklist = []  #list of lists each with 2 numbers, one for the suit and one for the value
        for value in range(4,15):
            for suit in range(4):
                card = playingcard.PlayingCard(value, suit)
                self.cardsindecklist.append(card)        
        self.cardsindecklist.append(playingcard.PlayingCard(15, 4))  #append joker card 
    def getcardsindecklist(self):
        return self.cardsindecklist
    
    def __str__(self):
        deck_str_list = [card.__str__()  for card in self.cardsindecklist]
        return '\n'.join(deck_str_list)
            

#d = DeckofCards()
#print(d)


#attributes -- all the way to the left ie:

#values = [2,3,4,5]
#def ljs(a, b):
#    pass

