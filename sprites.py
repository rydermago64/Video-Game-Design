# This file was created by: Ryder Magobet


# imports from libraries, sprites, vectors, and pygame
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# my first class
# this is my player, a yellow pacman
# yellow pacman fitted to size in paint
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'pacman.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
        # spawn in timer when the red pacman hit him
        self.spawn_again = 60
        self.start_spawn_timer = True
# controls to move around my pacman, W, Y, S, D, and the space bar
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # function to respawn
        if self.spawn_again >= FPS*1:
            self.spawnpoint()
            self.spawn_again = 0
            self.start_spawn_timer = False
#
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        # this is the fucntion to respawn the pacman
        # spawn timer is 1 second in real life
        if self.start_spawn_timer:
            self.spawn_again += 1
    
    def spawnpoint(self):
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.rect.midbottom = self.pos
    


# My second class
# class for my plateforms
# and the code inside let the plateforms move
class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

# My third class
# class for my mobs (red pacman)

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'packman.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = vec(2, 2)
        self.kind = kind
        self.pos = vec(x, y)
        # function lets the mob move around the game, in a loop
    def seeking(self):
        if self.rect.x < self.game.player.rect.x:
            self.rect.x +=1
        if self.rect.x > self.game.player.rect.x:
            self.rect.x -=1
        if self.rect.y < self.game.player.rect.y:
            self.rect.y +=1
        if self.rect.y > self.game.player.rect.y:
            self.rect.y -=1
    def update(self):
        if self.game.player.rect.y < 250:
            self.seeking()
# makes sure the mobs come back once they get to the edge of the screen
    def update(self):
        if self.rect.left < 0:
            self.vel.x = 2
        elif self.rect.right > WIDTH:
            self.vel.x = -2
        if self.rect.top < 0:
            self.vel.y = 2
        elif self.rect.bottom > HEIGHT:
            self.vel.y = -2
        
        self.pos += self.vel
        self.rect.midbottom = self.pos
        # fourth and last class, my grapes
class Cherries(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'grapes.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(x, y)
# moves the plateoforms 
    def update(self):
        self.rect.midbottom = self.pos

       