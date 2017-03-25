import random
		
def playgame():
	secretnum = random.randrange(1,101)
	correctguess = False
	guesscount= 0
	
	print "I'm thinking of a number between 1 and 100.\n Can you guess what it is?\n"
	print secretnum
	
	while not correctguess:
		while True:
			try:
				guess = int(raw_input("Guess a number: "))
			except ValueError:
				print("That is not a valid guess. Enter a number from 1 to 100")
			else:
				break
		correctguess = checkguess(guess, secretnum)
		guesscount += 1
		print "Guess Count: %d" % guesscount
	return
		

def checkguess(guess, secretnum):
	#print cguess
	#print csecretnum
	if guess > secretnum:
		print "Too high. Guess lower"
		return False
	elif guess < secretnum:
		print "Too low. Guess higher"
		return False
	elif guess == secretnum:
		print "Congratulations! You guessed the secret number!"
		return True
							
def keepplaying():
	playnow1 = raw_input("Would you like to play? (y or n) :")
	return playnow1

def main():
	print "Welcome to the game! \n"
	playnow = keepplaying()
	while playnow == "y":
		playgame()
		playnow	= keepplaying()
		
main()
