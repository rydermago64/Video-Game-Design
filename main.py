# This file was created by: Ryder Magobet


# Sources:
# Shawnik helped me with my code
# all images from google
# all rgb colors from google


# Game Design:
# Goals: Eat all 15 purple grapes with the pacman, watch out for red ghost because
# they will kill you, resulting in a respond, in 1 second, dont go negative in points, get all 20 points
# use the plateforms to get the grapes
 
# Rules, Dont stop moving, 
# watch out for mobs, run and jump, 
# don't go out of the screen

# Feedback, plus or minus points, FPS, 
# if you got responded, you hit and red ghost

# Freedom, jump around freely, move around freel



# import libraries and modules
# game is not possible without any of this
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

# vector class
vec = pg.math.Vector2

# for all the images and sounds inside the game, is set up here
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window, for the code to run
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    # my first class
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_Cherries = pg.sprite.Group()
        self.one_player = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)
        self.one_player.add(self.player)
# all my plateforms 
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
# all the red pacman, and how many spawn
        for m in range(0,10):
            m = Mob(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        #    all the grapes, and how many spawn
        for c in range(0,15):
            c = Cherries(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 0, 0, "normal")
            self.all_sprites.add(c)
            self.all_Cherries.add(c)


        self.run()
    # this is acually running the game in real like time (FPS)
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5
# gives the player a speed or gravity
                    
         # this stops the player from flying though a platform
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                # this prints ouch in the terminal if the player hits the bottem of a platform
                print("ouch")
                self.score -= 1
                if self.player.rect.bottom >= hits[0].rect.top - 1:
                    self.player.rect.top = hits[0].rect.bottom
                    self.player.acc.y = 5
                    self.player.vel.y = 0
# block of code allows the grapes to be eaten and at score for each one ate
        ghits = pg.sprite.spritecollide(self.player, self.all_Cherries, True)
        if ghits:
            self.score += 1
# block of code respawns the player if hit by red pacman, and sets a 1 second timer
        for mob in self.all_mobs:
            # function for if the yellow pacman colides with red pacman he dies and respawns 
            phit = pg.sprite.spritecollide(mob, self.one_player, False)
            if phit:
                self.player.start_spawn_timer = True

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites, and shows score on screen
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    # this function writes everything on the screen I have shown, like the score and what color and font it is
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
# passes start and go screen
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
# makes sure the game is running, becuase if you click the X button it goes to false and stops the game 
g = Game()
while g.running:
    g.new()

# quites game when user is ready to be done
pg.quit()
 