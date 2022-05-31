# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:26:40 2022

@author: Sergi
"""

'''
This code was presented as part of a hiring process. The exercise consisted in computing the change of a purchase and returning it in the optimal way
given a series of available coin denominations.
'''

def getChange(amount, price):
    '''
    This function computes the coins needed to give back the change optimally.
    
    Input
    amount: float. amount of money received
    price: float. price of the purchased item
    
    Output
    coin_hist: list. amount of coins of each denomination needed to give back the change.
    '''
    change = amount-price
    coins = [0.01, 0.05, 0.10, 0.20, 0.50, 1.00] #Available coin values
    coin_hist = [0 for i in range(0,6)] #Histogram of needed coins
    i=-1 #Start at the largest coin denomination
    while change < coins[i]: #Checks the largest denomination we can start from
        i = i-1
    while change != 0: 
        coin_hist[i] += 1 #Adds one coin at a time
        change = change - coins[i]
        change = round(change, 2) #Prevents rounding errors in the updated change
        try:
            while change < coins[i]:
                #Step down to smaller denomination when we can't keep substracting
                i = i-1
        except IndexError:
        #If we let it run it would give an error because the index is out of the list
            break
    return coin_hist

print(getChange(5, 0.99))
print(getChange(3.14, 1.99))
print(getChange(4, 3.14)) 
'''
Coding time: aprox. 30 min
Difficulty: easy
'''
