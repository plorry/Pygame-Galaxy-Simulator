import gravity, pickle
from gravity import *

gravity_data = open('gravity_data.txt','r')

data = pickle.load(gravity_data)

BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 50

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480),0,32)

num = len(data[0])
bodies = generate(num-1,screen)
times = len(data)


for i in data:
	screen.fill(BLACK)
	for j in range(num):
		bodies[j].position = i[j]
		bodies[j].draw()

	pygame.display.flip()
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
			exit_game()
