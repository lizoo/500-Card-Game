
## 500 Card Game
import deckofcards  
import playingcard
import random

#Deal the cards: 10 cards to each of 4 players and 5 to the blind
p1 = []
p2 = []
p3 = []
p4 = []
b = []
deck = deckofcards.DeckofCards()
gamedeck = deck.getcardsindecklist()
for j in [p1, p2, p3, p4]:
    for i in range(10):
        a = random.choice(gamedeck)
        card_index = gamedeck.index(a)
        gamedeck.pop(card_index)
        j.append(a)

for i in range(5):
    a = random.choice(gamedeck)
    print('blind contains', a)
    card_index = gamedeck.index(a)
    gamedeck.pop(card_index)
    b.append(a)

####################
#Teams: (p1 & p3) vs (p2 & p4)

#Time to look at player's hand to see what to bid

#*Note the ranking of the jacks' values depends on the suit of the winning bid 
#So we will bid according to these new rankings, thinking that if we get the bid then this will be the order 

##############
# tally the points for each suit and use the highest tally to bid.  Remember to add in things like left bauer(bower?) and joker.   
def points_est(player):   #ie 'p1'
    p1_hand = [0, 0, 0, 0]
    p2_hand = [0, 0, 0, 0]
    p3_hand = [0, 0, 0, 0]
    p4_hand = [0, 0, 0, 0]
    tally = 0
    #suit_list = [0, 1, 2, 3] = [spades, clubs, diamonds, hearts]
    
    for i in [0, 1, 2, 3]:
        tally = 0
        for j in p1:
            if j.getsuit() == i:
                tally = tally + j.getvalue()
        p1_hand[i] = p1_hand[i] + tally
    for i in [0, 1, 2, 3]:
        tally = 0
        for j in p2:
            if j.getsuit() == i:
                tally = tally + j.getvalue()
        p2_hand[i] = p2_hand[i] + tally
    for i in [0, 1, 2, 3]:
        tally = 0
        for j in p3:
            if j.getsuit() == i:
                tally = tally + j.getvalue()
        p3_hand[i] = p3_hand[i] + tally
    for i in [0, 1, 2, 3]:
         tally = 0
         for j in p4:
            if j.getsuit() == i:
                tally = tally + j.getvalue()
         p4_hand[i] = p4_hand[i] + tally

   # for k in [p1_hand, p2_hand, p3_hand, p4_hand]:
    #    for i in [0, 1, 2, 3]: 
     #       tally = 0
      #      for j in [p1, p2, p3, p4]:
       #         if j.getsuit() == i:   #getsuit doesn't work for list error
        #            tally = tally + j.getvalue()
         #   k[i] = k[i] + tally

     #for i in [0, 1, 2, 3]:
     #   tally = 0

     #   for j in p1:
     #       if j.getsuit() == i:
     #           tally = tally + j.getvalue()
     #   p1_hand[i] = p1_hand[i] + tally
   
   
   #p1_hand = [spades, clubs, diamonds, hearts]
    print('p1: ', p1_hand, 'p2 ',p2_hand, 'p3: ',p3_hand, 'p4: ' , p4_hand)
    tally = 0

#add value for left bauer(bower)-- add 8
    for i in [0, 1, 2, 3]:
        for j in p1:
            if (j.getvalue() == 11):
                if (((i == 0) and (j.getsuit() == 1))   
                or ((i == 1) and (j.getsuit() == 0))  
                or ((i == 2) and (j.getsuit() == 3))  
                or ((i == 3) and (j.getsuit() == 2))):
                    p1_hand[i] = p1_hand[i] + 8

#add value for right bauer add 10
    for i in [0, 1, 2, 3]:
        for j in p1:
            if (j.getvalue() == 11) and (j.getsuit() == i):
                p1_hand[i] =p1_hand[i] + 10

#add value for Joker--add 15 points to each suit
    for j in p1:
        if (j.getvalue() == 15) and (j.getsuit() == 4):
            for i in [0, 1, 2, 3]:
                p1_hand[i] = p1_hand[i] + 15
#add value for Aces of other suits--add 7
    for i in [0, 1, 2, 3]:
        for j in p1:
            if (j.getvalue() == 14) and (j.getsuit() != i):
                p1_hand[i] =p1_hand[i] + 7

    print(p1_hand)
    return p1_hand
#print(points_est(p1))

#time for each player to bid  -- **this could use some adjusting after testing

#each player must bid higher than previous bid or pass
#order of suits low to high: spades, clubs, diamonds, hearts
#possible to bid 6-10 of any suit (assuming it is higher than previous bid)
#ie 6 hearts is higher than 6 diamonds
def bid(p1_hand):
    suit_dict={0 : 'spades', 1 : 'clubs', 2 :'diamonds', 3 :'hearts'}   
    p1_bid_suit = p1_hand.index(max(p1_hand))
    print(max(p1_hand))
    if max(p1_hand) >= 80: 
        p1_bid_num = 10
    elif max(p1_hand) >= 70: 
        p1_bid_num = 9
    elif max(p1_hand) >= 60: 
        p1_bid_num = 8
    elif max(p1_hand) >= 50:
        p1_bid_num = 7
    elif max(p1_hand) >= 40:
        p1_bid_num = 6
    else: p1_bid_num = 'pass'
    print("player one bids " + str(p1_bid_num) +' ' + suit_dict[p1_bid_suit])
    
bid(points_est(p1))  #test

#the player who had the winning bid leads the round of play

#Tests
#The cards each player is dealt
for i in p1:
    print(i.__str__())
#for i in p2:
#    print(i.__str__())
#for i in p3:
#    print(i.__str__())
#for i in p4:
#    print(i.__str__())
#for i in b:
#    print('blind' + i.__str__())

#print(type(p1))

#card = playingcard.PlayingCard(4,2)
#points_est(p1)



