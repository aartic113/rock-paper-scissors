# Advanced version of rock-paper-scissors
from random import randint


player_wins = 0
computer_wins = 0
wining_score = 3

while player_wins < wining_score and computer_wins < wining_score:
	print(f"Player score: {player_wins} Computer score: {computer_wins}")
	print("Rock...")
	print("Paper...")
	print("Scissors...")

	player = input("Player, make your move: ").lower()
	if player == "quit" or player == "q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}")


	if player == computer:
		print("Its a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("Player wins")
			player_wins += 1
		else:
			print("computer wins")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("Player wins")
			player_wins += 1
		else:
			print("Computer wins")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("Player wins")
			player_wins += 1
		else:
			print("Computer wins")
			computer_wins += 1
	else:
		print("Something went wrong")
if player_wins > computer_wins:
	print("CONGRATS YOU WON!")
elif player_wins == computer_wins:
	print("YAY! YOU BOTH WON!!!")
else:
	print("OH NO, COMPUTER WINS :(")




