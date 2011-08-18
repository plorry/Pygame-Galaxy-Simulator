from game import *

stay_vic = 0.0
switch_vic = 0.0
stay_num = 0.0
switch_num = 0.0
switch_percent = 0
stay_percent = 0

while(True):
	result = start_game()
	if result[1]=='y':
		switch_num += 1
		if result[0]==1:
			switch_vic += 1
	else:
		stay_num += 1
		if result[0] == 1:
			stay_vic += 1
	if switch_num > 0:
		switch_percent = (switch_vic/switch_num) * 100
	if stay_num > 0:
		stay_percent = (stay_vic/stay_num) * 100
	print "You switched %i times. You stayed %i times.\n\n" % (switch_num, stay_num)
	print "When you switched, you won %.0f %% of the time." % switch_percent
	print "When you stayed, you won %.0f %% of the time.\n\n\n\n\n" %stay_percent