# play button:
import pygame
import pygame.font
class Button(object):
    def __init__(self,screen,msg):
        self.msg=msg
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.buttoncolor=(145,40,59)
        self.textcolor=(230,75,96)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,200,50)
        self.rect.center=self.screenrect.center
        self.image=self.font.render(self.msg,True,self.textcolor,self.buttoncolor)
        self.imagerect=self.image.get_rect()
        self.imagerect.center=self.rect.center
    def draw(self):
        self.screen.fill(self.buttoncolor,self.rect)
        self.screen.blit(self.image,self.imagerect)
        


