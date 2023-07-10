# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:19:46 2023

@author: Paris
"""

import random

def d6_roll():
    roll = random.randint(1,6)
    return roll

def snakes_and_snakes():
    tile_space = 0
    snake_counter = 0
    total_rolls = 0
    snake_dictionary = {14:-10, 17:-10,
                        31:-22, 38:-18,
                        54:-20, 59:-19,
                        62:-43, 64:-4, 67:-16,
                        81:-18, 84:-56, 87:-63,
                        91:-20, 93:-20, 95:-20, 99:-21}
    rolled_a_6 = False    
    while rolled_a_6 == False:
        roll = d6_roll()
        total_rolls += 1
        if roll == 6:
            rolled_a_6 = True
    while tile_space < 100 :
        if rolled_a_6:
            roll = d6_roll()
            total_rolls += 1
            tile_space += roll
            if tile_space in snake_dictionary:
                #print('Oops a snake')
                tile_space += snake_dictionary[tile_space]
                snake_counter += 1
                
    return total_rolls, snake_counter
        
def snakes_and_ladders():
    tile_space = 0
    snake_counter = 0
    total_rolls = 0
    snake_dictionary = {4:10, 9:22,
                        17:-10, 20:18,
                        28:56,
                        40:19,
                        51:16, 54:-20,
                        62:-43, 63:18, 64:-4,
                        71:20,
                        87:-63,
                        91:-20, 93:-20, 95:-20, 99:-21}
    rolled_a_6 = False    
    while rolled_a_6 == False:
        roll = d6_roll()
        total_rolls += 1
        if roll == 6:
            rolled_a_6 = True
    while tile_space < 100 :
        if rolled_a_6:
            roll = d6_roll()
            total_rolls += 1
            tile_space += roll
            if tile_space in snake_dictionary:
                #print("oops a snake")
                tile_space += snake_dictionary[tile_space]
                snake_counter += 1
                
    return total_rolls, snake_counter 

simulations = int(input('How Many simulations do you want?'))

snl = []
sns = []
runs = 0

while runs < simulations:
    snl.append(snakes_and_ladders()[0])
    sns.append(snakes_and_snakes()[0])
    runs += 1

average_sns = sum(sns)/len(sns)
average_snl = sum(snl)/len(snl)
print(average_sns, average_snl)