import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import random
import pygame
from settings import *
from sprites import *
from pygame.locals import *

road = pygame.transform.scale(pygame.image.load("road.png"), (WIDTH-((WIDTH/36)*2), HEIGHT*2))
car = pygame.transform.scale(pygame.image.load("car.png"), (CAR_WIDTH, CAR_HEIGHT))
arrow = pygame.transform.scale(pygame.image.load("arrows.png"), (400, 400))
rival = pygame.transform.scale(pygame.image.load("rival.png"), (CAR_WIDTH, CAR_HEIGHT))
rival2 = pygame.transform.scale(pygame.image.load("rival2.png"), (CAR_WIDTH, CAR_HEIGHT))
rival3 = pygame.transform.scale(pygame.image.load("rival3.png"), (CAR_WIDTH, CAR_HEIGHT))
rival4 = pygame.transform.scale(pygame.image.load("rival4.png"), (CAR_WIDTH, CAR_HEIGHT))
rival5 = pygame.transform.scale(pygame.image.load("rival5.png"), (CAR_WIDTH, CAR_HEIGHT))
rival6 = pygame.transform.scale(pygame.image.load("rival6.png"), (CAR_WIDTH, CAR_HEIGHT))
rival7 = pygame.transform.scale(pygame.image.load("rival7.png"), (CAR_WIDTH, CAR_HEIGHT))
background = pygame.transform.scale(pygame.image.load("BG3.jpeg"), (WIDTH, HEIGHT))
button = pygame.transform.scale(pygame.image.load("Button.png"), (320, 100))
buttonp = pygame.transform.scale(pygame.image.load("Button react.png"), (320, 100))
framehs = pygame.transform.scale(pygame.image.load("frame.png"), (600, 900))
RIVAL_LIST = [rival, rival2, rival3, rival4, rival5, rival6, rival7]
framehss = pygame.transform.scale(framehs, (600, 500))



