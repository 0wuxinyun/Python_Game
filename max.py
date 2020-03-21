# MAX
import pygame
import pygame.font
class Max(object):
    def __init__(self,screen):
        self.score=0
        self.text=pygame.font.SysFont(None,48)
        self.color=(34,56,1)
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.newimage()
        


    def newimage(self):
        self.image=self.text.render(str(self.score),True,self.color,(230,230,230))
        self.rect=self.image.get_rect()
        self.rect.centerx=self.screenrect.centerx
        self.rect.top=self.screenrect.top
    def show(self):
        self.screen.blit(self.image,self.rect)
