# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 12:42:49 2021

@author: aniruddh.phukan
"""


balance = 320000
annualInterestRate = 0.2


#########################
# Original code from bindra_k with print statements for debugging


print('\nFollowing is the output from the orignal code\n')
def limits(l,u):
    return (l+u)/2


def sheet(bal, mpr,air):
    i=0
    while i<12:
        bal = (bal-mpr)*(1+air/12)
        i = i+1
    return bal


def compute(balance, annualInterestRate):
    start0 = balance/12
    end0 = balance/12*(1+annualInterestRate)**12
    print ('From compute: Start0 = {}, End0 = {}'.format(round(start0,2), round(end0,2)))
    
    def ideal(start,end,total,air):
        guess = limits(start,end)
        x = sheet(total,guess,air)
        # print('From Ideal: start = {}, end = {}'.format(round(start,2), round(end,2)))
        print('From Ideal: balance = {}'.format(round(x,2)))

        if x > 0:
            start = guess
            print('From Ideal: Balance more than 0, updated start = {}'.format(round(start,2)))
            ideal(start,end,total,air)

        elif x <= (-0.10):   
            end = guess
            print('From Ideal: Balance less than 0, updated end = {}'.format(round(end,2)))
            ideal(start,end,total,air)

        else:
            print ('From Ideal: Balance within limit, Final guess = {}'.format(round(guess,2)))
            return round(guess,2)
            

    result = ideal(start0,end0,balance,annualInterestRate)
    print('From Compute: Result = {}'.format(result))
    return result


print('Lowest Payment: {}'.format(compute(balance,annualInterestRate)))






######################################
# Modified code keeping the print statements in


print ('\n\nFollowing is from the corrected code!\n')
def limits(l,u):
    return (l+u)/2


def sheet(bal, mpr,air):
    i=0
    while i<12:
        bal = (bal-mpr)*(1+air/12)
        i = i+1
    return bal


def compute(balance, annualInterestRate):
    start0 = balance/12
    end0 = balance/12*(1+annualInterestRate)**12
    print ('From compute: Start0 = {}, End0 = {}'.format(round(start0,2), round(end0,2)))
    
    def ideal(start,end,total,air):
        guess = limits(start,end)
        x = sheet(total,guess,air)
        # print('From Ideal: start = {}, end = {}'.format(round(start,2), round(end,2)))
        print('From Ideal: balance = {}'.format(round(x,2)))

        if x > 0:
            start = guess
            print('From Ideal: Balance more than 0, updated start = {}'.format(round(start,2)))
            return ideal(start,end,total,air) ### Added a Return statement

        elif x <= (-0.10):   
            end = guess
            print('From Ideal: Balance less than 0, updated end = {}'.format(round(end,2)))
            return ideal(start,end,total,air) ### Added a return statement

        else:
            print ('From Ideal: Balance within limit, Final guess = {}'.format(round(guess,2)))
            return round(guess,2)
            

    result = ideal(start0,end0,balance,annualInterestRate)
    print('From Compute: Result = {}'.format(result))
    return result


print('Lowest Payment: {}'.format(compute(balance,annualInterestRate)))



#########################################
# Using Richard's advice

print ('\n\nFollowing is from the modified code using Richard advice!\n')

def limits(l,u):
    return (l+u)/2


def sheet(bal, mpr,air):
    i=0
    while i<12:
        bal = (bal-mpr)*(1+air/12)
        i = i+1
    return bal


def compute(balance, annualInterestRate):
    start0 = balance/12
    end0 = balance/12*(1+annualInterestRate)**12
    print ('From compute: Start0 = {}, End0 = {}'.format(round(start0,2), round(end0,2)))
    
    def ideal(start,end,total,air):
        guess = limits(start,end)
        x = sheet(total,guess,air)
        # print('From Ideal: start = {}, end = {}'.format(round(start,2), round(end,2)))
        print('From Ideal: balance = {}'.format(round(x,2)))

        if x > 0:
            start = guess
            print('From Ideal: Balance more than 0, updated start = {}'.format(round(start,2)))
            guess = ideal(start,end,total,air) ### Added a Return statement

        elif x <= (-0.10):   
            end = guess
            print('From Ideal: Balance less than 0, updated end = {}'.format(round(end,2)))
            guess = ideal(start,end,total,air) ### Added a return statement

        else:
            print ('From Ideal: Balance within limit, Final guess = {}'.format(round(guess,2)))
            return round(guess,2)
            

    result = ideal(start0,end0,balance,annualInterestRate)
    print('From Compute: Result = {}'.format(result))
    return result


print('Lowest Payment: {}'.format(compute(balance,annualInterestRate)))