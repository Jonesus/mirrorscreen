import pygame
from pygame.locals import *
import math


class textobj:
    
    '''
    Class holds coordinates for itself, the font it uses to render text,
    the text itself and the surface (display) which render to.
    
    Includes methods for moving text around with logarithmic speed,
    fading text in and out and updating the text.
    
    '''
    
    def __init__(self, x, y, font, text, display, dispw, disph, maxhue = 255):
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        self.hue = 0
        self.colour = (self.hue, self.hue, self.hue)
        self.font = font
        self.inputtext = text
        self.text = self.font.render(text, True, self.colour, (0, 0, 0))
        self.display = display
        self.dispw = dispw
        self.disph = disph
        self.maxhue = maxhue
        self.passed_time = 0
    
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
    
    def move_up(self, passed_time):
        px_to_move = int( self.speed * (passed_time / 1000) )
        self.y -= px_to_move if px_to_move >= 1 else 1
    
    def move_down(self, time):
        self.increase_time(time)
        self.y = (math.log(self.passed_time) * 9) + self.starty
    
    def move_right(self, time):
        self.increase_time(time)
        self.x = (math.log(self.passed_time) * 35) - 200 + self.startx
    
    def move_left(self, time):
        self.increase_time(time)
        self.x = self.dispw - (math.log(self.passed_time) * 35) - 32
    
    def fade_in(self):
        self.hue +=  10
        self.hue = self.hue if 0 <= self.hue <= self.maxhue else self.maxhue
        self.colour = (self.hue, self.hue, self.hue)
        self.text = self.font.render(self.inputtext, True, self.colour, (0, 0, 0))

    def fade_out(self):
        self.hue -= 10
        self.hue = self.hue if 0 <= self.hue <= 255 else 0
        self.colour = (self.hue, self.hue, self.hue)
        self.text = self.font.render(self.inputtext, True, self.colour, (0, 0, 0))
    
    def draw(self):
        self.display.blit(self.text, (self.x, self.y))
    
    def update_text(self, text):
        self.inputtext = text
        self.text = self.font.render(self.inputtext, True, self.colour, (0, 0, 0))

