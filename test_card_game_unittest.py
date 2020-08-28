# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:16:04 2020

@author: Syed.Gilani
"""

import unittest
from mock import Mock, patch
from Card_Game import *

class TestCardGame(unittest.TestCase):
    
    def testCard(self):
        c = Card(9, 'R')
        self.assertEqual(c.getNumber(), 9)
        self.assertEqual(c.getColor(), 'Red')

    def testDeck(self):
        random.seed(666)
        deck = Deck()
        
        #original card count should be 30
        self.assertEqual(deck.getCardCount(), 30)
        
        #top most card on deck is 9Y 
        c = deck.draw()
        self.assertIsInstance(c, Card)
        self.assertEqual(str(c), '9Y')
        self.assertEqual(deck.getCardCount(), 29)
        
        #now the top most card is 8Y
        c = deck.draw()
        self.assertIsInstance(c, Card)
        self.assertEqual(str(c), '8Y')
        self.assertEqual(deck.getCardCount(), 28)
        
        #Shuffling the cards should change the order of cards in the deck
        deck.shuffle()
        c = deck.draw()
        self.assertIsInstance(c, Card)
        #Since calls to random  are made deterministic by using seed,
        #the first card after shuffle is 2G
        self.assertEqual(str(c), '2G')
        self.assertEqual(deck.getCardCount(), 27)
          
    def testPlayer(self):
        p = Player("Bob")
        
        #Mock the Deck
        deck = Mock()
        #mock the return value for draw method
        deck.draw.return_value = Card(9, 'R')
        p.draw(deck)
        deck.draw.return_value = Card(9, 'Y')
        p.draw(deck)
        deck.draw.return_value = Card(9, 'G')
        p.draw(deck)
        
        self.assertEqual(p.name, "Bob")
        
        #score should be 0 as no cards have been drawn 
        self.assertEqual(p.getScore(), 0)
        
        #mocked object's draw method should be called thrice
        self.assertEqual(deck.draw.call_count, 3)
        
        #length of hand in player object should be 3
        self.assertEqual(len(p.hand), 3)
        
        #testing the order of cards in hands
        #it should be the same order as the order in which they were added
        #first one should be card 9R
        self.assertEqual(p.hand[0].color, 'R')
        self.assertEqual(p.hand[0].number, 9)
        
        #second one should be card 9Y
        self.assertEqual(p.hand[1].color, 'Y')
        self.assertEqual(p.hand[1].number, 9)
        
        #third one should be card 9G
        self.assertEqual(p.hand[2].color, 'G')
        self.assertEqual(p.hand[2].number, 9)
        
        p.sortHand('YRG')
        #shuffle with YRG should change the order of the cards
        #first one should be card 9Y
        self.assertEqual(p.hand[0].color, 'Y')
        self.assertEqual(p.hand[0].number, 9)
        
        #second one should be card 9R
        self.assertEqual(p.hand[1].color, 'R')
        self.assertEqual(p.hand[1].number, 9)
        
        #third one should be card 9G
        self.assertEqual(p.hand[2].color, 'G')
        self.assertEqual(p.hand[2].number, 9)
        
        def testGame(self):
            p1 = Player("Bob")
            p2 = Player("Rob")
            deck = Mock()
            
            #test if the turn method computes points correctly 
            deck.draw.return_value = Card(9, 'R')
            p1.draw(deck)
            deck.draw.return_value = Card(9, 'Y')
            p1.draw(deck)
            deck.draw.return_value = Card(9, 'G')
            p1.draw(deck)
            
            points = game.turn(p1)
            
            self.assertEqual(points, 27+18+9)
            
            deck.draw.return_value = Card(8, 'R')
            p2.draw(deck)
            deck.draw.return_value = Card(8, 'Y')
            p2.draw(deck)
            deck.draw.return_value = Card(8, 'G')
            p2.draw(deck)
            
            points = game.turn(p2)
            
            self.assertEqual(points, 24+16+8)
            

if __name__ == '__main__':
    unittest.main()