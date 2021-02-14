# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:08:16 2019

@author: Iraklis Kalamas
"""

def checkCard(card):
    
    n = len(card)
    if ((card[0:2] in ("34", "37")) and n == 15):
        return "AMEX"
    elif (card[0] == "4" and (n == 13 or n == 16)):
        return ("VISA")
    elif ((card[0:2] in ("51", "52", "53", "54", "55")) and n == 16):
        return ("MASTERCARD")
    else:
        return ("INVALID")


def checkSum(card):
    
    odds = ""
    evens = ""
    n = len(card)
    i = 0
    j = 1
    if (n == 16):
        while (i and j) < n:
            odds += card[i]
            i += 2
            evens += card[j]
            j += 2
    elif (n == 13 or n == 15):
        while (i and j) < n:
            odds += card[j]
            j += 2
            evens += card[i]
            i += 2
        
    odds = [int(i) for i in list(odds)]
    evens = [int(i) for i in list(evens)]

    sum_odds = sum([i//10+i%10 for i in [i*2 for i in odds]])
    sum_evens = sum(evens)
    total  = sum_odds + sum_evens
    #print(total)
    
    if (total % 10 == 0):
        print(checkCard(card))
    else:
        print("INVALID")

def main():
    num = input("Card Number: ")
    while len(num) < 2:
        num = input("Card Number: ")
    checkSum(num)

if __name__ == "__main__":
    main()
 
