import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
import sys
import game
from images import *
from settings import *


def message_display(screen, txt, color, pos, size):
		myfont = pygame.font.SysFont("DejaVuSans", size)
		label = myfont.render(txt, 1, color)
		screen.blit(label, pos)
		pygame.display.flip()
		
def read_from_file_and_find_highscore(file_name):
	file = open(file_name, 'r')
	lines=file.readlines()
	file.close()
	all_score = []
	for line in lines:
		sep = line.index(' - ')
		name = line[:sep]
		score = int(line[sep+3:])
		all_score.append((score, name))
	all_score.sort(reverse=True)  # sort from largest to smallest
	high_score = all_score[0][0]
	high_name = all_score[0][1]
	return high_name, high_score


def write_to_file(file_name, your_name, points):
	score_file = open(file_name, 'a')
	score_file.write(your_name+" - "+str(points))
	score_file.write("\n")
	score_file.close()


def show_top10(screen, file_name, ingame):
	file = open(file_name, 'r')
	lines=file.readlines()
	all_score = []
	for line in lines:
		sep = line.index(' - ')
		name = line[:sep]
		score = int(line[sep+3:])
		all_score.append((score, name))
		file.close()
	all_score.sort(reverse=True)  # sort from largest to smallest
	best = all_score[:10]
	screen.blit(background, (0, 0))
	screen.blit(framehs, (60, 40))
	message_display(screen, "High Score", black, (120, 150), 90)
	if ingame:
		screen.blit(button, (20, 1100))
		screen.blit(button, (380, 1100))
		message_display(screen, "Play Again", white, (50, 1120), 50)
		message_display(screen, "Main Menu", white, (405, 1120), 50)
	else:
		message_display(screen, "tap to continue", white, (100, 1120), 70)
	for i, entry in enumerate(best):
		message_display(screen, entry[1] + "  " + str(entry[0]), black, (120, 55*i+280), 55)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.FINGERDOWN:
				touch_pos = [event.x * WIDTH, event.y * HEIGHT]
				if ingame:
					if 1200 > touch_pos[1] > 1100:
						if 340 > touch_pos[0] > 20:
							screen.blit(buttonp, (20, 1100))
							message_display(screen, "Play Again", white, (50, 1120), 50)
							return
						if 700 > touch_pos[0] > 380:
							screen.blit(buttonp, (380, 1100))
							message_display(screen, "Main Menu", white, (405, 1120), 50)
							#pygame.quit()
							game.g.show_start_screen()
				else:
					game.start_game()
			game.g.clock.tick(FPS)
				

def enterbox(screen, txt, txt2, txt3):
	font = pygame.font.SysFont("DejaVuSans", 30)
	def blink(screen):
		for color in [black, white]:
			pygame.draw.rect(screen, color, (300, 251, 1, 28))
			pygame.display.flip()
			pygame.time.wait(300)
	def show_name(screen, name):
		pygame.draw.rect(screen, white, (120, 250, 400, 30), 0)
		txt_surf = font.render(name, True, black)
		txt_rect = txt_surf.get_rect(center=(300, 265))
		screen.blit(txt_surf, txt_rect)
		pygame.display.flip()
	screen.blit(framehss,(60, 40))
	screen.blit(button, (200, 350))
	message_display(screen, "Submit", white, (270, 370), 50)
	message_display(screen, txt, black, (120, 100), 35)
	message_display(screen, txt2, black, (120, 145), 35)
	message_display(screen, txt3, black, (120, 190), 35)
	name = ""
	show_name(screen, name)
	pygame_sdl2.key.start_text_input()

    # the input-loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.TEXTINPUT:
				input = str(event.text)
				name = name + input
			elif event.type == KEYDOWN:
				if event.key == 8:
					name = name[:-1]
			elif event.type == FINGERDOWN:
				touch_pos = [event.x * WIDTH, event.y * HEIGHT]
				if 450 > touch_pos[1] > 350:
					if 520 > touch_pos[0] > 200:
						pygame_sdl2.key.start_text_input()
				if 500 > touch_pos[1] > 300:
					if 520 > touch_pos[0] > 120:
						screen.blit(buttonp, (200, 350))
						message_display(screen, "Submit", white, (270, 370), 50)
						pygame.display.flip()
						pygame_sdl2.key.stop_text_input()
						return name
						
		if name == "":
			blink(screen)
		show_name(screen, name)
		

def highscore(screen, file_name, your_points):
	high_name, high_score = read_from_file_and_find_highscore(file_name)
	if your_points > high_score:
		your_name = enterbox(screen, "YOU HAVE BEATEN", "THE HIGHSCORE - ", "What is your name?")
	elif your_points <= high_score:
		st1 = "Highscore is " + str(high_score)
		st2 = "made by " + high_name
		st3 = "What is your name?"
		your_name = enterbox(screen, st1, st2, st3)
	if your_name == None or len(your_name) == 0:
		return  # do not update the file unless a name is given
	write_to_file(file_name, your_name, your_points)
	show_top10(screen, file_name, True)
	return