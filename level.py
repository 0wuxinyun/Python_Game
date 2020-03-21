# LEVEL:
import pygame
import pygame.font

class Level(object):
    def __init__(self,screen,msg):
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.text=pygame.font.SysFont(None,48)
        self.color=(23,56,88)
        self.msg=msg
        self.newimage()
    def newimage(self):
        self.image=self.text.render(self.msg,True,self.color,(230,230,230))
        self.rect=self.image.get_rect()
        self.rect.top=self.screenrect.top+70
        self.rect.right=self.screenrect.right-20
    def show(self):
        self.screen.blit(self.image,self.rect)
