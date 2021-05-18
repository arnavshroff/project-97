Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> print("Let's Play The Number Guessing Game")
Let's Play The Number Guessing Game
>>> number = random.randint(1,9)
>>> chances = 0
>>> print("Guess A Number Between 1 To 9")
Guess A Number Between 1 To 9
>>> while chances < 5:
	guess = int(input("Enter The Guess: "))
	if guess == number:
		print("Congrats! You Won The Game")
		break
	elif guess < number:
		print("Your Guess Is Too Low. Guess A Number Higher Than This")
	else:
		print("Your Guess Is Too High. Guess A Number Lower Than This")
	chances = chances+1
	if chances==5 and guess!= number:
		print("You Lose. Better Luck Next Time!")

		
Enter The Guess: 5
Your Guess Is Too High. Guess A Number Lower Than This
Enter The Guess: 2
Your Guess Is Too High. Guess A Number Lower Than This
Enter The Guess: 1
Congrats! You Won The Game
>>> 