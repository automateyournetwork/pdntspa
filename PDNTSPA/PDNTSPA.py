import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *
 
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
 
# Create the display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Please Do Not Throw Sausage Pizza Away")
 
 
# Run animation for the RIGHT
run_ani_R = [pygame.image.load("images/Player_Sprite_R.png"), pygame.image.load("images/Player_Sprite2_R.png"),
             pygame.image.load("images/Player_Sprite3_R.png"),pygame.image.load("images/Player_Sprite4_R.png"),
             pygame.image.load("images/Player_Sprite5_R.png"),pygame.image.load("images/Player_Sprite6_R.png"),
             pygame.image.load("images/Player_Sprite_R.png")]
 
# Run animation for the LEFT
run_ani_L = [pygame.image.load("images/Player_Sprite_L.png"), pygame.image.load("images/Player_Sprite2_L.png"),
             pygame.image.load("images/Player_Sprite3_L.png"),pygame.image.load("images/Player_Sprite4_L.png"),
             pygame.image.load("images/Player_Sprite5_L.png"),pygame.image.load("images/Player_Sprite6_L.png"),
             pygame.image.load("images/Player_Sprite_L.png")]
 
 

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("images/Background.png")
            self.rectBGimg = self.bgimage.get_rect()        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))      
 
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Ground.png")
        self.rect = self.image.get_rect(center = (350, 350))
        self.bgX1 = 0
        self.bgY1 = 285
 
    def render(self):
        displaysurface.blit(self.image, (self.bgX1, self.bgY1)) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player_Sprite_R.png")
        self.rect = self.image.get_rect()
 
        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"
 
        # Movement 
        self.jumping = False
        self.running = False
        self.move_frame = 0
 
 
    def move(self):
          # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
          self.acc = vec(0,0.5)
 
          # Will set running to False if the player has slowed down to a certain extent
          if abs(self.vel.x) > 0.3:
                self.running = True
          else:
                self.running = False
 
          # Returns the current key presses
          pressed_keys = pygame.key.get_pressed()
 
          # Accelerates the player in the direction of the key press
          if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
          if pressed_keys[K_RIGHT]:
                self.acc.x = ACC 
 
          # Formulas to calculate velocity while accounting for friction
          self.acc.x += self.vel.x * FRIC
          self.vel += self.acc
          self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
 
          # This causes character warping from one point of the screen to the other
          if self.pos.x > WIDTH:
                self.pos.x = 0
          if self.pos.x < 0:
                self.pos.x = WIDTH
         
          self.rect.midbottom = self.pos  # Update rect with new pos            
 
    def gravity_check(self):
          hits = pygame.sprite.spritecollide(player ,ground_group, False)
          if self.vel.y > 0:
              if hits:
                  lowest = hits[0]
                  if self.pos.y < lowest.rect.bottom:
                      self.pos.y = lowest.rect.top + 1
                      self.vel.y = 0
                      self.jumping = False
 
 
    def update(self):
          # Return to base frame if at end of movement sequence 
          if self.move_frame > 6:
                self.move_frame = 0
                return
 
          # Move the character to the next frame if conditions are met 
          if self.jumping == False and self.running == True:  
                if self.vel.x > 0:
                      self.image = run_ani_R[self.move_frame]
                      self.direction = "RIGHT"
                else:
                      self.image = run_ani_L[self.move_frame]
                      self.direction = "LEFT"
                self.move_frame += 1
 
          # Returns to base frame if standing still and incorrect frame is showing
          if abs(self.vel.x) < 0.2 and self.move_frame != 0:
                self.move_frame = 0
                if self.direction == "RIGHT":
                      self.image = run_ani_R[self.move_frame]
                elif self.direction == "LEFT":
                      self.image = run_ani_L[self.move_frame]
 
    def attack(self):
          pass
 
    def jump(self):
        self.rect.x += 1
 
        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)
         
        self.rect.x -= 1
 
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -12
       
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
  
       
     
player = Player()
Playergroup = pygame.sprite.Group()
 
background = Background()
 
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
 
 
while True:
    player.gravity_check() 
       
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
              if event.key == pygame.K_SPACE:
                    player.jump()
         
    # Player related functions        
    player.update()         
    player.move()
     
    # Display and Background related functions 
    background.render()
    ground.render()
     
    # Rendering Player
    displaysurface.blit(player.image, player.rect)
 
    pygame.display.update()      
    FPS_CLOCK.tick(FPS)