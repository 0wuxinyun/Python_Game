# ship:
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen):
        super(Ship,self).__init__()
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.rect.centerx=self.screenrect.centerx
        self.rect.bottom=self.screenrect.bottom
        self.rightmove=False
        self.leftmove=False
        self.upmove=False
        self.downmove=False

    def show(self):
        self.screen.blit(self.image,self.rect)
        
    def move(self):
        if self.rightmove and self.rect.right<900:
            self.rect.x+=10
        if self.leftmove and self.rect.left>0:
            self.rect.x-=10
        if self.upmove and self.rect.top>0:
            self.rect.y-=10
        if self.downmove and self.rect.bottom<600:
            self.rect.y+=10


            
    def restart(self):
        self.rect.centerx=self.screenrect.centerx
        self.rect.bottom=self.screenrect.bottom
        
    
            
