# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 01:27:37 2021

@author: aniruddh.phukan
"""

import time

startTime = time.process_time()


balance = 999999
annualInterestRate = 0.18
monthlyPaymentRate = 0.04
# emi = 303.325


# Problem 1

def balance_remaining(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        balance = (balance - monthlyPaymentRate*balance)*(1+annualInterestRate/12)
        print('Month {}, Remaining Balance = {}'.format(i,format(balance,'.2f')))
        
    return format(balance,'.2f')

def balance_remaining_emi(balance, annualInterestRate, emi):
    for i in range(12):
        balance = (balance - emi)*(1+annualInterestRate/12)
        print('Month {}, Remaining Balance = {}'.format(i,format(balance,'.2f')))
        
    return format(balance,'.2f')



# balance = balance_remaining(balance, annualInterestRate, monthlyPaymentRate)
# print('Remaining balance: {}'.format(balance))

# balance = balance_remaining_emi(balance, annualInterestRate, emi)
# balance


# Problem 2

def lowest_payment(balance, annualInterestRate):
    emi = round(balance/12)
    starting_balance = balance
    
    limit = 0.1
    
    while balance>limit:
        emi += 1
        balance = starting_balance
        for i in range(12):
            balance = (balance - emi)*(1+annualInterestRate/12)
                
    return format(format(round((emi+5)/10)*10,'.2f'))
    


# emi = lowest_payment(balance, annualInterestRate)
# print('Lowest Payment: {}'.format(emi))

# endTime = time.process_time()
# print('Elapsed Time = {}'.format(endTime-startTime))


# Problem 2 : Less steps

def lowest_payment(balance, annualInterestRate):
    emi = round(balance/120)*10
    starting_balance = balance
    
    limit = 1
    
    while balance>limit:
        emi += 10
        balance = starting_balance
        for i in range(12):
            balance = (balance - emi)*(1+annualInterestRate/12)
        
        
    return format(format(emi,'.2f'))
    

# emi = lowest_payment(balance, annualInterestRate)
# print('Lowest Payment: {}'.format(emi))

# endTime = time.process_time()
# print('Elapsed Time = {}'.format(endTime- startTime))


# Problem 3

def remaining_balance(balance, annualInterestRate, emi):
    remainingBalance = (balance - emi) * (1+annualInterestRate/12)
    return remainingBalance

def lowest_payment_bisection(balance, annualInterestRate):
    startingBalance = balance
    guessCount = 0
    
    lowestEMI = startingBalance/12 # Assuming interest rates will never be negative
    highestEMI = (startingBalance * (1+annualInterestRate/12)**12)/12
    
    emi = lowestEMI
    limit = 0.01
        
    while abs(balance) > limit:
        balance = startingBalance
        for i in range(12):
            balance = remaining_balance(balance, annualInterestRate, emi)
        
        print ('Guess Count = {}, LEMI = {}, HEMI = {}, Guess EMI = {}, Balance = {}'.format(guessCount, lowestEMI, highestEMI, format(emi,'.2f'), format(balance,'.2f')))
        if balance > limit:
            # print('Old LEMI = {}, Old HEMI ={}'.format(lowestEMI,highestEMI))
            lowestEMI = emi
            emi = (lowestEMI + highestEMI)/2
            # print('New LEMI = {}, New HEMI ={}'.format(lowestEMI,highestEMI))
        elif balance < limit:
            # print('Old LEMI = {}, Old HEMI ={}'.format(lowestEMI,highestEMI))
            highestEMI = emi
            emi = (lowestEMI + highestEMI)/2
            # print('New LEMI = {}, New HEMI ={}'.format(lowestEMI,highestEMI))
        else:
            break
        
        guessCount += 1
        
    return format(emi, '.2f')

# emi = lowest_payment_bisection(balance, annualInterestRate)
# print('Lowest Monthly Payment: {}'.format(emi))

# endTime = time.process_time()
# print('Elapsed Time = {}'.format(endTime-startTime))





############################################
# Other solutions


# Kiwitrader # Problem 1 # List Comprehension

# b, r, p = [balance], annualInterestRate/12, monthlyPaymentRate
# c = [b.append(b[-1] * (1-p) * (1+r)) for _ in range(12)] and round(b[-1],2)
# print('Remaining Balance: {}'.format(c))

# endTime = time.process_time()
# print('Elapsed Time = {}'.format(endTime - startTime))


# Kiwitrader # Problem 2

# r = annualInterestRate/12
# minp = balance / 12
# maxp = (balance * (1 + r)**12) / 12

# while True:
#     p = (minp + maxp) / 2
#     b = balance
#     for _ in range(12):
#         b = ((b-p) * (1+r))
#     if b <= -0.12:
#         maxp = p
#     elif b > 0:
#         minp = p
#     else:
#         break

# print("Lowest Payment: ", round(p, 2))

# endTime = time.process_time()
# print('Elapsed time = {}'.format(endTime-startTime))
    




# Richard_b_uk # Problem 2 # Recursion

# def annualRun(bal, pay):
#     for month in range(12):
#         bal -= pay
#         bal *= (1 + annualInterestRate/12)
#         bal = round(bal, 2)
#     if bal <= 0:
#         return int(pay)
#     else:
#         return annualRun(balance, pay + 10)

# print ("Lowest payment:", annualRun(balance, 10))
    



# amhyf # Problem 3
    
# newbal = balance
# lowerbound = balance/12
# upperbound = (balance*(1+(annualInterestRate/12))**12)/12
# guess = (upperbound+lowerbound)/2    
# while newbal > 0:
#     for i in range(12):
#         newbal = (newbal - guess)*(1+(annualInterestRate/12))
#     if newbal > 0:
#         lowerbound = guess      
#     elif newbal < 0:
#         upperbound = guess
#     guess  = (upperbound + lowerbound)/2
#     newbal = balance
#     if round(lowerbound,8) == round(upperbound,8) or round(lowerbound+0.000000005,8)==round(upperbound,8):
#         break
# print('Lowest Payment: ' + str(round(guess,2)))

# endTime = time.process_time()
# print('Elapsed Time = {}'.format(endTime-startTime))
    



