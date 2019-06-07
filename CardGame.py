# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:26:15 2019

@author: Shivangi
"""
import random

class CardGame:
    def __init__(self):
        self.chrachteristics = []
        self.player = []
   
player1 = CardGame()
player2 = CardGame()
        
king = {"Name" : "King",
        "Powerful" : 10,
        "Beautiful" : 9,
        "Joyful" : 2,
        "Trump" : 8}
queen = {"Name" : "Queen",
        "Powerful" : 9,
        "Beautiful" : 10,
        "Joyful" : 3,
        "Trump" : 6}
joker = {"Name" : "Joker",
        "Powerful" : 8,
        "Beautiful" : 5,
        "Joyful" : 10,
        "Trump" : 1}
ace = {"Name" : "Ace",
       "Powerful" : 7,
        "Beautiful" : 6,
        "Joyful" : 4,
        "Trump" : 10}
        
cards = [king, queen, joker, ace]

random.shuffle(cards)

player1 = cards[len(cards)//2:]
#print(player1)

player2 = cards[:len(cards)//2]
#print(player2)

def rolling_dice():
    def do_nonlocal():
        nonlocal dice_played_by_player1
        nonlocal dice_played_by_player2
        
    dice_played_by_player1 = random.randint(1,6)
    print('Dice played by player1 is ', dice_played_by_player1)            
    dice_played_by_player2 = random.randint(1,6)
    print('Dice played by player2 is ', dice_played_by_player2)
    
    
    while ((dice_played_by_player1) == (dice_played_by_player2)):
        dice_played_by_player1 = random.randint(1,6)
        print('dice_played_by_player1 again is ', dice_played_by_player1)
        dice_played_by_player2 = random.randint(1,6)
        print('dice_played_by_player2 again is ', dice_played_by_player2)
        
    if (dice_played_by_player1) > (dice_played_by_player2):
        print('\nPlayer1 will start the game with',player1[0])
    else:
        print('\nPlayer2 will start the game with',player2[0])


rolling_dice()

player1_win_count = 0
player2_win_count = 0

outdated_deck = []

for i in cards:

    character_choice = input('Choose any of the character: ')   
#    print(character_choice)
        
    if character_choice == '1':
        if player1[0]["Powerful"] > player2[0]["Powerful"]:
            print("Player1 win")
            player1_win_count += 1
            print("player1 won with count =" ,player1_win_count)
            
        else:
            print("Player2 win")
            player2_win_count += 1
            print("player2 won with count =" ,player2_win_count)
            
  
    if character_choice == '2':
        if player1[0]["Beautiful"] > player2[0]["Beautiful"]:
            print("Player1 win")
            player1_win_count += 1
            print("player1 won with count =" ,player1_win_count)
            
        else:
            print("Player2 win")
            player2_win_count += 1
            print("player2 won with count =" ,player2_win_count)
            
                
    if character_choice == '3':
        if player1[0]["Joyful"] > player2[0]["Joyful"]:
            print("Player1 win")        
            player1_win_count += 1
            print("player1 won with count =" ,player1_win_count)
            
        else:
            print("Player2 win") 
            player2_win_count += 1
            print("player2 won with count =" ,player2_win_count)
            
    
    if character_choice == '4':
        if player1[0]["Trump"] > player2[0]["Trump"]:
            print("Player1 win")
            player1_win_count += 1
            print("player1 won with count =" ,player1_win_count)
            
        else:
            print("Player2 win") 
            player2_win_count += 1
            print("player2 won with count =" ,player2_win_count)
            

    outdated_deck.append(player1[0])
    outdated_deck.append(player2[0])
    del player1[0]
    del player2[0]
    if player1 == [] or player2 == []:     
        if player1_win_count > player2_win_count:
            print("\nPlayer1 won the card game\n")
        elif player1_win_count < player2_win_count:
            print("\nPlayer2 won the card game\n")
        else:
            print("\nPlayer1 and player2 both won the card game\n")            
        break
    
for i in outdated_deck:    
    print("Outdated card deck contains -", i['Name'])        
print("\nCard game has ended.")
