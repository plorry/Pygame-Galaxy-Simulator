import gravity, pickle
from gravity import *

screen = pygame.display.set_mode((640,480),0,32)

bodies = generate(350,screen)
data = []

gravity_data = open('gravity_data.txt', 'w')
t = 0

print 'working ',
while t < 500:
	print '.',
	data.append([])
	for i in bodies:
		i.force = (0,0)
		for j in bodies:
			if j!= i:
				i.pull(j)
		i.update()
		data[t].append(i.position)
	t+=1

pickle.dump(data,gravity_data)