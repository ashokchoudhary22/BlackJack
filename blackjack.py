#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[3]:


suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')

ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,
        'King':10,'Ace':10}

playing=True


# In[4]:


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+" of "+self.suit


# In[5]:


class Deck():
    def __init__(self):
        self.deck=[]
        for ele1 in suits:
            for ele2 in ranks:
                self.deck.append(Card(ele1,ele2))
    def __str__(self):
        str1=''
        for ele in self.deck:
            str1+='\n'+ele.__str__()
        return "The deck has:\n"+str1
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
        


# In[6]:


class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1


# In[7]:


class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet


# In[8]:


def take_bet(Chips):
    while True:
            try:
                Chips.bet=int(input("please enter no of chips you want to bet"))
            except:
                print("sorry..! please provide an integer")
            else:
                if(Chips.bet>Chips.total):
                    print("sorry...! you don't have enough chips..!  You have: {}".format(Chips.total))
                else:
                    break


# In[9]:


def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# In[10]:


def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x=input("do you want to hit or stand please enter 'h' or 's'" )
        
        if(x.lower()=='h'):
            hit(deck,hand)
        elif(x.lower()=='s'):
            print("player stand dealer's turn")
            playing=False
        else:
            print("you have not entered 'h' or 's' please enter again...!")
            continue
        break
            


# In[11]:


# Functions to deal with end of game

def player_busts(player,dealer,chips):
    print("BUST Player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player WINS!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Bust Dealer")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Player and Dealer Tie! PUSH")


# In[12]:


def show_all(player,dealer):
    print("\nDealer's Hand:",*dealer.cards,sep='\n')
    print("\nPlayer's Hand:",*player.cards,sep='\n')
    

def show_some(player,dealer):
    print("\nDealer's Hand:\n Hidden Card\n",dealer.cards[1])
    print("\nPlayer's Hand:",*player.cards,sep='\n')
        


# In[ ]:


while True:
    
    print("--------------WELCOME-------------")
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips=Chips()
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    if player_hand.value<=21:
        
        while dealer_hand.value<=player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        if(dealer_hand.value>21):
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif(dealer_hand.value>player_hand.value):
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif(dealer_hand.value<player_hand.value):
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    print(f"You have toatal {player_chips.total} chips ")
    
    new_game=input("would you like to play another Hand ? y/n")
    
    if new_game[0]=='y':
        playing=True
        continue
    else:
        print("Thank You for playing.....!")
        break

        
            


# In[ ]:




