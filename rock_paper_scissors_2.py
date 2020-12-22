#Intermediate level of rock-paper-scissors


print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("*****No Cheating!\n\n"*40)
player2 = input("Player 2, make your move: ")


if player1 == player2:
	print("Its a tie!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player 1 wins")
	elif player2 == "paper":
		print("Player 2 wins")
elif player1 == "paper":
	if player2 == "rock":
		print("Player 1 wins")
	elif player2 == "scissors":
		print("Player 2 wins")
elif player1 == "scissors":
	if player2 == "rock":
		print("Player 2 wins")
	elif player2 == "paper":
		print("Player 1 wins")
else:
	print("Something went wrong")