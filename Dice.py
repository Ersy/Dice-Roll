# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 23:59:36 2016

@author: Ers
"""

import random

def rollDice():
    return (random.randint(1, 6))


correct = 0

running = True

while running:

    try:
        rounds = int(input("Enter the number of rounds "))
    except ValueError:
        print ("Please enter a number")
        continue
    else:
        break
    

    
    
while rounds > 0:
    
    try:    
        guess = int(input("Guess a number between 1 and 6 "))
    except ValueError:
        print ("Please enter a number")
        continue
    answer = rollDice()
    if guess == answer:
        print ("The dice roll was ",answer)
        print ("You were correct!")
        correct += 1
        rounds -= 1
    else:
        print ("The dice rolls ", answer)
        print ("You were wrong!")
        rounds -= 1

print ("You were correct ",correct, " times!")
