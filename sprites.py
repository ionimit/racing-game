import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import random
import pygame
import images
from settings import *
#from images import *
from game import *
from pygame.locals import *
from kivy.vector import Vector as vec
#vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = images.car
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT - 280)
		self.pos = vec(WIDTH/2, HEIGHT - 280)
		self.vel = vec(0, 0)
		
	def update(self):
		self.pos += self.vel
		self.rect.center = self.pos
		if self.rect.x <= 0:
			self.vel.x = 0
			self.rect.x = 0
		if self.rect.x >= WIDTH - self.rect.w:
			self.vel.x = 0
			self.rect.x = WIDTH - self.rect.w
		if self.rect.y <= 0:
			self.vel.y = 0
			self.rect.y = 0
		if self.rect.y >= HEIGHT - self.rect.h - 40:
			self.vel.y = 0
			self.rect.y = HEIGHT - self.rect.h - 40
			

class Rival(Player):
	def __init__(self, image):
		Player.__init__(self)
		self.image = image
		self.pos = vec(random.randrange(40, WIDTH - 40), random.randrange(-HEIGHT*2, -self.rect.y))
		self.vel = vec(0,(random.randrange(3, 10)))
		
	def update(self):
		self.pos += self.vel
		self.rect.center = self.pos
		if self.rect.y  >= HEIGHT:
			self.pos = vec(random.randrange(40, WIDTH - 40), random.randrange(-HEIGHT*3, -self.rect.y))

