import random

print('Hello! This is a guess the number game!')
print('What is your name dude?')

myname=input()
number = random.randint(1, 104)
print('hey ' +myname+ ' dude im thinking of a number between 1 and 104 and you have to guess')

guess = input()
guess =  int(guess)

print('your guess is ' +str(guess))

print('the answer is ' + str(number))