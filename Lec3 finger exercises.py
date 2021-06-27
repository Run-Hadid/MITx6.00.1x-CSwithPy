# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:29:33 2021

@author: aniruddh.phukan
"""


# Guess my number for bisection

smallest = 0
largest = 100
guess = int((smallest+largest)/2)
score = input("Please think of a number between 0 and 100. \nIs your number = {}? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.".format(guess))

while score != 'c':

    if score == 'h':
        largest = guess
        guess = int((smallest + largest)/2)
    elif score == 'l':
        smallest = guess
        guess = int((smallest + largest)/2)
    else:
        print('Sorry, I did not understand your input.')
    
    score = input("Is your number = {}? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.".format(guess))

print('Game over. Your secret number was: {}'.format(guess))