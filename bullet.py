# bullet
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()

        self.screen=screen
        self.ship=ship
        self.rect=pygame.Rect(0,0,30,5)
        self.rect.top=self.ship.rect.top
        self.rect.centerx=self.ship.rect.centerx
        self.bulletv=8
        self.color=(10,2,5)
        
        
    
        
    def show(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


    def update(self):
        self.rect.y-=self.bulletv

    

    
