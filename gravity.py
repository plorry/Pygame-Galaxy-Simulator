import pygame, math, sys, random
from pygame.locals import *
from math import *

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)



class Body():
	def __init__(self, screen, radius, mass, position, velocity = (0,0)):
		self.screen = screen
		self.radius = radius
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.force = (0,0)
		self.accel = (0,0)
		
	def update_force(self):
		self.accel = (self.force[0]/self.mass,self.force[1]/self.mass)
		self.velocity = (self.velocity[0]+self.accel[0],self.velocity[1]+self.accel[1])
		self.position = (self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
		
	def pull(self, other):
		dy = other.position[1] - self.position[1]
		dx = other.position[0] - self.position[0]
		radius = math.sqrt(dy**2 + dx**2)
		if radius > 50:
			vec = (dx/radius, dy/radius)
			force_strength = self.mass*other.mass/(radius**2)
			self.force = (self.force[0]+force_strength*vec[0],self.force[1]+force_strength*vec[1])
		
	def update(self):
		self.update_force()
		"""
		if self.position[0] > 64000:
			self.position = (0,self.position[1])
		if self.position[0] < 0:
			self.position = (64000, self.position[1])
		if self.position[1] > 48000:
			self.position = (self.position[0],0)
		if self.position[1] < 0:
			self.position = (self.position[0],48000)
		"""
		pygame.draw.circle(self.screen,WHITE,(self.position[0]/100,self.position[1]/100),self.radius)
		
	def draw(self):
		pygame.draw.circle(self.screen,WHITE,(self.position[0]/100,self.position[1]/100),self.radius)
		
def exit_game():
	sys.exit()
	
def generate(num, screen):
	bodies = [Body(screen,5,900000000,(31000,23000),(0,0))]
	#bodies = []
	for i in range(1,num+1):
		bodies.append(Body(screen,2,300000,(random.randint(8000,56000),random.randint(8000,40000))))
		bodies[i].velocity=((bodies[i].position[1]-24000)/100,(0-bodies[i].position[0]+32000)/100)
	
	return bodies
	
if __name__=='__main__':
	screen = pygame.display.set_mode((640,480),0,32)
	pygame.init()
	clock = pygame.time.Clock()
	bodies = generate(40,screen)
	
	while 1:
		clock.tick(50)
		screen.fill(BLACK)
		
		for i in bodies:
			i.force=(0,0)
			for j in bodies:
				if i!= j:
					i.pull(j)

			i.update()

		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
				exit_game()