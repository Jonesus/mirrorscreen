import pygame
from pygame.locals import *
import math


class imgobj:
    
    '''
    Class holds coordinates for itself, the image to be rendered
    and the surface (display) which render to.
    
    Includes methods for fading image in and out and updating it.
    '''
    
    def __init__(self, x, y, img, display, size, maxhue = 255):
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        self.size = size
        self.hue = 0
        self.maxhue = maxhue
        self.display = display
        self.img = img
        self.img.set_alpha(self.hue)
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def reset_pos(self):
        self.x = self.startx
        self.y = self.starty
    
    def get_hue(self):
        return self.hue
    
    def increase_time(self, time):
        self.passed_time += time
        
    def zero_time(self):
        self.passed_time = 0
    
    def fade_in(self):
        self.hue +=  10
        self.hue = self.hue if 0 <= self.hue <= self.maxhue else self.maxhue
        self.img.set_alpha(self.hue)

    def fade_out(self):
        self.hue -=  10
        self.hue = self.hue if 0 <= self.hue <= self.maxhue else 0
        self.img.set_alpha(self.hue)
    
    def draw(self):
        self.display.blit(self.img, (self.x, self.y))
    
    def update_img(self, img):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.smoothscale(self.img, (self.size, self.size))
        self.img.set_alpha(self.hue)


