#!/usr/bin/env python3
import random


secret_number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')
print('You have 5 guesses left.')

guessed_number = 0
number_of_guesses = 5
play_again = 'yes'

while (guessed_number != secret_number and play_again == 'yes') :
    if number_of_guesses == 0:
        print('you ran out of guesses!')
        play_again = input('Whatn to play again?')
        play_again = play_again.lower()
        if play_again == 'yes':
            number_of_guesses = 5
        else:
            break
    guessed_number = int(input('What\'s the number?'))
    number_of_guesses -= 1
    if guessed_number != secret_number:
        print('Nope, try again!')
    if guessed_number > secret_number:
        print(guessed_number, ' is too high.')
        print('You have {} guesses left'.format(number_of_guesses))
    elif guessed_number < secret_number:
        print(guessed_number, ' is too low.')
        print('You have {} guesses left'.format(number_of_guesses))
    else:
        print('Yes! You win!')
        play_again = input('Want to play again? -FINAL')
        play_again = play_again.lower()
        if play_again == 'yes':
            number_of_guesses = 5
            print('***value of play_again is ', play_again)
        else:
            break
        
