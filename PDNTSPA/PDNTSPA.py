import os
import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
from game_classes import Background, Ground, Player, Enemy

pygame.init()  # Begin pygame

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Please Do Not Throw Sausage Pizza Away")

# Main Game Loop
while True:
       
    for event in pygame.event.get():
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass