# scoreboard
import pygame.font
import pygame

class Score(object):
    def __init__(self,screen):
        self.primary=0
        self.text=pygame.font.SysFont(None,48)
        self.color=(255,78,90)
        self.screen=screen
        self.screenrect=self.screen.get_rect()
        self.newimage()
    def newimage(self):
        self.score=str(self.primary)
        self.image=self.text.render(self.score,True,self.color,(230,230,230))
        self.rect=self.image.get_rect()
        self.rect.top=self.screenrect.top+30
        self.rect.right=self.screenrect.right-20
    def show(self):
        self.screen.blit(self.image,self.rect)
    

