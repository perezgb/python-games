import random

print('Hello! This is a guess the number game!')
print('What is your name?')

start = 1
end = 20

myname=input()
number = random.randint(start, end)
guessesTaken = 0

print('Hey ' +myname+ ' I am thinking of a number between ' +str(start)+' and ' +str(end))

for guessesTaken in range(5):
    print('Take a guess!')
    guess = input()
    guess= int(guess)
 
    if guess < number:
        print('Higher!')
    
    if guess > number:
        print('Lower...')    

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Congrats! ' +myname+ ', you guessed my number in ' +guessesTaken+ ' guesses!')

if guess != number:
    number = str(number)
    print('Boohoo! Your guesses are over, and the number I was thinking of was' +number+ '.')