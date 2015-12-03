#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

A number guessing game demonstration program.

"""

from os import system
import random

high = 100
secret_num = random.randint(1, high)
while True:
    guess = input("Give me a random number between 1 and %s: \n" % high)
    if guess == secret_num:
        print "You got it!"
        system('say Ding Ding Ding We got a winner')
        break
    elif guess > secret_num:
        print "That's too high. Try again!"
        system('say Wah Wah Womp Womp')
    else:
        print "That's too low. Try again!"
        system("say Too bad, so sad, you got it wrong.")
