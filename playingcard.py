
class PlayingCard():
    
    def __init__(self, value, suit):
    #Values map to: 4-10, J=11, Q=12, K=13, A= 14, Joker=15 *Note 2's and 3's not used in this game
        self.value = value
        self.value_names = [None,None, None, None, '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', 'Joker']

     #Suits map to: Spades--0, Clubs--1, Diamonds--2, Hearts--3, nothing--4 (joker only)
        self.suit = suit
        self.suit_names = [' of Spades', ' of Clubs',' of Diamonds', ' of Hearts', ''] #blank is for the Joker     
     

    def __str__(self):
        return str(self.value_names[self.value])  +  str(self.suit_names[self.suit])

    def getsuit(self):
        return self.suit

    def getvalue(self):
        return self.value       

#print(PlayingCard(4, 2))    
