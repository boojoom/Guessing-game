import sys
import random

def game():
	rand = random.randint(1,9)
	guess = 0
	c = 0
	while guess != rand:
		guess = int(input("Enter a number between 1 and 9: "))
		if guess < rand:
			print('Too low value. Try again!')
		elif guess > rand:
			print('Too high value. Try again!')
		if guess == rand:
			c = int(guess)
			print('Correct! You guessed the number in', c ,'times!')
game()
cont = str(input('Do you want to continue?[Yes/No]: '))
if cont == 'No':
	sys.exit()
while cont == 'Yes':
	game()
	cont = str(input('Do you want to continue?[Yes/No]: '))
