# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:56:44 2020

@author: Syed.Gilani
"""
import random
from operator import attrgetter

class Card:
    
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.colors = {"R": "Red",
                   "G": "Green",
                   "Y": "Yellow"}
        self.value = self.numbers[self.number] + self.color
    
    def getNumber(self):
        """returns the number of the card"""
        return self.number

    def getColor(self):
        """returns the color of the card"""
        return self.colors.get(self.color)
    
    def show(self):
        print("(%s, %s)" % (self.colors.get(self.color), self.numbers[self.number]))
     
    def __str__(self):
        return "%s%s" % (self.numbers[self.number], self.color)

class Deck:
    
    def __init__(self):
        self.cards = []
        self.create()
        
    def create(self):
        for color in ['R', 'G', 'Y']:
            for number in range(0, 10):
                    self.cards.append(Card(number, color))
        return self.cards

    def show(self):
        for card in self.cards:
            print(card)
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise ValueError("No more cards in the deck")
    
    def getCardCount(self):
        return len(self.cards)
    
    def shuffle(self):
        random.seed(666)
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
#        self.cards = random.shuffle(self.cards)

class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.color_points = {"R":3, "Y":2, "G":1}
        
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self
    
    def setHand(self, hand):
        self.hand = hand
    
    def sortHand(self, order):
        self.hand = sorted(self.hand, key=attrgetter('color', 'number'))
        sorted_list = []
        for color in order[::1]:
            sorted_list = sorted_list + [c for c in self.hand if c.color == color]
        self.hand = sorted_list
        return sorted_list
    
    def getScore(self):
        return self.score
    
    def incrementScore(self, increment):
        self.score += increment
        
    def showHand(self):
        return self.hand

class Game:
    
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.color_points = {"R":3, "Y":2, "G":1}
        self.deck.shuffle()
        for card in self.deck.cards:
            print(str(card))
    
    def play(self):
        try:
            i=0
            while True:
                print("Player " + self.player1.name + " turn")
                turn_points = self.turn(self.player1)
                for c in self.player1.hand[-3:]:
                    print(str(c))
                print("Player " + self.player1.name + " scored " +\
                      str(turn_points) + "in turn " + str(i))
                self.player1.incrementScore(turn_points)
                print("Player " + self.player2.name + " turn")
                turn_points = self.turn(self.player2)
                for c in self.player2.hand[-3:]:
                    print(str(c))
                print("Player " + self.player2.name + " scored " +\
                      str(turn_points) + "in turn " + str(i))
                self.player2.incrementScore(turn_points)
                i += 1
        except ValueError:
            if self.player1.getScore() > self.player2.getScore():
                print("Player " + self.player1.name + " wins with " +\
                      str(self.player1.getScore()))
                print("Player " + self.player2.name + " loses with " +\
                      str(self.player2.getScore()))
                print("Game Over")
                return self.player1
            else:
                print("Player " + self.player2.name + " wins with " +\
                      str(self.player2.getScore()))
                print("Player " + self.player1.name + " loses with " +\
                      str(self.player1.getScore()))
                print("Game Over")
                return self.player2
                
                
            
        
    
    def turn(self, player):
        turn_points = 0
        if self.deck.getCardCount() >=3:
            for i in range(0,3):
                a = player.draw(self.deck)
            for card in player.showHand():
                turn_points += (self.color_points[card.color] * int(card.number))
        else:
            raise ValueError("No More Cards Left in the Deck")
        return turn_points 
            
    
    def getWinner(self):
        if self.player1.getScore() > self.player2.getScore():
            return self.player1
        else:
            return self.player2


#d = Deck()
#d.shuffle()
#d.show()
#c = d.draw()
#print("--------------CARD------------------")
#c.show()
#print("--------------DECK-----------------")
#d.show()
#
p1 = Player("bob")
p2 = Player("Rob")
#for i in range(0,3):
#    p.draw(d)
#print("------------------UnSorted Hand-----------------")
#p.showHand()
#print("------------------Sort--------------")
#sorted_hand = p.sortHand('GYR')
#p.setHand(sorted_hand)
#p.showHand()
deck = Deck()
game = Game(p1, p2, deck)
game.play()
winner = game.getWinner()
print(p1.name + " beats " + p2.name)
print(p1.name + " Score: " + str(p1.getScore()))
print(p2.name + " Score: " + str(p2.getScore()))

            