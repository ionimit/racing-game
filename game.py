import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import random
import pygame
import time
import highscore
from settings import *
from sprites import *
from images import *
from pygame.locals import *


class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		
	def new(self):
		self.all_sprites = pygame.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		self.run()
		
	def run(self):
		global score
		self.playing = True
		self.rival = [Rival(random.choice(RIVAL_LIST))]
		while self.playing:
			self.clock.tick(FPS)
			if (score // 250) + 12 > len(self.rival):
				self.rival.append(Rival(random.choice(RIVAL_LIST)))
			for j in range(len(self.rival)):
				self.all_sprites.add(self.rival[j])
				self.rival[j].update()
			self.events()
			self.draw()
			self.update()
			score += 1


	def update(self):
		global road_starty
		self.player.update()
		self.all_sprites.update()
		road_starty += road_speed
		if road_starty >= 0:
			road_starty = -HEIGHT
		for i in range(len(self.rival)):
			if pygame.sprite.collide_rect_ratio(0.85)(self.rival[i], self.player):
				self.crash()
			for k in self.rival:
				if self.rival[i] != k:
					if pygame.sprite.collide_rect_ratio(1.12)(self.rival[i], k):
						k.pos.x += (k.pos.x - self.rival[i].pos.x)/6
						if k.pos.x - self.rival[i].pos.x == 0:
							k.pos.x += (k.rect.w)/6

						
	def message_display(self, txt, color, pos, size):
		myfont = pygame.font.SysFont("DejaVuSans", size)
		self.label = myfont.render(txt, 1, color)
		self.screen.blit(self.label, pos)

						
	def crash(self):
		global score, LIVES
		self.playing = False
		LIVES += -1
		if LIVES < 0:
			self.message_display("Game Over", black, (160, 640), 70)
			time.sleep(1)
			highscore.highscore(self.screen, file_name, score)
			score = 0
			LIVES = 3
		else:
			self.message_display("Crashed", black, (240, 640), 70)
		pygame.display.flip()
		time.sleep(1)
		self.new()
		
	def events(self):
		global PAUSE
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False
				
			if event.type == FINGERMOTION:
				touch_pos = [event.x * WIDTH, event.y * HEIGHT]
				if 1150 > touch_pos[1] > 1015:
					if touch_pos[0] > WIDTH - 130:
						self.player.vel.x = PLAYER_VEL
					if 450 > touch_pos[0] > 320:
						self.player.vel.x = -PLAYER_VEL
				if 590 > touch_pos[0] > 450:
					if touch_pos[1] > 1150:
						self.player.vel.y = PLAYER_VEL
					if 1015 > touch_pos[1] > 880:
						self.player.vel.y = -PLAYER_VEL
				if 800 > touch_pos[1]:
					PAUSE = True
					self.pause()
			if event.type == FINGERUP:
				self.player.vel = vec(0, 0)
				#print(event.fingerId)
#				touch_pos = [event.x * WIDTH, event.y * HEIGHT]
#				if self.player.vel.x != 0:
#					if 1150 > touch_pos[1] > 1015:
#						if touch_pos[0] > 520:
#							if self.player.vel.x > 0:
#								self.player.vel.x += -PLAYER_VEL
#						if 520 > touch_pos[0] > 320:
#							if self.player.vel.x < 0:
#								self.player.vel.x += PLAYER_VEL
#				if self.player.vel.y != 0:
#					if 590 > touch_pos[0] > 450:
#						if 1080 > touch_pos[1] > 880:
#							if self.player.vel.y < 0:
#								self.player.vel.y += PLAYER_VEL
#						if touch_pos[1] > 1080:
#							if self.player.vel.y > 0:
#								self.player.vel.y += -PLAYER_VEL
		
	def draw(self):
		self.screen.fill(green)
		self.screen.blit(road, (WIDTH/36, road_starty))
		self.all_sprites.draw(self.screen)
		self.screen.blit(arrow, (320, 880))
		self.message_display("score: " + str(score), black, (10, 0), 60)
		self.message_display("lives: " + str(LIVES), black, (500, 0), 60)
		pygame.display.flip()
		
		
	def show_start_screen(self):
		while self.running:
			for ev in pygame.event.get():
				if ev.type == FINGERDOWN:
					self.show_menu_screen()
			self.screen.blit(background, (0, 0))
			self.message_display("tap to continue", white, (140, 1100), 60)
			pygame.display.flip()
			
		
	def show_menu_screen(self):
		global score, LIVES
		while self.running:
			for ev in pygame.event.get():
				if ev.type == FINGERDOWN:
					touch_pos = [ev.x * WIDTH, ev.y * HEIGHT]
					if 340 > touch_pos[0] > 20:
						if 1100 > touch_pos[1] > 1000:
							self.screen.blit(buttonp, (20, 1000))
							self.message_display("Play", white, (130, 1020), 50)
							pygame.display.flip()
							score = 0
							LIVES = 3
							self.new()
							
					if 700 > touch_pos[0] > 380:
						if 1100 > touch_pos[1] > 1000:
							self.screen.blit(buttonp, (380, 1000))
							self.message_display("High Score", white, (405, 1020), 50)
							pygame.display.flip()
							self.show_high_score()
#					if 700 > touch_pos[0] > 380:
						if 1220 > touch_pos[1] > 1020:
							self.screen.blit(buttonp, (380, 1120))
							self.message_display("Quit", white, (490, 1140), 50)
							pygame.display.flip()
							sys.exit()
							
			self.screen.blit(background, (0, 0))
			self.screen.blit(button, (20, 1000))
			self.screen.blit(button, (380, 1000))
			self.screen.blit(button, (20, 1120))
			self.screen.blit(button, (380, 1120))
			self.message_display("Play", white, (130, 1020), 50)
			self.message_display("High Score", white, (405, 1020), 50)
			self.message_display("Settings", white, (80, 1140), 50)
			self.message_display("Quit", white, (490, 1140), 50)
			pygame.display.flip()
			
	def show_high_score(self):
		highscore.show_top10(self.screen, file_name, False)
		
	def unpause(self):
		global PAUSE
		PAUSE = False
		
	def pause(self):
		global score, LIVES
		while PAUSE:
			self.message_display("Paused", black, (240, 500), 70)
			self.screen.blit(button, (20, 1000))
			self.screen.blit(button, (380, 1000))
			self.screen.blit(button, (20, 1120))
			self.screen.blit(button, (380, 1120))
			self.message_display("New Game", white, (45, 1020), 50)
			self.message_display("Continue", white, (425, 1020), 50)
			self.message_display("Settings", white, (80, 1140), 50)
			self.message_display("Quit", white, (490, 1140), 50)
			pygame.display.flip()
			
			for ev in pygame.event.get():
				if ev.type == FINGERDOWN:
					touch_pos = [ev.x * WIDTH, ev.y * HEIGHT]
					if 340 > touch_pos[0] > 20:
						if 1100 > touch_pos[1] > 1000:
							self.screen.blit(buttonp, (20, 1000))
							self.message_display("New Game", white, (45, 1020), 50)
							pygame.display.flip()
							score = 0
							LIVES = 3
							self.new()
							
					if 700 > touch_pos[0] > 380:
						if 1100 > touch_pos[1] > 1000:
							self.screen.blit(buttonp, (380, 1000))
							self.message_display("Continue", white, (425, 1020), 50)
							pygame.display.flip()
							self.run()
#					if 700 > touch_pos[0] > 380:
						if 1220 > touch_pos[1] > 1020:
							self.screen.blit(buttonp, (380, 1120))
							self.message_display("Quit", white, (490, 1140), 50)
							pygame.display.flip()
							sys.exit()
			
		
		
g = Game()


def start_game():
	g.show_start_screen()
