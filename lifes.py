from ship import Ship
import pygame
from pygame.sprite import Group

class Lifes(object):
    def __init__(self,screen,ship):
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.life=3
    def show(self):
        self.lifes=Group()
        for num in range(self.life):
            newone=Ship(self.screen)
            newone.rect.y=10
            newone.rect.x=10+newone.rect.width*num
            self.lifes.add(newone)
        self.lifes.draw(self.screen)
            
