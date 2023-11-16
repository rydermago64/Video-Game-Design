# This file was created by: Ryder Magobet

# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings

# how big the game window is when you play the game
WIDTH = 1024
HEIGHT = 768
FPS = 30

# player settings

# how fast the player may fun, how high he can jump, and the gravity
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors

# the rgb is from online sources
WHITE = (255, 234, 0)
BLACK = (0, 0, 0)
RED = (255,20,147)
GREEN = (0,0,255)
BLUE = (0, 0, 255)

# how the platefroms are placed, and how big they are in my game 
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal"),
                 (175, 35, 25, 20, "moving"),
                 (800, 65, 70, 20, "normal"),]