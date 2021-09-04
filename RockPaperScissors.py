#Loop

while True:
	import random
	#List
	options = ['Rock', 'Paper', 'Scissors']

	#opponent choose
	random = random.choice(options)

	#ScoreBoard
	
	#ROCK PAPER SCISSORS GAME
	ask = input('''
	1 = Rock
	2 = Paper
	3 = Scissors
	4 = Stop Game
	''')

	#Rock
	if ask == '1':
		if random == options[2]:
			print('< YOU WIN > Rock beats Scissors')
		elif random == options[0]:
			print('< ITS A DRAW > Both use rock')
		elif random == options[1]:
			print('< YOU LOST > Rock loses to Paper')
		#Paper
	elif ask == '2':
		if random == options[0]:
			print('< YOU WIN > Paper beats Rock')
		elif  random == options[1]:
			print('< ITS A DRAW > Both use paper')
		elif random == options[2]:
			print('< YOU LOST > Paper lose to scissors')
		#Scissors
	elif ask == '3':
		if random == options[0]:
			print('< YOU LOST > Scissors loses to rock')
		elif random == options[1]:
			print('< YOU WIN > Scissors beats paper')
		elif random == options[2]:
			print('< ITS A DRAW > Both use scissors')

	elif ask == "4":
		print("Good Game!")
		break
