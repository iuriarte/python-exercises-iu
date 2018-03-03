#!/usr/bin/env python3

coins = 0
want_coins = 'yes'
while want_coins == 'yes':
    print("You have {} coins".format(coins))
    want_coins=input("Do you want another? ")
    want_coins=want_coins.lower()
    coins += 1

print("Bye")