import random
from math import *

def pick_door():
	return random.randint(1,3)
		
def start_game():

	winning_door = pick_door()
	door_choice = pick_door()
	revealed_door = pick_door()
	while revealed_door == winning_door or revealed_door == door_choice:
		revealed_door = pick_door()
	switch_door = pick_door()
	while revealed_door == switch_door or door_choice == switch_door:
		switch_door = pick_door()
	switch = random.randint(0,1)
	if switch == 1:
		door_choice = switch_door

	if door_choice == winning_door:
		return (1, switch)
	else:
		return(0, switch)

num_runs = int(raw_input("How many games do you want to automatically run?\n"))
print("Okay! Here I go!")
num_switch = 0.0
num_stay = 0.0
win_switch = 0.0
win_stay = 0.0
per_switch = 0.0
per_stay = 0.0
for i in range(num_runs):
	result = start_game()
	if result[1]==1:
		num_switch += 1
		if result[0]==1:
			win_switch += 1
	else:
		num_stay += 1
		if result[0] == 1:
			win_stay += 1
	if num_switch > 0:
		per_switch = (win_switch/num_switch) * 100
	if num_stay > 0:
		per_stay = (win_stay/num_stay) * 100
print "You switched %i times. You stayed %i times.\n\n" % (num_switch, num_stay)
print "When you switched, you won %.0f %% of the time." % per_switch
print "When you stayed, you won %.0f %% of the time.\n\n\n\n\n" %per_stay