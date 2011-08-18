import random
from math import *

def pick_door():
	return random.randint(1,3)
		
def start_game():

	winning_door = pick_door()
	door_choice = int(raw_input("\n\n\n\n\n\n\n\n\n\nPick a door: 1 - 2 - 3\n"))
	revealed_door = pick_door()
	while revealed_door == winning_door or revealed_door == door_choice:
		revealed_door = pick_door()
	switch_door = pick_door()
	while revealed_door == switch_door or door_choice == switch_door:
		switch_door = pick_door()
	print "Door %i is NOT the winner. You chose Door %i. Would you like to switch to Door %i?" % (revealed_door, door_choice, switch_door)
	switch = raw_input( "(Y/N)" )
	if switch == 'y':
		door_choice = switch_door
	if door_choice == winning_door:
		print("You win!\n\n\n\n")
		return (1, switch)
	else:
		print("You lose!\n\n\n\n")
		return(0, switch)
		