# alian
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen,ship,bullets):
        super(Alien,self).__init__()

        
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.image=pygame.image.load('alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.vx=6
        self.vy=self.rect.height
        self.direction=1
        self.check_edege1()
        self.update1()

    def update1(self):
        self.rect.x+=self.vx*self.direction
        

    def check_edege1(self):
        if self.rect.left<0:
            return True
        if self.rect.right>self.screenrect.width:
            return True

    def turn(self):
        if self.check_edege1():
            self.rect.y+=self.vy
            self.direction*=-1
        self.update1()
            
            

 


    
        
